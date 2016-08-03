Tutorials on inheritance in Object-Oriented Programming (OOP) are a dime a dozen on the internet. Many of them have a top-down flavour. The concept of inheritance is introduced then shoe-horned onto some code example. One classic example goes like this: 

- Declare a base class `Vehicle`
- Declare two subclasses of `Car` and `Bicycle`
- Illustrate how these subclasses can reuse methods from the base class. 

This makes for easy tutorial writing but doesn't really illustrate _good_ code reuse. So I'm going to try a bottom-up example. 

Suppose you're writing some transportation-based app and you write a `Car` class. The class (in pseudocode) might look like this: 

<pre><code>
class Car {

    

    // constructor
    public Circle(double r) {
        radius = r;
    }

    public double getArea() {
        return 3.1415*radius*radius;
    }

    public getCircumference() {
        return 2*3.1415*radius;
    }

}
</code></pre>

So far, so good. A little while later - think days later - you need a rectangle object, so you write a class for a rectangle, which may look like this  