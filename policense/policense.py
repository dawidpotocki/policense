#!/usr/bin/env python3

# Copyright (c) 2019, Dawid Potocki
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os
import subprocess
import sys
import textwrap

import licensename
import toml
from prompt_toolkit import HTML
from prompt_toolkit import print_formatted_text as fprint

from .__init__ import __version__
from . import options


def get_license_info(path_to_license):
    """Gets information about license, such as:
        * name
        * license text
        * description
        * is fsf/osi approved
        * is gpl compatible
        * linking (static, dynamic)
        * for what is intended
        * permissions
        * conditions
        * limitations
    """
    try:
        with open(path_to_license) as file:
            return toml.load(file)
    except FileNotFoundError as err:
        fprint(HTML(f"<ansired><b>Error: License not found</b></ansired>\n{err}"))
        exit()


def get_git_info(name):
    """Get git configuration info, e.g. user.name, user.email."""
    try:
        command = f"git config --get user.{name}".split()
        result = subprocess.check_output(command).strip().decode("utf-8")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    else:
        return result


def get_hg_info(name):
    """Get mercurial configuration info, name, email."""
    command = f"hg config ui.username --pager never".split()
    # ^ expected output:
    # Firstname Lastname <email@example.org>
    try:
        result = subprocess.check_output(command).strip().decode("utf-8").split()
        if name == "name":
            return_var = result[:-1]
        elif name == "email":
            return_var = result[-1]
            if return_var[0] == "<":  # we add it later, so we don't want it twice
                return_var = return_var[1:]
            if return_var[-1] == ">":
                return_var = return_var[:-1]
            return return_var
        else:
            return_var = result
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return " ".join(return_var)


def gen_license_text(license_text, year, fullname, email, projectname):
    """Returns modified license text
        Changes [year], [fullname], [email], [projectname]
        to passed values
    """
    license_text = license_text.replace("[year]", year)
    if fullname == "hg":  # git is default, so we only check for hg
        fullname = get_hg_info("name")
    license_text = license_text.replace("[fullname]", fullname)
    # We have space, because "[email]" is placed next to "[fullname]" without
    if email == "git":
        email = f" <{get_git_info('email')}>"
    elif email == "hg":
        email = f" <{get_hg_info('email')}>"
    elif email is not None:
        email = f" <{email}>"
    else:
        email = ""
    if email == " <None>":  # When get_hg_info or get_git_info failed
        email = ""
    license_text = license_text.replace("[email]", email)
    license_text = license_text.replace("[projectname]", projectname)
    return license_text


