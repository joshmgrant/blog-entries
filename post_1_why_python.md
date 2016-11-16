# How To Use Python To Automate Almost Anything

## Why Python?

Congratulations, you've decided to try automating some of your tasks! Good automation can help free up time and computing resources, make tasks cleaner and uniform, and can sometimes even help do things that are impossible otherwise. For modern software testers, having familarity with automation approaches and tools is almost essential. Using automation well can be make testing efficient and even more enjoyable, 

Scripting languages like Python are a great choice for simple automation tasks. Why use Python? 

- **It's Cross-Platform.** Python work well on Micorsoft Windows, Mac OSX and most mainstream versions of Linux such as CentOS, Ubuntu and Debian. Simple scripts can be written that are perfectly portable from one operating system or environment to another. This is means that using Python doesn't bind testers to a particular environment. This can be helpful for using automation in multi-platform settings that testers may encounter and work with regularly. It's also beneficial because Python scripts will work well on operating systems as they update from version to version.

- **It's Fun To Write.** For software testers, automation often - but not always - means working with a programming language. This means writing code. Programming language syntax comes in all shapes and sizes, all of which come with a particular philosophy. Python's [underlying philosophy](https://www.python.org/dev/peps/pep-0020/) is to focus on simplicity, readability and being able to integrate various components together well. Python has a syntax that makes scripts look uniform, even from author to author. Scripts also tend to make intention clear even with a casual glance.

- **It's a Mainstream Language With A Mature Ecosystem.** While the language itself is important, the ecosystem around it is also helpful. This includes both the community aspect and tooling aspect. Python has a mature ecosystem, meaning that there are mature conventions and tools around how Python is used. Conventions include rules for writing ["clean" code](https://www.python.org/dev/peps/pep-0008/) and common set-ups for Python projects. Python has first-class language tools such a [package manager](https://pypi.python.org/pypi/pip/) for getting libraries for different utilties (called modules in Python), a full-featured intepreter, developer tools such as IDE support, and so on. There's a wealth of knowledge available online and offline for Python that any tester can tap into if they need it.

- **Lots of Cool Modules and Tools To Do Almost Anything.** As a scripting language, Python has a large number of modules to help with a variety of tasks. This means that scripts can take advantage of existing functionality instead of writing lines of code from scratch. Modules that could be of interest for testers are [processing HTML](https://www.crummy.com/software/BeautifulSoup/), [reading and writing Excel files](http://openpyxl.readthedocs.io/en/default/), [generating random values](https://docs.python.org/2/library/random.html) and [driving a web browser](http://selenium-python.readthedocs.io/api.html). Python also has more typical programming features like text manipulation and reading and writing to text files. With Python it really is possible to automate almost any task on a typical computer. 

Based on all that, how could any tester not want to automate things with Python? Let's get started. 

## Getting started

Now that we've seen all the good stuff Python can do, let's go through setting up Python for usage. As mentioned previously, Python is a cross-platform language and is available on Windows, Mac and Linux operating systems. These sections will walk through getting Python set up on common operating systems. The rest of this article will be based on the latest major version of Python (3.5 as of now). 

### Linux and Mac OS

Both Linux and Mac OS include versions of Python by default on recent OS versions.  You can check by open opening a terminal typing `python --version` and hitting enter. This should tell you the Python version installed on the system or throw an error. 

If Python is missing on your Linux operating system, you can usually install it using your operating system's package manager. For example, Ubuntu uses apt-get and Python can be installed by typing `apt-get install python` and hitting enter (you may need to use `sudo` here based on your operating system permissions). If you use another Linx distribution, check your package manager to see if Python is included.  

If Python is missing your Mac operating system, or you need to update it, you can use [Homebrew](http://brew.sh/) to install Python by opening a terminal, typing `brew install python3` and hitting enter. 

### Windows

Typically Windows operating systems do not include Python by default. Luckily, installation is straighforward. Find the [latest version of Python](https://www.python.org/downloads/windows/) and download the installer. All major versions of Python have full Windows installers that configure Python. 

### What Comes With Python

Installing Python installs several components. The central component is the Python intepreter. This is called by typing `python` into a terminal and hitting enter. When called like this with no arguments, it starts a Python [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) that allows Python commands to be called in an isolated, safe way. This is a great way to try Python commands. When called with a Python script in the form `python /path/to/script.py` the Python interpreter tries to execute the contents of the script. This is the other common usage of the Python interpreter.

The other tool that is installed with Python is its package manager, called Pip. Pip allows Python modules for a whole variety of tools to be installed. The usual way of installing Python modules using Pip is to call `pip install --update MODULE_NAME`. This will install the module with the given name if it hasn't been installed, or update it the module if it has been installed. More information on Pip can be found on the [official documentation pages](https://pip.pypa.io/en/stable/) if you're interested beyond the basic usage.

Along with modules installed using Pip, Python comes with some standard modules. These are mainly based on common programming usage such as working with file systems (the [os](https://docs.python.org/3/library/os.html) and [sys](https://docs.python.org/3/library/sys.html) modules). 

With Python set up, the next step is to think of a good scripting project. Let's see what we can do!

## Project Idea: Automating Creating Test Users

Python scripting is always fun but it's good to have a goal in mind when starting a project. Here, we'll look at using the Selenium WebDriver to help with some a fairly common task when testing a web application. 

Here's a situation that may be familiar to many testers. A bug is reported in your app that occurs when there are a large number of user accounts created on the app. To either reproduce the bug or to explore the case, it would be helpful (or even necessary) to add a large number of user accounts to your app under test. In particular, creating user accounts sometimes means coming up with unique fields and or identifies, like unique email addresses. Doing this may be time consuming and repetitive, which in turn can lead to boredom and human error. Situations like this can be annoying and problematic for testers. 

The solution to this problem is automation. It's a perfect case for automation since it involves doing a specific task over and over several times. It also allows for easy scaling, whether creating ten users or ten thousand test users. We're also in luck because Python has WebDriver bindings, which means we can use it "off-the-shelf" as a Python module. The WebDriver is a great tool for driving and controlling a web app in a browser. 

Let's start scripting!

## Writing the Script



Given this scenario,  