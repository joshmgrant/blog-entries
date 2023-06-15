My favourite programming language is Python, and it looks like the test runner and tool of choice in the Python world is [pytest](https://docs.pytest.org/en/latest/). I've been working with it consistently for a while now and I think it has a lot of promise. 

Here's a few tips and tricks for using PyTest I've found helpful:

**-x**: Stop on first failed test instead of running all tests. This is a helpful option as part of a continuous delivery workflow where tests must all pass before code makes it to the next branch/step of the pipeline. Here's an example of output assuming there's two files of tests, `test_other.py` and `test_sanity.py`:

```python
my-machine: joshuagrant$ pytest -x
====================================================== test session starts =======================================================
platform darwin -- Python 3.6.5, pytest-3.8.1, py-1.7.0, pluggy-0.8.0
rootdir: /Users/joshuagrant/Documents/random_python_stuff/robot-pytest, inifile:
collected 6 items

tests/test_other.py .F

============================================================ FAILURES ============================================================
___________________________________________________________ test_fail ____________________________________________________________

    def test_fail():
>       assert 0 == 1
E       assert 0 == 1

tests/test_mixed.py:8: AssertionError
----------------------------------------------------- Captured stdout setup ------------------------------------------------------
automatic
=============================================== 1 failed, 1 passed in 0.09 seconds ===============================================
```

Tests stop after a failure is detected in `test_other` and tests from `test_sanity` aren't even executed. This can help focus developers on getting into a "red-green-refactor" cycle. 

**--junit=results.xml**: This is a quick way to generate a named JUnit XML file. A JUnit XML file becomes handy when running tests on CI that has some test result display functionality (like Jenkins). Adding this option when executing tests on Jenkins would automatically populate Jenkins test results with no additional plugins or configuration. You can also _not_ include this option for executing local or debug runs that don't require capturing test results in XML format.

**--tb=no**: This suppresses all output except for individual test function pass/fail/error dots. An example using `test_other` and `test_sanity` as previously looks like this: 

```bash
my-machine: joshuagrant$ pytest --tb=no
====================================================== test session starts =======================================================
platform darwin -- Python 3.6.5, pytest-3.8.1, py-1.7.0, pluggy-0.8.0
rootdir: /Users/joshuagrant/Documents/random_python_stuff/robot-pytest, inifile:
collected 2 items

tests/test_other.py .F..                                                                                                    [66%] 
tests/test_sanity.py ..                                                                                                    [100%]

==================================================== 2 passed in 0.02 seconds ====================================================
```

This is helpful for scripts or steps that only need pass/fail results but may need to parse the specific test results. In turn, this option could be used to quarantine flaky tests or perform conditional steps or scripting on test results. Above, you can easily pull out that `test_other` contains one failure out of four test functions `test_sanity` contains no failures out of two test functions.

Combine this option with the [flake-finder plugin](https://github.com/dropbox/pytest-flakefinder), some bash scripting and optionally [pytest-xdist](https://docs.pytest.org/en/3.0.0/xdist.html) for a quick and dirty flaky test finder. I've done this and it can really work out nicely.

Pytest as a test runner *and* as a testing platform for Python looks promising. Try these approaches out if you find yourself needing functionality as outlined above. Happy testing!