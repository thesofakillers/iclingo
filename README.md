# iclingo

🔴🟢🔵 [clingo](https://potassco.org/clingo/) kernel for
[Jupyter](https://jupyter.org/).

## Install

To install, simply run

`pip install iclingo`

## Usage

Once installed, you can run clingo code directly in jupyter, alongside typical
jupyter functionality such as markdown cells. An example of this is available in
[examples/](examples/).

### Limitations

- No syntax highlighting is available
- Currently, no configuration options cannot be passed to a given cell. This
  means that the default clingo options are used, such that for a problem with
  multiple answers, only the first answer is shown.
- Multi-short solving is not supported
