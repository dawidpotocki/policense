policense(1)

# NAME

policense - Licensing, simplified.

# SYNOPSIS

*policense* [options...] [command]

# OPTIONS

*-h, --help*
	Show help message and quit

*-l, --license <license_name>*
	Print license text.
	Licenses are named according to SPDX identifiers (if they exist).
	There are some symlinks, so you don't have to remember them 100% correctly.
	If there are multiple version of license, when you type without version, it will link to newest (GPL -> GPL-3.0).
	Letter case don't matter, it will be made internally upper anyway.
	By default changes [fullname] to your git name, [year] to current year and [email] to empty string.

	*-fn, --fullname*
		Replaces [fullname] to your name

	*-y, --year*
		Replaces [year] to specified year

	*-e, --email*
		Replaces [email] to specified email.
		When "git" or "hg" passed, changes to email from these tools.

	*-pn, --projectname*
		Replaces [projectname] to specified project name.
		Appears in only few licenses, like X11 and BSD-3-Clause.

*-i, --info <license_name>*
	Prints information about license.
	Licenses are named according to SPDX identifiers.
	There are some symlinks, so you don't have to remember 100% correctly.
	If there are multiple version of license, when you type without version, it will link to newest (GPL -> GPL-3.0).
	Letter case don't matter, it will be made upper anyway.
	The following will be displayed:
		- name
		- description
		- is approved by Free Software Foundation
		- is approved by Open Source Initiative
		- is compatible with GPL
		- allows dynamic and/or static linking without changing license
		- for what it is intended (software, media, fonts)
		- permissions
		- conditions
		- limitations

*-w, --what <filename_or_licensetext>*
	Shows name of license that file/text contains.
	When no argument is passed, defaults to reading from stdin or file named "LICENSE".

*-s, --save <filename>*
	*-l, --license flag required*
	Saves license text to file. When no argument is passed, defaults to "LICENSE".

*-v, --version*
	Shows version, like really, what can you expect?

# AUTHORS

Dawid Potocki

# DEVELOPMENT

If you want to contribute or found bug, visit https://github.com/dawidpotocki/policense
