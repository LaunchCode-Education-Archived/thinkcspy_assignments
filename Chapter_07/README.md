# Weekly Graded Assignment Instructions

Write a function, ``is_prime``, that takes a single integer argument and returns ``True`` when the argument is a prime number and ``False`` otherwise.

As a refresher, a prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

For example:

* 2 is prime
* 3 is prime
* 4 is not prime because is is divisible by 2
* 5 is prime
* 6 is not prime because it is divisible by 2 and 3
* 7 is prime
* 8 is not prime because it is divisible by 2 and 4
* 9 is not prime because it is divisible by 3

Also remember that you can use the modulo operator (%) to check whether one number is divisible by another.

For example, here are a bunch of modulo operations on 12:

* 12 % 2 is 0
* 12 % 3 is 0
* 12 % 4 is 0
* 12 % 5 is 2
* 12 % 6 is 0
* 12 % 7 is 5
* 12 % 8 is 4
* 12 % 9 is 3

Notice that 2, 3, 4, and 6, all the factors of 12, yield 0. This makes sense because modulo returns the remainder after division, and these numbers divide 12 perfectly, so there is no remainder left over.

Anyway, 12 is definitely not prime since it is divisible by a bunch of numbers: 2, 3, 4, and 6.