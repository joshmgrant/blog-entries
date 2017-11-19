In the previous post, we saw how Josh's Pizzeria was working to [solve the problem of how they keep track of their pizza inventory](http://simplythetest.tumblr.com/post/158938334610/database-design-and-modelling-using-pizzas). Now that there's a model of how pizza orders are structured, it can be used to implement the actual database. 

As seen previously, there are three entities: orders, pizzas and toppings. Orders and pizzas have a [one-to-many](https://en.wikipedia.org/wiki/One-to-many_(data_model)) relationship and pizzas and toppings have a [many-to-many](https://en.wikipedia.org/wiki/Many-to-many_(data_model)) relationship. What can we do with such relationships in place? This post will explore the pizza and orders relationship.

For orders and pizzas, having a one-to-many relationship means that each pizza in the database includes a reference to a single, unique order. Since orders are distinct, the table for orders can look something like this:

<!---Insert image here--->

and the table for pizzas could then look something like this:

<!---Insert image here--->

Since each order id is unique, the order id can be set to be the (_primary key_)[https://www.w3schools.com/sql/sql_primarykey.asp] for the the orders table. This means that each order in the table can be uniquely identified by its primary key value. 

In turn, each pizza belongs to a particular (unique) order so we can use the order's primary key in the pizza table. When a primary key is used in another table to associate two tables, it is called a (_foreign key_)[https://en.wikipedia.org/wiki/Foreign_key]. In this case, the foreign key in the pizza table says which order the pizza belongs to. Note that the order table contains no direct reference to the pizza table here; it's enough to define a primary key for the orders table and use that reference in the pizza table. This will help when we create a SQL database of the orders and pizzas. 

Next up, the relationship between pizzas and toppings will be explored.
