If you are a computer person, or just generally someone who likes to learn things about computers, a person I strongly suggest to follow is [Julia Evans](https://mastodon.social/@b0rk@jvns.ca/). She is a software professional who has made some wonderful zines on various UNIX/Linux utilities. 

One of her latest posts really struck a nice chord with me: explaining the [Diffie Hellman key exchange algorithm](https://mastodon.social/@b0rk@jvns.ca/116297199114287967). In a nutshell, this an algorithm for being able to pass a cryptographic key in an open space. And in a slightly larger nutshell, this kind of algorithm is important for public key cryptography methods, which are ways of encrypting or securing secret information in a way the is still public and can be done "openly", such as on a public website. This is why you can login to your banking online or email and not worry that some bad actor will easily login as well.

The part I love the most about this particular zine is when Julia talks about a function that takes two values and produces an outcome. Since the functions involved are [pretty complicated](https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_operations), she decides to use a ☺️ emoji to represent the operation. 

Honestly, I love everything about this.

First, using ☺️ as the operation makes clear this isn't a typical addition or multiplication. It's something a bit more abstract. 

Perhaps more importantly, using the ☺️ also suggests this is an operation that's _kind of like_ addition or multiplication. Instead of adding _x + y_, you compute _x ☺️ y_. Mathematically speaking, since elliptic curves with a well-defined point addition are groups, it's possible to think of this operation as form of addition, however a much more involved one. In a way, this abstracts the notion of adding two numbers into this more complex context.

(Lastly, this is just fun. Who doesn't like seeing ☺️?)

The main point though is that using an emoji to represent the operation helps abstract the notion of "addition" without getting lost in the details. In programming we may call this encapsulation, where the details of a method or function are hidden from a developer, and all they see is an interface or API. You may not even need to be aware of underlying details or functionality to use it. If a developer needs to use a cryptographic algorithm to secure some secret keys or credentials, they can do so without knowing the (possibly very complicated) details of how this works and instead implement the solution.

I've always enjoyed thinking abstractly, but it can be helpful too.