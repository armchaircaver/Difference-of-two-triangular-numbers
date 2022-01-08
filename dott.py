"""
Module to calculate indices of pairs of triangular numbers whose difference 
make a specified number.

i.e.  construct pairs of positive integers (p,q)
where p*(p+1)//2 - q*(q+1)//2 = n

Inspired by Enigma 914: Bridge too far
From New Scientist #2069, 15th February 1997 

"""
try:
  from enigma import divisors
except:
  from factors import all_factors as divisors


def dott(n):
  
  # isolate the powers of 2 that divide n
  t = 1
  nodd = n
  while nodd%2 == 0:
    nodd//=2
    t *= 2
  # n = t * nodd   , nodd is odd, t is a power of 2

  sols=set()
  for p in divisors(nodd):
    q = nodd//p

    #x-y = 2*t*p, x+y+1=q
    x = p*t +(q-1)//2
    y = (q-1)//2 - p*t
    if y > 0 :
      sols.add((x,y))
    
    #x-y = p, x+y+1=2*t*q
    x = q*t + (p-1)//2
    y = q*t - (p+1)//2
    if y > 0 :
      sols.add((x,y))
  return sols

if __name__=="__main__":

  # test using OEIS sequence A136107 (with entry for n=0 prepended)

  A136107 = [0, 0, 1, 1, 1, 2, 1, 2, 1, 3, 1, 2, 2, 2, 2, 3, 1, 2, 3, 2, 2, 3, 2, 2, 2, 3, 2, 4, 1, 2, 4, 2, 1, 4, 2, 4, 2, 2, 2, 4, 2, 2, 4, 2, 2, 5, 2, 2, 2, 3, 3, 4, 2, 2, 4, 3, 2, 4, 2, 2, 4, 2, 2, 6, 1, 4, 3, 2, 2, 4, 4, 2, 3, 2, 2, 6, 2, 4, 3, 2, 2, 5, 2, 2, 4, 4, 2, 4, 2, 2, 6, 3, 2, 4, 2, 4, 2, 2, 3, 6, 3, 2, 4, 2, 2, 7 ]
  for n in range(1,len(A136107)):
    sols = dott(n)
    for (x,y) in sols:
      assert (x*(x+1) - y*(y+1))//2 == n
    if ( len(sols) != A136107[n] ):
      print ("A136107 mismatch for n=",n,len(sols), A136107[n], sols )
      exit(1)
  print ("A136107 all match")
            

  

