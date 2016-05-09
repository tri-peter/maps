maps20160430.py

Originator: Tri-Peter Shrive
Contact: tri.shrive@gmail.com
Created: 2016_04_30

Recomended operating system: GNU-Linux. Run in command line with python3.

usage: python3 maps20160430.py [-h] [-L] [-H] [-I] [-B] float

Calculation and plotting of iterations and bifurcation diagrams for the Logistic and Henon iterated maps.

positional arguments:
  float              determine the constant 'r' or 'a' respectively

optional arguments:
  -h, --help         show this help message and exit
  -L, --logistic     use the Logistic Function (WARNING: incompatable with the -H/--henon: argument)
  -H, --henon        use the Henon Function (WARNING: incompatable with the -L/--logistic: argument)
  -I, --iteration    plot an iteration of the Map using the given constant
  -B, --bifurcation  plot the Map's Bifurcation

If both arguments -I/--iteration: and -B/--bifurcation: are selected close the first window to view next plot. 

 EXAMPLES 
 Iterate Logistic map with r = 2.5 and plot bifucation diagram: 
 maps20160430.py -LIB 2.5 

 Iterate Henon map with a = 1.3: 
 maps20160430.py -HI 1.3 

 Plot bifurcation diagram for Henon map. The constant is trivial yet essential: 
 maps20160430.py -HB 1.3 


