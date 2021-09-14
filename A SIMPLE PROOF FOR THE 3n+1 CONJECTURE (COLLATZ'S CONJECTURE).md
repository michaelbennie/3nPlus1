# A SIMPLE PROOF FOR THE 3n+1 CONJECTURE (COLLATZ'S CONJECTURE)

# 

## Introduction:

Collatz's Conjecture was first popularized by German mathematician Lothar Collatz in 1937 and is defined as follows: "start with any [positive integer](https://en.wikipedia.org/wiki/Positive_integer "Positive integer") n. Then each term is obtained from the previous term as follows: if the previous term is [even](https://en.wikipedia.org/wiki/Parity_(mathematics) "Parity (mathematics)"),
 the next term is one half of the previous term. If the previous term is
 odd, the next term is 3 times the previous term plus 1. The conjecture 
is that no matter what value of n, the sequence will always reach 1."([Collatz conjecture - Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture))

In this paper, we offer a  proof for the numbers of loops within the 3n+1 function is 1 and contains the values [1,2,4]. We first generalize the functions to loops of any n number and show that for each loop permutation there is only one one number that satifies the equation. We then show the possible permutations and derive that the only numbers that form a loop are [1,2,4].

## Definitions:

The general equation:

$$
n ∈N, f(n) =\begin{cases} \frac{n}{2}  & n  \equiv  0 (mod 2)\\ 3n+1 & n  \equiv  1 (mod 2)\end{cases} 
$$

Reformatted into more concise text:

For this proof i will be using o and e as shorthand for the odd and even functions. 

We assume n is the number that fulfills a cycle.

$$
e=e(n)=\frac{n}{2}
$$

$$
o=o(n)= 3n+1
$$

$$
f(n) =\begin{cases} o  & n  \equiv  0 (mod 2)\\ e & n  \equiv  1 (mod 2)\end{cases} 
$$

If multiple o's and e's are stringed together, this would be shorthand for the iterated composition of those functions starting from right to left.

$$
Ex: oee = 3(\frac{1}{2}(\frac{n}{2}))+1=\frac{3n}{4}+1
$$

We define a pattern looping if a repeated function applied to the number returns the same number.

$$
f(a0) = a1, f(a1) = a2, ..., and f(aq) = a0
$$

Let, g(n)= arbitrary sequence of o and e functions.

Define E as the number of e's in g(n) and O as the number of o's in g(n).

### Lemma 0.1:

To demonstrate that a sequence of o's and e's will be a looping sequence if it equals n.

$$
Assume:g(n) = ...eoee = n, 
$$

$$
g(n)=...e(o(e(e(n)))), \text{deftiniton of o and e}
$$

$$
...e(o(e(e(n)))) = e(n)= n1,e(n1)= n2,o(n2)= n3,e(n3)....,  \text{deftinition of an iterated function}
$$

$$
e(n)= n1,e(n1)= n2,o(n2)= n3,e(n3).... = n, \text{deftinition of g(n)}
$$

$$
\text{so }e(n)= n1,e(n1)= n2,o(n2)= n3,e(n3).... = n \text{ is a looping pattern by deftinition}
$$

$$
\text{so, } g(n) = e(n)= n1,e(n1)= n2,o(n2)= n3,e(n3) .... = n \text{ is a looping pattern}
$$

Therefore, an arbitrary sequence of o's and e's, g(n), will be a looping sequence if it equals n.

### Lemma 0.2:

To demonstrate that the highest degree for a sequence of o's and e's is 1.

We assume n is the number that fulfills a cycle.

The starting degree is n which is 1.

$$
e=e(n)=\frac{n}{2}, deftinition 
$$

$$
o=o(n)= 3n+1, deftiniton

$$

$$
n = n^1 \text{, identity property of exponents}
$$

$$
\text{The degree of } n^1 \text{ is 1 by deftinition}
$$

$$
\text{By deftinition the degree of a term is the sumation of the degrees of each variable in the term}
$$

$$
Case 1: e(n) = \frac{1}{2}*n:
$$

$$
\frac{1}{2} \text{ has degree 0},
$$

$$
\text{n has degree 1 ,} 1+0=1
$$

No matter the inputted n, the degree will not change for e.

$$
Case 2: o(n) = 3*n+1:
$$

$$
3,1 \text{ both have degree 0},
$$

$$
\text{n has degree 1 ,} 1+0=1> 0(from 1)
$$

No matter the inputted n, the degree will not change for o.

Because e's and o's don't change the degree of a function, a sequence of them would not change the degree.

Therefore the starting degree (1) will not change.

The degree of the function will stay as 1 no matter the amount of o's and e's.

### Definitions Pt.2:

Since g(n) =n is a singe variable function with degree 1, it can be generalized to the form 

p=qn. p,q∈N.

### Lemma 1.1:

To demonstrate the solution to g(n) is p/q.

$$
g(n)=n
$$

$$
⇒p=qn,deftinition
$$

$$
\frac{p}{q}=n
$$

### Lemma 1.2:

To demonstrate an equation for q.

Let c be an arbitrary constant within the integers that starts at 0.

v is the rational number that represents the coefficient of n on the left side of the function.

$$
g(n) =n,
$$

$$
\text{if next function in composition is o:}
$$

$$
o(vn+c)= 3(vn+c)+1,
$$

$$
o(vn+c)=3vn+3c+1,
$$

$$
o(vn+c)=3vn+c,
$$

$$
o(vn+c)=3vn+3c,
$$

$$
o(vn+c)=3(vn+c)
$$

If we have O many o's:

$$
t=o_{0}( o_{2}( o_{3}( o_{4}(... o_{O}(n))))) = 3_{0}( 3_{2}( 3_{3}( 3_{4}(... 3_{O}(n))))) 
$$

For multiplying by 3 O many times:

$$
3^O\text{ is the formula for the coefficent on the left side from th enumber of o's, deftinition of exponent }
$$

$$
t=3^O
$$

$$
\text{if next function in composition is e:}
$$

$$
o(vn+c)= (vn+c)/2,
$$

$$
o(vn+c)=\frac{1}{2}(vn+c),
$$

If we have E many e's:

$$
b=e_{0}( e_{2}( o_{3}( e_{4}(... e_{E}(n))))) = \frac{1}{2}_{0}( \frac{1}{2}_{2}( \frac{1}{2}_{3}( \frac{1}{2}_{4}(... \frac{1}{2}_{E}(n))))) 
$$

For multiplying by 1/2 E many times:

$$
(\frac{1}{2})^E\text{ is the formula for the coefficent on the left side from the number of e's, deftinition of exponent }
$$

$$
b=(\frac{1}{2})^E
$$

$$
\frac{1}{b}=(\frac{1}{\frac{1}{2}^E})
$$

$$
\frac{1}{b}=(2^E)
$$

$$
p=qn
$$

$$
(q-1)n+p=n
$$

$$
(q-1)n+c=n
$$

$$
(t*b)n+c=n
$$

$$
t*n+\frac{c}{b}=\frac{n}{b}
$$

$$
c= \frac{n}{b}-t*n
$$

$$
c= (\frac{1}{b}-t)*n
$$

$$
(\frac{1}{b}-t) = q, deftinition
$$

$$
2^E-3^O=q
$$

### Lemma 1.3:

To show that q =1 for all unique answers.

Define p' as the coprime factor between p and q 

$$
\frac{p}{q}=n, deftinition
$$

$$
n∈N, deftinition
$$

$$
therefore,\frac{p}{q}∈N
$$

$$
\text{if p has q as a factor then, it can be simplefied to an integer}
$$

$$
p=p'*q,
$$

$$
\frac{p}{q}=\frac{p'*q}{q},
$$

$$
\frac{p}{q}= \frac{p'}{1},
$$

$$
\text{Therefore, any answer for n can be simplified to q=1 and p=p}'
$$

## Proof:

Note: E and O can't be less than one since they count how many e's and o's and there cant be a negative ammount of e's and o's.

$$
q =2^E-3^O, (1.2)
$$

$$
E >1↑ O>1, Catalan's Conjecture
$$

### Cases:

Cases E <=1&& O<=1:

$$
2^0-3^0=0
$$

$$
2^1-3^0=1
$$

$$
2^0-3^1=-2
$$

$$
2^1-3^1=-1
$$

Only case E=1, O= 0 works.

Cases E >1&& O<=1:

$$
\text{If O = 0:}
$$

$$
2^E-3^0=1
$$

$$
2^E=2
$$

$$
E=1
$$

$$
\text{If O = 1:}
$$

$$
2^E-3^1=1
$$

$$
2^E=4
$$

$$
E=2
$$

Only case E=2, O=1

Cases E <=1&& O>1:

$$
\text{If E = 0:}
$$

$$
2^0-3^O=1
$$

$$
3^O=0
$$

$$
O= \text{no solutions}
$$

$$
\text{If E = 1:}
$$

$$
2^1-3^O=1
$$

$$
3^O=-1
$$

$$
O = \text{no solutions}
$$

### Permutations:

$$
(E,O)∈[(1,0)(2,1)]
$$

Permutations of (1,0):

[e]

Permutations of (2,1):

[eeo,eoe,oee]

### Converting to Numbers:

#### Case e:

$$
n/2=n
$$

$$
0=n
$$

$$
p=0,q=1
$$

$$
p/q = 0
$$

$$
\text{0 is not in the set of natural numbers so it can be ignored}
$$

#### Case eeo:

$$
1/2*(1/2*(3n+1))=n
$$

$$
1=n
$$

$$
p=1, q=1
$$

$$
p/q=1
$$

1 is a solution

#### Case eoe:

$$
1/2*(3(1/2*n)+1)=n
$$

$$
2=n
$$

$$
p=2, q=1
$$

$$
p/q=2
$$

2 is a solution

#### Case oee:

$$
3(1/2*(1/2*n))+1=n
$$

$$
4=n
$$

$$
p=4, q=1
$$

$$
p/q=4
$$

4 is a solution



$$
solutions∈[1,2,4]
$$

$$
\text{Therefore the 1,2,4 loop is the only loop}
$$
