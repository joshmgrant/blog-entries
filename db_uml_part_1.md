Joshi's Pizzeria is doing pretty well. Early on, the owners doubled down on creating delicious pizzas and nothing else. They've been selling pizzas like hotcakes. However, as the market changes, Joshi's wants to keep track of their pizza orders in some kind of database. Partially this is to help improve service, partially this to satisfy one of the owner's need to better himself as a developer. 

What' the best way to start creating such a database? 

One way to look at modeling the domain problem, which can be restated as: 
> How can we represent pizza orders to keep track of ingredients that being used?

One approach is to use [domain modeling](http://csis.pace.edu/~marchese/CS389/L8/DomainModel-UML_short.pdf). This is an approach that can be used to model relationships between entities with the eventual goal of establishing a database structure (called a schema) to represent data. The general approach here is to look at _nouns_ (a person, place, or thing) and then look at the relationships between these nouns. Modeling in this way helps see how different data relates to other data. 

In the original problem, there are three nouns that can be identified:

- _Orders_ 
- _Pizzas_
- _Ingredients_

How do these things relate? 

Each order has one or more pizzas. Since Joshi's only makes pizzas for the time being, it's definitely the case that a given order has at least one pizza in it.

As well, each individual pizza is belongs to one order only. Even if two pizzas are made with identical ingredients they are still unique pizzas that should be tracked separately. 

As well, each pizza contains one or more ingredients. One of Joshi's secrets is a fantastic thin crust that is used on every pizza. As this is the same for each pizza created, crusts can be ignored in this model for the time being and consider toppings. Each pizza contains some toppings such as marinara sauce, cheese and blueberries (among other possible ones). Based on this, let's change the terminology from _Ingredients_ to _Toppings_ to reflect the model better.

Lastly, each topping could be found on several pizzas, or none at all. 

Based on this description, let's see what this looks in a diagram:

![first approach](https://drive.google.com/open?id=0B37cQz-ao056WFUzT29Sd0prYjg)

The basic idea of this diagram is to represent the previous relationships. Every order can have one or more pizzas but each pizza can belong to only one order. As well, each pizza can contain one or more toppings and each topping can be found on one or more pizzas. In relational database lingo, the relationship between orders and pizzas is _one-to-many_ and the relationship between pizzas and toppings is _many-to-many_. 

Using common notations, the diagram formally now looks like this:

![first approach with relationships](https://drive.google.com/open?id=0B37cQz-ao056aUJrdHhTZ2FyVjQ)

This is a first draft of the design of a database tracking pizza orders for Joshi's. 