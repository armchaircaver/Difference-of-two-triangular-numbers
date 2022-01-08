# Difference-of-two-triangular-numbers
Python module to create pairs of positive integers whose triangular number differences are a given number

Creates indices of pairs of triangular numbers whose difference make a specified number.

i.e.  given n, constructs pairs of positive integers (p,q) where p*(p+1)//2 - q*(q+1)//2 = n

The module requies an external function, divisors, that returns all the divisors of a given number.
Two options for this are included in the source code, obtaining divisors from the module enigma.py (available from 
http://www.magwag.plus.com/jim/enigma.html ) or from my own factorisation library, factors, (available in my github, https://github.com/armchaircaver/Factors)
