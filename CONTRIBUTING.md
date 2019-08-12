# Contributing to policense

Oh, so you want to contribute? That's great.

## Setup

To get started, you should clone repository and install dependencies.

```shell
$ git clone https://github.com/dawidpotocki/policense.git
$ cd policense
$ pip3 install --user poetry
$ poetry shell
$ poetry install
$ python3 -m policense
```

## Build

```shell
$ poetry build
$ cd dist
$ pip3 install --user policense-{version}.tar.gz
```

## Formating

Before you commit, you should format Python code using [black](https://github.com/python/black).
It fixes inconsistency and makes code look great (in my opinion).
For TOML, add trailing commas `,` in lists and use `'` where possible for strings.

## Adding license files

To add new license, copy file `policense/license/template/LICENSE.toml` and name it according to [SPDX identifier](https://spdx.org/licenses/).
If license doesn't have a SPDX Identifier, it _probably_ shouldn't be added.
Some stuff is already prepared, to make your life easier.
At the end we have license text and last ''' should be at the same line as last word of license instead of below (so we don't have \n at the end).
Remember to remove stuff that is not needed (like comments and empty lists)
Like in Unlicense there are no "conditions", so we just remove it.

## Fixing license info

If you noticed wrong information about a license, please create an issue or merge request on GitHub.