def print_license_data(license_name):
    """Prints license information
        * name
        * description
        * is fsf/osi approved
        * is gpl compatible
        * linking (dynamic, static)
        * for what is intended
        * permissions
        * conditions
        * limitations
    """
    license = get_license_info(f"{script_dir}/license/{license_name}.toml")
    fprint(HTML(f"<reverse><b>{license['name']}</b></reverse>"))

    for line in textwrap.wrap(license["description"], width=70):
        fprint(HTML(f"<i>{line}</i>"))

    if "references" in license:
        for i, link in enumerate(license["references"]):
            fprint(HTML(f"<ansiblue>[{i+1}] {link}</ansiblue>"))

    # FSF/OSI Approved
    if license["fsf"]:
        fprint(HTML("<ansicyan>FSF Approved ✔</ansicyan>"))
    else:
        fprint(HTML("<ansired>FSF Approved ✖</ansired>"))
    if license["osi"]:
        fprint(HTML("<ansicyan>OSI Approved ✔</ansicyan>"))
    else:
        fprint(HTML("<ansired>OSI Approved ✖</ansired>"))

    # Is compatible with GPL?
    if license["gpl_compatible"] is True:
        fprint(HTML("<ansicyan>GPL Compatible ✔</ansicyan>"))
    elif license["gpl_compatible"] is False:
        fprint(HTML("<ansired>GPL Compatible ✖</ansired>"))
    else:
        fprint(
            HTML(
                f"<ansicyan>GPL Compatible ✔<i>{license['gpl_compatible']}</i></ansicyan>"
            )
        )

    # Copyleft
    if not license["copyleft"]:
        fprint(HTML("<ansired>Copyleft ✖</ansired>"))
    else:
        fprint(HTML(f"<ansicyan>Copyleft ✔<i>{license['copyleft']}</i></ansicyan>"))

    # Allows static, dynamic linking?
    if license["static_linking"] is True:
        fprint(HTML("<ansicyan>Static Linking ✔</ansicyan>"))
    else:
        fprint(
            HTML(
                f"<ansired>Static Linking ✖<i>{license['static_linking']}</i></ansired>"
            )
        )
    if license["dynamic_linking"] is True:
        fprint(HTML("<ansicyan>Dynamic Linking ✔</ansicyan>"))
    else:
        fprint(
            HTML(
                f"<ansired>Dynamic Linking ✖<i>{license['dynamic_linking']}</i></ansired>"
            )
        )

    # For what stuff is licensed intended
    fprint(HTML(f"<ansimagenta>Intended for {license['intended_for']}</ansimagenta>"))

    # Permissions, Conditions and Limitations
    if "permissions" in license:
        fprint(HTML("\n<ansigreen>Permissions</ansigreen>"))
        for permission in license["permissions"]:
            print(permission)
    if "conditions" in license:
        fprint(HTML("\n<ansiblue>Conditions</ansiblue>"))
        for condition in license["conditions"]:
            print(condition)
    if "limitations" in license:
        fprint(HTML("\n<ansired>Limitations</ansired>"))
        for limitation in license["limitations"]:
            print(limitation)


def save_license_to_file(
    original_license_text, filename, email, year, fullname, projectname
):
    """Generates license and saves it to file, simple as that"""
    with open(filename, "w") as file:
        file.write(
            gen_license_text(original_license_text, year, fullname, email, projectname)
        )


def main():
    """Main function, mostly managing cli arguments"""
    args = options.get_args(get_git_info("name"), get_git_info("email"))
    if args.license is not None:  # --license, -l
        print(
            gen_license_text(
                get_license_info(f"{script_dir}/license/{args.license.upper()}.toml")[
                    "license"
                ],
                args.year,
                args.fullname,
                args.email,
                args.projectname,
            ),
            end="",
        )

    if args.save is not None:  # --save, -s
        if args.license is not None:
            license = get_license_info(
                f"{script_dir}/license/{args.license.upper()}.toml"
            )["license"]
            save_license_to_file(
                license,
                args.save,
                args.email,
                args.year,
                args.fullname,
                args.projectname,
            )
        else:
            fprint(HTML(f"<ansired><b>Error: Set --license/-l flag</b></ansired>"))

    if args.info is not None:  # --info , -i
        print_license_data(args.info.upper())

    if args.what is not None:  # --what, -w
        license = ""
        if args.what is False:  # if no argument passed
            if sys.stdin.isatty():  # if nothing piped
                args.what = "LICENSE"
            else:
                for line in sys.stdin:
                    license = license + "\n" + line
        try:
            license_name = licensename.from_file(args.what)
        except FileNotFoundError:
            license_name = licensename.from_text(license)
        if license_name is not None:
            print_license_data(license_name.upper())
        else:
            fprint(HTML("<ansired><b>Error: Unknown license</b></ansired>"))

    if args.version is not None:  # --version -v
        # I was bored, but rainbow looks nice
        fprint(
            HTML(
                "<ansired>p</ansired>"
                "<ansiyellow>o</ansiyellow>"
                "<ansigreen>l</ansigreen>"
                "<ansicyan>i</ansicyan>"
                "<ansiblue>c</ansiblue>"
                "<ansimagenta>e</ansimagenta>"
                "<ansiblue>n</ansiblue>"
                "<ansicyan>s</ansicyan>"
                "<ansigreen>e</ansigreen>"
                f" {__version__}"
            )
        )

    if len(sys.argv) == 1:  # No arguments passed
        print(f"Type: 'policense -h' to get some help.")


script_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    main()
