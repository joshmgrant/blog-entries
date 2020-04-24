In the next installment of my series on [how to write example code](https://simplythetest.tumblr.com/post/612302779439087616/writing-example-code-a-series), I'm going to discuss the concept of YAGNI, and why in example code it turns out you ain't gonna need YAGNI. 

In my previous articles, I discussed [keeping your audience in mind](https://simplythetest.tumblr.com/post/612751899042742272/writing-example-code-knowing-your-audience-or) and the [Copy/Paste Conundrum](https://simplythetest.tumblr.com/post/613040287641681920/writing-example-code-the-copypaste-conundrum). I planned on having this post pretty soon after the last one, but then a deadly pandemic broke out, so I had to put my thoughts on writing example code on the shelf for a bit. It took a minute, but now I'm ready to talk about the next consideration, needing YAGNI - or not. 

In software development, the [concept of YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) comes out of extreme programming. YAGNI stands for "You aren't going to need it", or more colloquially, "You ain't gonna need it". The principle when applied to software development is straightforward: don't build or add in code or features until you actually need them. Trying to guess what features are needed in a piece of code in the future is difficult to do well. Instead, write code that you _know_ is required now and leave future work until the future. You can think of YAGNI as a way to avoid premature optimization since any code that is written is code that needs to be maintained in the future. (Martin Fowler has an [excellent article](https://martinfowler.com/bliki/Yagni.html) on the greater concept of YAGNI in software.)

Generally speaking, this is a good approach to writing code. Keep code as simple as possible, and only write the code you absolutely need to keep maintenance costs down. For example code, I think we don't need YAGNI, mainly because example code is trying to _show_ how code works, instead of actually _being_ working code. Keeping this in mind is particularly helpful for reading example code and learning from it.

Let's go back to the Josh Labs service library. Here's a sample of code showing some functionality:

```python
from joshlabs import JoshLabsAPI
import requests

jl_instance = JoshLabsAPI(password='mySuperSecretPassword1')

base_url = jl_instance.JOSH_LABS_BASE_URL
status = requests.get(baseurl + "/status")

user_name = jl_instance.get_user_name()
print("User name is {}".format(user_name))

user_account_type = js_instance.get_user_account_type()
print("User account is {}".format(user_account_type))

jl_instance.close_session()
```

This piece of example code shows a few basic operations of the Josh Labs API library. Reading this piece of code does show in a simple flow how some operations are executed. From a maintenance perspective, there's some lines that YAGNI applies to. The print statements don't add anything functionally to the code and might even lead to problems if the methods change data types - or in the case of Python, the print syntax itself changes. Further, the `status` variable doesn't even seem to be used in any meaningful way and those two lines of code could be removed without any real change to the functionality.

On the other hand, thinking about this code from a _reading_ perspective I think this is good example code. Reading the code top to bottom provides some insight into how this API library works and how the API operations are structured. Patterns emerge based on multiple methods in this example. Of course the example could be broken up into multiple snippets which might be helpful in some cases. Often, readers looking for examples want something more "complete" where at least patterns of usage can be determined. Seeing how to retrieve status, user names and user information might be exactly the combination of features some users want to see. Here we're trying to balance copy/paste considerations while being clear and concise. I think the example code above balances these considerations nicely.

Once such example code is copy/pasted into some production destination then naturally principles like YAGNI come into play. But reading code is not writing code is not executing code, so different considerations for each of these contexts are important. Adding a bit of "extra" functionality or lines of code to make for a more complete picture of what a piece of code is doing is preferable in example code over trying to be as concise as possible. People learn in different ways and human brains love finding patterns. Keeping these elements in mind when writing example code helps a lot for producing a good reading experience.

Whether or not you decide you ain't gonna need some pieces of your example code, remember you ain't gonna need YAGNI when it comes to your code samples.
