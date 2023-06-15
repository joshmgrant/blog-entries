If you are currently working on a production codebase using Python 2.7 and/or using Nose in your test framework, stop what you're doing and read this. 

(If you're working with Python 3 or not using Nose, you can read this too, I won't mind.)

You need to start using [Pytest](https://docs.pytest.org/en/latest/). 

I'm usually not one for hard opinions with sweeping generalizations but I've been thinking about this and I think this is good move overall. 

I'm recommending moving off Nose in Python 2.7 to Pytest in Python 3 (maybe 3.4 or later) because both [Nose is dead](https://nose.readthedocs.io/en/latest/#note-to-users) and [Python 2.7 is soon to be dead](https://pythonclock.org/ ). This means getting updates, new features and bug fixes is going to slow to a halt soon. Your test framework will be frozen in ice and it will be tougher to keep up. 

As well, Pytest has pretty good support for integrating with Nose. It also works well with Python 2.7 and works mostly well with unittest, with some caveats. Test frameworks will have to make a few tweaks but they should be straightforward and not an entire overhaul. You can also use Pytest as a runner at first instead of a full test framework. Working up to replacing Nose/Python 2.7 with Pytest/Python 3. 

So, how to do this? One thing that's worked for me is using a [Red, Green, Refactor](https://www.codecademy.com/articles/tdd-red-green-refactor) approach. This looks like:

1. **Red**: Install the latest version Pytest and run your nose tests using it instead of `nosetests` . This is low effort and should work with Python 2.7 and Python 3.4+. It will also likely produce errors and/or invalid test failures. 

Completing the **Red** step is both fairly simple and _critical for getting started_. I cannot stress enough to start with this step. 

2. **Green**: After running existing tests with Pytest, examine the errors and failures and make some changes. This could mean making changes to setup or configuration files, changing some `setUp`/`tearDown` methods in classes, or other things. It might also mean trying older versions of Pytest. Make iterative changes until you get something working (tests in the same pass/fail state as before).

3. **Refactor**: Once you have a Pytest as your runner and tests are running mostly as before, you can start to remove Nose functionality like `@with_setup()` decorators and unittest conventions like subclassing `unittest.TestCase` or class-level `setUp` and `tearDown` functions. You can replace this kind of functionality with [Pytest fixtures](https://docs.pytest.org/en/latest/fixture.html) which provide the same functionality but with more flexibility. 

Follow this pattern in order and you'll find your happy place with Pytest (or at least much happier than using Nose). 
