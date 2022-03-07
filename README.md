# iclingo

[![Compatible python versions](https://img.shields.io/pypi/pyversions/iclingo)](https://badge.fury.io/py/iclingo)
[![build workflow
badge](https://img.shields.io/github/workflow/status/thesofakillers/iclingo/build)](https://github.com/thesofakillers/iclingo/actions/workflows/build.yml)
[![PyPI version](https://badge.fury.io/py/iclingo.svg)](https://badge.fury.io/py/iclingo)

🔴🟢🔵 [clingo](https://potassco.org/clingo/) kernel for
[Jupyter](https://jupyter.org/).

## Install

To install, simply run

```console
pip install iclingo
python -m iclingo.install
```

## Usage

Once installed, you can run clingo code directly in jupyter, alongside typical
jupyter functionality such as markdown cells. An example of this is available in
[examples/](examples/).

### Limitations

- No syntax highlighting is available
- Currently, no configuration options can be passed to a given cell. This means
  that the default clingo options are used, such that for a problem with
  multiple answers, only the first answer is shown.
- Multi-shot solving is not supported

## Development

This repository is mostly based on the documentation presented in
[_Making simple Python wrapper kernels_](https://jupyter-client.readthedocs.io/en/stable/wrapperkernels.html).

We use [poetry](https://python-poetry.org/) to track dependencies and build our
package.

[GitHub Actions](https://github.com/features/actions) are then used for
automatic publishing to [PyPi](https://pypi.org/) upon pushes of
[git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) to the repository.

When ready to publish the latest commit, simply run the following:

```console
git tag $(poetry version --short)
git push --tags
```

Pull requests and contributions are more than welcome. Please refer to the
[relevant page](https://github.com/thesofakillers/iclingo/contribute).
