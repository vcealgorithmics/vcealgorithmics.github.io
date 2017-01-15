# This page still under construction

Recursion occurs when something is self refferential; that is, it calls itself.


## Examples of recursion

### Maths

If you've studied sequences and series (VCE Specialist Mathematics)...

A particularly famous recurrance relation is the fibbonaci sequence, which follows the simple form of 

> Start at 1

> take the last two numbers and add them to get the next number
> do the next step in the fibbonachi sequence

### Geometry

A particularly interesting form of recursion exists in fractals, geometric shapes that repeat over and over again.

serpinski triangle

other

If you've ever pointed two mirrors at each other, and seen the mirror reflecting itself infinitely, you've seen this form of recursion at play.

## Programming

By now, you should have learnt about functions. Recursion in programming languages is very simple, a function simply calls itself inside it's own contents.

For example :

> def fib:
blah

## Recursion vs Iteration

By now you might be wondering what the point of recursion is when you can simply use iteration (and in fact, all recursion can be converted into iteration, and vice versa. This is known as [tail recursion](tailrecursion)). 

The answer is that recursion provides a neater, more coherent way of looping in many cases, particularly for algorithmis that deal with subproblems such as divide and conquer.

more code examples