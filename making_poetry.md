One upon a time, Python did not have a decent command-line package manager like the vaunted [npm](https://www.npmjs.com/) for NodeJS.

That was then. Now there are good options in the Python world for package managers.

Recently, I've been able to try out both [Pipenv](https://pipenv.pypa.io/en/latest/) and [Poetry](https://python-poetry.org/) for some projects of mine. I feel like I've given both a try, and I prefer Poetry over Pipenv.

## What's Good, Overall
Both provide essentially the same good functionalities such as

- creating and managing a lock file for deterministic builds,
- allowing for pinning module versions, as well as just taking the latest version by default, and
- having a good CLI and workflow for working with Python projects.

## Pipenv - The Good Parts
Pipenv was the first package manager tool that I tried of these two. It definitely appealed to me, since it promises to combine [pip](https://pypi.org/project/pip/) (for dependency management) and [virtualenv](https://docs.python.org/3/tutorial/venv.html) (for environment management). Hence the name. 

Pipenv is really nice to use "off the shelf". If you are used to a Python workflow where you create a virtual environment first, then install dependencies, then start developing, Pipenv adds some efficiency. Instead of creating a `requirements.txt` file, you instead create a `Pipfile` file and list dependencies there. You can also run `pipenv install <module-name>` to add packages from command line and to your `Pipfile` as needed. These are good features. 

As well, you can either open a virtual environment in place according to the Pipfile configuration using `pipenv shell` or run a script added to the `Pipfile` by running `pipenv run <script-name>`. These are both handy utilities. Sometimes it's helpful to poke around and debug inside the virtual environment itself, and defining a script that will be executed regularly can be helpful. A script is a Python-based command. Some example of scripts defined in the Pipfile look like the following,

```
[scripts]
build = python setup.py install
lint = flake8 .
unit-test = pytest test/unit/
```

which can then be called using a command like

```
pipenv run build
pipenv run lint
pipenv run unit-test
```

This is definitely helpful for projects that have a few well-defined functionalities that need to be executed regularly. As of this writing, there doesn't appear to be any kind of auto-complete or suggestion features, which would be a nice touch given that scripts need to be defined in the `Pipfile`.

## Poetry - The Good Parts
As a project, Poetry does seem a bit more polished and buttoned up on first glance. The initial landing page and documentation is clean and modern. Definitely a good sign of things to come.

Poetry does make use of a configuration file called `pyproject.toml`. This file contains information such as dependencies and their versions, as well as information around PyPI publishing. You can optionally define scripts that can be executed, similar to how Pipenv handles scripts, but Poetry also allows for specific command line calls to be made directly. This is actually one of the two killer features for Poetry for me.

For example, suppose I have a `lint` command defined that will lint the entire project, but I want to specifically to lint just the `tests` directory. In poetry I can accomplish this by using the command line directly like

```
poetry run flake8 tests/
```

Poetry does allow adding dependencies from command line using `poetry add <module-name>`, or specific versions using something like `pipenv install <module-name>@1.2.3`.

As mentioned, Poetry does have built-in functionality to publish packages in addition to installing and building packages. This can be done directly by calling the simply named `poetry publish`. This is helpful for projects with multiple folks who need to publish, or just to simplify the existing workflows for publishing to PyPi. 

```
poetry publish
```

Easy breezy lemon squeezy.

## Why I like Poetry Better

While this isn't an exhaustive comparison, I think I prefer Poetry over Pipenv for one small thing and one big thing. 

The small thing is package publishing. I have consulted the same section of the [same Medium article for how to publish to PyPI](https://medium.com/@prudhvi.gnv/how-to-publish-your-own-python-package-in-pypi-5037ca21dd82) for a while now. I almost always forget some step. Poetry packages this process up neatly (pun intended) which makes the publishing process a bit smoother. You can also configure the `pyproject.toml` with credentials for team workflows and build pipelines if needed.

The bigger reason is how Poetry handles virtual environments. 

Poetry almost fully encapsulates virtual environments. You almost don't even know you're using one, for whatever tasks that you end up executing. Dependency installation, development, building and publishing is all done via the `poetry <commands>` CLI. Where virtual environments are kept and how they are managed is basically invisible to the end user, including in the cases where different Python versions are used. Create the `pyproject.toml` and off you go. 

Pipenv does not take this approach, and does expose some of the virtual environment(s) to end users. This feels natural at first if you're comfortable with virtual environment usage, but eventually it just gets cumbersome. 

For example, consider the `pipenv shell` command. This command opens a virtual environment instance, which is a typical Python workflow. Using the `shell` command works great, until it doesn't. Pipenv manages virtual environments itself but will also try to use existing local virtual environments as well. If there is an existing virtual environment directory in the project, Pipenv sometimes errors if it cannot cleanly create or select the "default" virtual environment Pipenv created. This can lead to less than ideal situations. As well, if Pipenv is managing a virtual environment, resetting dependencies or even deleting the virtual environment and starting over (a hack I use sometimes with virtual environments) is difficult or tricky. 

Another issue that arises out of this lack of abstraction is running one-off or non-standard script commands. Suppose I'm back at my scenario above where I want to link only the `tests` directory. In Pipenv the options I have are

- create a new script in the `Pipfile` just for this task (annoying),
- manually update the `pipenv run lint` script for my one use case (annoying and possibly easy to check-in to version control, causing shenanigans), or
- run the command via `pipenv shell` (see above for problems in this case).

Poetry avoids these situations by abstracting the entire virtual environment concept away. There is no `poetry shell` command or analog, since the usage of a virtual environment is completely hidden. These edge cases aren't all that edgy really, and Poetry is well thought out from this perspective.

I do think Pipenv is a decent tool, but it is better suited to smaller Python projects or relatively static projects where the same scripts and commands are called often without any modification or updates. 

Both tools have their place, but sometimes what you really need is just a hint of encapsulation, as a treat.