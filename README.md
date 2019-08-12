<img src="https://raw.githubusercontent.com/dawidpotocki/policense/master/img/policense.svg?sanitize=true" width=350px />

_Licensing, simplified._

## Install

```
$ pip3 install --user policense
```

### Generate license text (`-l, --license`)

Licenses are named according to [SPDX identifiers](https://spdx.org/licenses/).
There are some symlinks, so you don't have to remember 100% correctly (2BSD, BSD2 -> BSD-2-Clause)
If there are multiple version of license, when you type without version, it will link to newest (GPL -> GPL-3.0).
Letter case of license names don't matter, why should it?

```shell
$ policense -l BSD-2-Clause
$ policense -l 2BSD
$ policense -l BSD2
$ policense -l bSd-2-cLaUsE
```

###### output

Even though we did not pass our name, policense got it from our git config.

```
BSD 2-Clause License

Copyright (c) 2019, Dawid Potocki
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

#### Add email (`-e, --email`)

Adds email specified to license text.
If `git` or `hg` specified, it will get email from these tools.

```shell
$ policense -l ISC -e git
```

###### output

```
Copyright (c) 2019, Dawid Potocki <dpot@disroot.org>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

### Save license to file (`-s`, `--save`)

If after `-s` filename is not specified, it will default to `LICENSE`.

```shell
$ policense -l 0BSD -s COPYING
```

### Show TL;DR of license

```shell
$ policense -i BSD-2-Clause
```

###### output (it actually has noice colors)

```
BSD 2-Clause "Simplified" License
A permissive license similar to the BSD 3-Clause License, but without
a 3rd advertising clause.
FSF Approved ✔
OSI Approved ✔
GPL Compatible ✔
Copyleft ✖
Static Linking ✔
Dynamic Linking ✔
Intended for software

Permissions
Commercial use
Distribution
Modification
Private use

Conditions
License and copyright notice

Limitations
Liability
Warranty
```

## NAQ (Never Asked Questions)

> Can you add license X?

If there is a SPDX identifier, then I don't see a problem.
It would be nice if you could help with that.
Look at [CONTRIBUTING.md](CONTRIBUTING.md)

## FAQ (Frequently Asked Questions)

Yes
