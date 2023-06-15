As I continue showing some [awesome parts](https://simplythetest.tumblr.com/post/188858906385/pytest-the-awesome-parts) of Pytest, I'd like to focus a little bit on one feature that is an oldie but a goodie: fixtures.

Fixtures are an [interesting and often confusing topic](https://docs.pytest.org/en/latest/fixture.html) to new Pytest users. At first they seem counter-intuitive or even wrong, but after you get a feel for how they work fixtures are indispensible to writing good Pytest code. 

Let's start at the beginning. What is a fixture? A fixture is a function that has logic that is applied to a specific context. As an example, suppose we want to test a [random number generator](https://www.johndcook.com/blog/2010/12/06/how-to-test-a-random-number-generator-2/) library that we created, called `Rando`. We can use fixtures to test an instance of this object like this:

```python
@pytest.fixture
def rando():
    return Rando(0,1)

def test_upper_range(rando):
    val = rando.value()

    assert val < 1

def test_lower_range(rando):
    val = rando.value()

    assert val > 0
```

Here the fixture returns a `Rando` instance called `rando` that can be passed into functions. Each function gets its own independent instance of `rando` that can be used in the function body logic. This seems pretty straightforward from a syntactic perspective, but there's some interesting things going on. 

One, we're not using object oriented programming in our test code. The two test functions above don't require being members of a class. The fixture is reusable between these two functions without having to hold state between the tests. 

As a pseudocode example using an object oriented approach, here's a similar example:

```java
class TestRando(){

    private Rando rando;

    private setUp() { this.rando = new Rando(0,1); }

    @Test
    private testUpperRange() {
        double val = rando.value()

        assert val < 1
    }

    @Test
    private testLowerRange() {
        double val = rando.value()

        assert val > 0
    }
}
```

This is a more traditional approach, which would still work in Python with classes as well. The surprisingly beautiful part is that _OOP is not required_ for working with Pytest. And it turns out, it's better not to use OOP when working with Pytest.

To see why, let' see another cool aspect of using fixtures: that fixtures can use fixtures.

Suppose in the above random number generator example a `RandoSeed` can be created and passed into a `Rando` instance. If we want to both test the seed and make use of the seed, we could come up with fixtures like this:

```python
@pytest.fixture
def seed():
    return RandoSeed(0)

@pytest.fixture
def seeded(seed):
    return Rando(0,1, seed=seed)

@pytest.fixture
def unseeded():
    return Rando(0,1)

def test_seeded_value(seeded):
    actual = rando.val()
    expected = SEEDED_VAL

    assert actual == expected

def test_upper_range(unseeded):
    val = rando.value()

    assert val < 1

def test_lower_range(unseeded):
    val = rando.value()

    assert val > 0
```

(Don't worry if you aren't familiar with random number generation. The point is test approach, not the specific properties being tested. Random number generation is a [tough problem](https://en.wikipedia.org/wiki/Random_number_generator_attack).)

In the above code, using a seed fixture is cleanly separated from a random number generator instance. Both can be used independently in tests or in fixtures. There's no need to separate these test functions into different classes or try to order setup or teardown functionality in some way. Everything works as expected. Tests can be added, removed or refactored individually and as needed without rejigging class structures.  

These examples really are just the beginning when it comes to using fixtures well in Python, but they do provide a taste of how fixtures work and what kinds of problems they solve. Life is good with Pytest Fixtures!