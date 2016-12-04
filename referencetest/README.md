
TDDA Reference Test, a wrapper for unit-testing frameworks, providing
support for reference-testing through Test-Driven Data Analysis.

Supports both unittest and pytest.


Explanatory examples of how to use `writabletestcase` are in the `examples`
subdirectory.

Use

    cd examples
    python test_using_writabletestcase.py

to run an example test.

See doc strings inside to see how to make the tests fail, then re-write
the output.

Briefly: edit the generation functions in `examples/generators.py`
to generate different output, re-run the tests, see them fail, check
the output and then run

    python test_using_writabletestcase.py -w

to re-write the reference output in `examples/reference`,

after which if you run again with

    python test_using_writabletestcase.py

Test tests should pass again.

Obviously, you should only rewrite the test output after carefully verifying
the the changes are OK!

All examples, tests and code should run under Python2 and Python3.
