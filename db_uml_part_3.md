This is the third post in a series on how Joshi's Pizzeria is managing its orders using a database. In the [first post](), a basic domain model is created relating some entities of interest. In the [second post](), the relationship between orders and pizzas is made more concrete.

This post explores the relationship between pizzas and toppings in terms of the domain model which will eventually be used in a database. The relationship between pizzas and toppings is a many-to-many relationship, meaning that a given pizza may have many toppings associated with it and a given topping may be associated with many pizzas. Following the same approach of writing sample basic tables for pizzas and toppings, here is a what a pizza table may look like:

<!--- image here --->

and here is one idea of what a topping table may look like: 

<!--- image here --->

There is a slight problem with these tables. How is a given pizza associated with its toppings and vice versa? Looking at the pizzas table, one approach would be to give each pizza a list of toppings as part of its table. It could look like this: 

<!--- list approach image ---> 

This doesn't really work since lists can be of varying sizes. If a topping is updated in some way, each list in the pizza table would also have to be updated. As well, lists would need to be variable in size since a given pizza may have some subset of toppings. This could lead to a table relationship that is difficult to manage. 

Another approach is to add columns that represent each topping individually: 

<!--- column approach strategy --->

This is also problematic. Columns need to be specified upfront which could lead to a large number of possible topping columns. Most pizzas will likely not need every single topping column so there's a lot of unnecessary space here. As well if columns need to be added, removed or renamed this creates a lot of overhead. This approach seems to be worse than the previous approach. 

Both approaches suffer from the same problem: it's difficult to track a variable number of unique keys in a table. In fact, most databases [don't support many-to-many relationships](http://www.tomjewett.com/dbdesign/dbdesign.php?page=manymany.php). 