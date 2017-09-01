pytest useful commands:

`pytest --version   # shows where pytest was imported from`

`pytest --fixtures  # show available builtin function arguments`

`pytest -h | --help # show help on command line and config file options`

`pytest -x            # stop after first failure`

`pytest --maxfail=2    # stop after two failures`

`pytest -k "MyClass and not method"`

`pytest testing/`  running a directory

`pytest test_mod.py::TestClass::test_method` Running specific test nodes

`pytest --pyargs pkg.testing` Run tests from packages

**Modifying printing:**

`pytest --showlocals # show local variables in tracebacks`

`pytest -l           # show local variables (shortcut)`

`pytest --tb=auto    # (default) 'long' tracebacks for the first and last // entry, but 'short' style for the other entries`
                     
`pytest --tb=long    # exhaustive, informative traceback formatting`

`pytest --tb=short   # shorter traceback format`

`pytest --tb=line    # only one line per failure`

`pytest --tb=native  # Python standard library formatting`

`pytest --tb=no      # no traceback at all`

`pytest --pdb` Going into debug 

`pytest --junitxml=path` to generate a html report at given path

