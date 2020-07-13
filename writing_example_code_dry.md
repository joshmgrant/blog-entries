After a long hitaus due to, well, basically everything, I am continuing my series on [how to write good example code](https://simplythetest.tumblr.com/post/612302779439087616/writing-example-code-a-series). 

In the previous post, I discussed how [you ain't gonna need YAGNI](https://simplythetest.tumblr.com/post/615769806536327168/writing-example-code-you-aint-gonna-need-yagni) despite the fact that YAGNI is often a good principle to follow when writing software. Following along these lines, I'm going to discuss another good coding principle - [Don't Repeat Yourself or DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) - and why it's not so spry when it comes to writing example code. 

The main idea of DRY is pretty straightforward: avoid repeating code and/or abstractions in different places. DRY is less of an ironclad rule and more of a helpful guideline. Here's an example from object-oriented programming. Suppose I have three classes that represent entities in the Josh Labs system, `User`, `Account` and `Platform` and they look like this:

```python
class User():

    def __init__(self, name, is_active=True):
        self.jl_id = self.set_id()
        self.name = name
        self.is_active = is_active

    def set_id(self):
        return complicated_id_hash_function()

    def deactivate(self):
        self.is_active = False

class Account():

    def __init__(self, name, is_active=True):
        self.jl_id = self.set_id()
        self.name = name
        self.account_number = ''
        self.is_active = is_active

    def set_id(self):
        return complicated_id_hash_function()

    def set_account_number(self, num):
        self.account_number = num

    def deactivate(self):
        self.is_active = False

class Platform():

    def __init__(self, name, is_active=False):
        self.jl_id = self.set_id()
        self.name = name
        self.is_active = is_active

    def set_id(self):
        return complicated_id_hash_function()

    def deactivate(self):
        self.is_active = False
```

The above classes are valid, but contain some repetition in some of the members and methods. The `jl_id`, `name` and `is_active` members are common to each class, as well as some of the associated methods. Also note that `Account` has some additional members and methods over `User` and `Platform`. If more classes were added this way, there could be errors in duplication since these fields were added by hand. Using the DRY principle, let's put all these common fields into a super class and use inheritance to reduce repetition: 

```python
class Entity():

    def __init__(self, name, is_active=True):
        self.jl_id = self.set_id()
        self.name = name
        self.is_active = is_active

    def set_id(self):
        return complicated_id_hash_function()

    def deactivate(self):
        self.is_active = False

class User(Entity):

    def __init__(self):
        super().__init__(name, is_active=True)

class Account(Entity):

     def __init__(self):
        super().__init__(name, is_active=True)
        self.account_number = ''

    def set_account_number(self, num):
        self.account_number = num

class Platform(Entity):

     def __init__(self):
        super().__init__(name, is_active=False)
```

Using inheritance is one of many ways to make code more DRY. Above, we see that the `User` and `Platform` classes are minimal and only use the provided members in the base `Entity` class, while `Account` adds one additional member and method. Changing a method's implementation or adding a new common member now happens in one place instead of having to repeat the change in several places. DRY is looking pretty good for maintaining production code.

Let's look at some example code to see why DRY might not be so spry. Using the same classes above, let's suppose that we'd like to document how these classes work. Let's start by writing out some examples of how we might use these classes with the Josh Labs service:

```python
// The User Service
from joshlabs import JoshLabsAPI
from joshlabs.entities import User

jl_instance = JoshLabsAPI()
jl_instance.start_session('secret','credentials')

new_user = User('Alice')
jl_instance.add_user(new_account)

jl.end_session()
```

```python
// The Account Service
from joshlabs import JoshLabsAPI
from joshlabs.entities import Account

jl_instance = JoshLabsAPI()
jl_instance.start_session('secret','credentials')

new_account = Account('Bob Industries')
new_account.set_account_number('BI123')
js_instance.add_account(new_account)

jl_instance.end_session()
```

```python
// The Platform Service
from joshlabs import JoshLabsAPI
from joshlabs.entities import Platform

jl_instance = JoshLabsAPI()
jl_instance.start_session('secret','credentials')

new_platform = Platform('UNIX')
js_instance.add_platform(new_platform)

jl_instance.end_session()
```

These examples each look good, and contain complete and pertinent information to use each class and service. Each code example could be placed independent of each other one on different pages of documentation, for example. Following DRY, there is a temptation to split this up into two sets of code samples, one showing the initialization of the service and each entity

```python
from joshlabs import JoshLabsAPI

jl_instance = JoshLabsAPI()
jl_instance.start_session('secret','credentials')
```

and then three sets of specific usages, one for each service

```python
from joshlabs.entities import User

new_user = User('Alice')
jl_instance.add_user(new_account)

jl.end_session()
```

```python
from joshlabs.entities import Account

new_account = Account('Bob Industries')
new_account.set_account_number('BI123')
js_instance.add_account(new_account)

jl_instance.end_session()
```

```python
from joshlabs.entities import Platform

new_platform = Platform('UNIX')
js_instance.add_platform(new_platform)

jl_instance.end_session()
```

Reorganizing the example code like this has actually made things worse. Now, there's a cognitive dependency on each of these snippets. The reader needs to see the initialization code for the rest of the entity code examples to make sense. The entity code examples also can't be executed on their own since they're missing some import and initialization statements. Ultimately this means that these code examples cannot be moved around independently without some reference to the initialization code. Remember that reading code is different than writing code, and applying DRY to these examples shows some reasons why.

If the WET (which is the opposite of DRY) code example above would need to be broken up for documentation or some other organizational reason, repeating code would actually be more helpful in this case. The WET code samples could even be placed in the same page without any real loss of understanding. 

This may seems like a straightforward case of not using the DRY principle in example code but there are others. The key is remember that reading code in a particular context can greatly help with understanding what that code is doing and how it works. Approaches that help increase efficiency for production code may hamper usability for example code. Keep this in mind when thinking about DRYing off some code for documentation.