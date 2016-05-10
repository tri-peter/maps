# -*- coding: utf-8 -*-

""" Numerical Solutions and Bifurcation Diagrams
    of the Logistic and Henon Maps

    This module calculates and plots iterations and bifurcation diagrams
    for the Logistic and Henon iterated maps.

    Copyright 2016 Tri-Peter Shrive

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Tri-Peter Shrive
    Anklamer Str 13
    10115 Berlin
    Deutschland

    +49 17 62087558
    Tri.Shrive@gmail.com

"""

import argparse
import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np
import os
import sys

global_xtemp = 0.3
global_ytemp = 0.3

def logistic_map(r):
	"""function for iterating and plotting the logistic map"""

	xtemp = global_xtemp

	x = [xtemp]

	for t in range(1,400):
		xtemp = logistic_function(r, xtemp)
		x.append( xtemp )

	fig = plt.figure()
	fig.canvas.set_window_title('Numerical Solutions and Bifurcation Diagrams')
	fig.suptitle('Logistic Map', fontsize=14, fontweight='bold')
	ax = fig.add_subplot(111)
	ax.set_title('x[n] = r * x[n-1] * (1 - x[n-1])')
	ax.set_xlabel('n')
	ax.set_ylabel('Xn')

	plt.plot(x, 'r.', markersize = 2.99)
	plt.show()

	return

def henon_map(a):
	"""function for iterating and plotting the henon map"""

	xtemp = golbal_xtemp
	ytemp = global_ytemp

	x = [xtemp]
	y = [ytemp]

	for t in range(1,400):
		xtemp, ytemp = henon_function(a,xtemp,ytemp)
		x.append( xtemp )
		y.append( ytemp )

	fig = plt.figure()
	fig.canvas.set_window_title('Numerical Solutions and Bifurcation Diagrams')
	fig.suptitle('Henon Map', fontsize=14, fontweight='bold')
	ax = fig.add_subplot(111)
	ax.set_title('x[n] = 1 - a * x[n-1]^2 + y[n-1], y[n] = 0.3 * x[n-1]')
	ax.set_xlabel('n')
	ax.set_ylabel('Xn')

	plt.plot(x, 'r.', markersize = 2.99)
	plt.show()

	return
	
def logistic_worker(r):
	"""worker function for calculating the tragectories of the logistic map"""

	xtemp = golbal_xtemp

	x = [xtemp]

	for t in range(1,400):
		xtemp = logistic_function(r, xtemp)
		x.append( xtemp )

	return x[-20:]
	
def logistic_function(r, x):
	return r * x * (1 - x)

def henon_worker(a):
	"""worker function for calculating the tragectories of the henon map"""

	xtemp = golbal_xtemp
	ytemp = global_ytemp

	x = [xtemp]
	y = [ytemp]

	for t in range(1,400):
		xtemp, ytemp = henon_function(a,xtemp,ytemp)
		x.append( xtemp )
		y.append( ytemp )

	return x[-20:]

def henon_function(a, x, y):
	return 1 - a * x**2 + y, 0.3 * x

def quality():
	if args.logistic == False and args.henon == False:
		print("error: one and only one of the arguments -L/--logistic: or -H/--henon: must be selected")
		sys.exit()

	if args.logistic and args.henon:
		print("error: argument -L/--logistic: not allowed with argument -H/--henon")
		sys.exit()

	if args.iteration == False and args.bifurcation == False:
		print("error: either one or both arguments -I/--iteration: and -B/--bifurcation: must be selected")
		sys.exit()

if __name__ == '__main__':

	from argparse import RawTextHelpFormatter
	parser = argparse.ArgumentParser(description='Calculation and plotting of iterations and bifurcation diagrams for the Logistic and Henon iterated maps.', epilog='If both arguments -I/--iteration: and -B/--bifurcation: are selected close the first window to view next plot. \n\n EXAMPLES \n Iterate Logistic map with r = 2.5 and plot bifucation diagram: \n %(prog)s -LIB 2.5 \n\n Iterate Henon map with a = 1.3: \n %(prog)s -HI 1.3 \n\n Plot bifurcation diagram for Henon map. The constant is trivial yet essential: \n %(prog)s -HB 1.3 \n', formatter_class=RawTextHelpFormatter)

	parser.add_argument("float", type=float, help="determine the constant 'r' or 'a' respectively")

	parser.add_argument("-L", "--logistic", help="use the Logistic Function (WARNING: incompatable with the -H/--henon: argument)", action='store_true')
	parser.add_argument("-H", "--henon", help="use the Henon Function (WARNING: incompatable with the -L/--logistic: argument)", action='store_true')
	parser.add_argument("-I", "--iteration", help="plot an iteration of the Map using the given constant", action='store_true')
	parser.add_argument("-B", "--bifurcation", help="plot the Map's Bifurcation", action='store_true')

	args = parser.parse_args()

	quality()
	
	a, b, c = 0, 4, 0.0001
	logistic_range = np.arange(a, b, c)

	d, e, f = 0, 1.4, 0.0001
	henon_range = np.arange(d, e, f)


	if args.iteration:
		if args.logistic:
			logistic_map(args.float)

		if args.henon:
			henon_map(args.float)


#	if args.iteration:
#		if args.logistic:
#			if 2.4 <= round(args.float,2) <= 4:
#				logistic_map(args.float)
#			else:
#				print("The constant 'r' must be greater or equal to 2.4 and less than or equal to 4")
#
#		if args.henon:
#			if 1 <= round(args.float,2) <= 1.4:
#				henon_map(args.float)
#			else:
#				print("The constant 'a' must be greater or equal to 1 and less than or equal to 1.4")

	if args.bifurcation:
		print("Running...")
		if args.logistic:
			with mp.Pool(processes=mp.cpu_count()) as pool:
				T = pool.map(logistic_worker, np.arange(a, b, c))

			fig = plt.figure()
			fig.canvas.set_window_title('Numerical Solutions and Bifurcation Diagrams')
			fig.suptitle('Logistic Bifurcation', fontsize=14, fontweight='bold')
			ax = fig.add_subplot(111)
			ax.set_title('x[n] = r * x[n-1] * (1 - x[n-1])')
			ax.set_xlabel('r')
			ax.set_ylabel('Trajectories')

			plt.plot(np.arange(a, b, c), T, 'r.', markersize = 0.65)
			plt.xlim([a,b])
			plt.show()

		if args.henon:
			with mp.Pool(processes=mp.cpu_count()) as pool:
				T = pool.map(henon_worker, np.arange(d, e, f))

			fig = plt.figure()
			fig.canvas.set_window_title('Numerical Solutions and Bifurcation Diagrams')			
			fig.suptitle('Henon Bifurcation', fontsize=14, fontweight='bold')
			ax = fig.add_subplot(111)
			ax.set_title('x[n] = 1 - a * x[n-1]^2 + y[n-1], y[n] = 0.3 * x[n-1]')
			ax.set_xlabel('a')
			ax.set_ylabel('Trajectories')

			plt.plot(np.arange(d, e, f), T, 'r.', markersize = 0.65)
			plt.xlim([d,e])
			plt.show()

