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

As an example of an app, I've created a [rough test app](http://joshmgrant.github.io/UserGenerator/login.html). It's very narrow in scope and not even really functional but it will work as a good test app for trying out WebDriver.

Let's start scripting!

## Writing the Script

The first thing we need to write this script is to get the WebDriver module. To do this we use Pip. Open a terminal, and type `pip install --update selenium`. This will install the modules needed for the Selenium WebDriver. To keep things simple, we will use Chrome for our testing, so make sure you have installed the latest Chrome browser. You'll also need the Chromedriver, which is an executable the WebDriver uses to access browser internals. It can be downloaded [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Download unzip the `chromedriver` executable and put it somewhere it can be accessed globally. On Windows, you could add it to `C:\Chromedriver\chromedriver.exe`. We will assume it's in this location but you can place it anywhere valid on your file system. It doesn't matter where you locate the Chromedriver but you will need the path for the script. 

Other than Selenium, we can write a script with all built-in Python modules. Here's an example of a [finished product found on Github](https://github.com/joshmgrant/TestUserGenerator/blob/master/generate_users.py). You can clone that repository or copy/paste the code from that file and try it by typing `python generate_users.py`. If there's no problems, a browser will open up, log into the test app then add ten test users. 

Let's walk through this script in sections, starting with the top section.

    from selenium import webdriver
    import time
    import random
    import string

These are imported modules that give us some additional functionality. The first line imports the WebDriver components of the Selenium module (which contains some other utilities). This allows us to drive the browser. The other import statements give us tools for timing (`time`), generating random values (`random`), and string sets and manipulation (`string`). Other than the WebDrive, there are standard modules that come with Python 3. 

We can set the number of users we want to generate using a variable. In this case, we write

    NUMBER_OF_USERS = 10

Python uses dynamic typing, so we can create variables without deciding explicitly what type it is. In this case, we declare a variable to be an integer number. 

Next we can start a browser using the WebDriver, in this case using the lines 

    driver = webdriver.Chrome("C:\\Chromedriver\\chromedriver.exe")
    driver.get("http://joshmgrant.github.io/UserGenerator/login.html")

This starts a new Chrome instance and navigates to the test application. We will use the `driver` object to manipulate the browser in this script. In the next steps, we can locate the user name and password fields to work with. Using the lines 

    driver.find_element_by_id("username").send_keys("admin@testcorp.com")
    driver.find_element_by_id("password").send_keys("p4zzW0Rd")
    driver.find_element_by_name("login").click()

the script finds the user name and password fields by their id attribute then sets text in their fields with valid credentials. The script also finds the Login button but this time by the name attribute then clicks it.  

These elements are found using functions based on the `find_element` method of the WebDriver. This is really the workhorse of the WebDriver and likely the main method called to retrieve elements from [the Document Object Model (DOM) layer](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) of a web app. This is a layer that is below the actual UI and gives developers something to either attach to or manipulate in a web app. The Selenium WebDriver makes use of the DOM and is what gives the WebDriver so much flexibility to interact with elements on a page. 

Now we can introduce the first logical construct, a for-loop. This is one of [my favourite programming constructs](http://simplythetest.tumblr.com/post/145304551395/why-i-cant-quit-for-loops). 

    for i in range(NUMBER_OF_USERS):

Essentially this allows a block of code to be repeated a specifed number of times. In this case, we repeat the code block adding a new user the specified number of times based on the `NUMBER_OF_USERS` variable. In particular, `range()` creates an array of values of the length of the number of users which is then iterated over in order. Non-blank lines that are to be executed within the loop are preceeded by a single tab character, which is the syntax for any logical grouping in Python.  

In the loop, we can generate random test users using the `random` and `string` modules. These lines 

    random_id = ''.join(random.choice(string.digits) for i in range(3))
    random_first = "user"
    random_last = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))
    random_email = random_first + random_last + "@testcorp.com"

These lines create necessary values for a user first name, last name, user id and email. The first name is given a constant value of `user` for simplicity, and a random last name containing letters and digits is created. An employee id is created using a random set of digits. An email is then created by combining the first and last names.

The lines 

    driver.find_element_by_id("userEmail").clear()
    driver.find_element_by_id("userEmail").send_keys(random_email)

    driver.find_element_by_id("userIdCode").clear()
    driver.find_element_by_id("userIdCode").send_keys(random_id)

    driver.find_element_by_id("newUserFirst").clear()
    driver.find_element_by_id("newUserFirst").send_keys(random_first)

    driver.find_element_by_id("newUserLast").clear()
    driver.find_element_by_id("newUserLast").send_keys(random_last)
    
    driver.find_element_by_id("newUserButton").click()

    time.sleep(2) 

then send these random user values to the respective fields using `find_element` methods after first clearing the text fields. By default `send_keys` does not do any logic while sending keys, so fields need to be cleared separately. 

We also add a two second delay at the end of each user creation to properly synchronize some actions in each iteration. 

Finally, we close the browser session using the commands

    driver.quit()

## Common Pitfalls or problems

This script was written to work "off-the-shelf" without any changes. However, there may be some problems that lead to this script not working well. These are problems common to most WebDriver-based scripts. 

**Browser Not Found**: Sometimes an error will be thrown if a browser specified by the WebDriver is not available or installed. If you see this, definitely confirm you have installed the latest Chrome browser.

**Selenium Module Not Found**: This problem occurs when you run the script without the Selenium modules installed properly. See the previous section to install Selenium via Pip if you see this issue. 

**Can't Reach the Test App**: This can happen if you have no Internet connection. This has happened to me even in professional software environments. Make sure the machine you run this script on is connected online. 

**Element Not Found Exceptions**: If one of the `find_element` calls fail, it may be due to an element not appearing properly or "in time". This could be due to a slow Internet connection, poor browser performance or an overall underpowered machine. Elminiating these problems can be tricky, but there are a number of approaches. The simplest is to add in some sleep statements, even this is not recommended in general.

Now that we've written the script we can run it as needed and reap the benefits of automation. 

