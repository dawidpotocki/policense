#!/usr/bin/env python3

# Copyright (c) 2019, Dawid Potocki
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import argparse
import datetime


def get_args(gitname, gitemail):
    """Gets arguments from cli"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--license", "-l", metavar="LICENSE_NAME", help="show license text"
    )

    parser.add_argument(
        "--info", "-i", metavar="LICENSE_NAME", help="show tl;dr of license"
    )

    parser.add_argument(
        "--what",
        "-w",
        nargs="?",
        default=None,
        const=False,
        metavar="FILENAME_OR_TEXT",
        help="finds what license file/text contains (text can be piped)",
    )

    parser.add_argument(
        "--save",
        "-s",
        nargs="?",
        default=None,
        const="LICENSE",
        metavar="FILENAME",
        help="save license to a file (default is file named LICENSE)",
    )

    parser.add_argument(
        "--fullname",
        "-fn",
        nargs="?",
        default=gitname,
        help="replace [fullname] in license, without this flag, it gets name from .gitconfig",
    )

    parser.add_argument(
        "--year",
        "-y",
        default=f"{datetime.datetime.now().year}",
        help="replace [year] in license, without this flag, it gets from your local time",
    )

    parser.add_argument(
        "--email",
        "-e",
        nargs="?",
        default=None,
        const=gitemail,
        metavar="EMAIL",
        help="replace [email] in license, giving `git` or `hg` as argument will get it from these tools",
    )

    parser.add_argument(
        "--projectname",
        "-pn",
        default="[projectname]",
        metavar="PROJECT_NAME",
        help="replace [projectname] in license",
    )

    parser.add_argument(
        "--version",
        "-v",
        nargs="?",
        const="store_true",
        default=None,
        help="print version",
    )

    return parser.parse_args()
