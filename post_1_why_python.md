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

Typically Windows and Mac operating systems do not include Python by default. Luckily, installation is straighforward in both cases. Both