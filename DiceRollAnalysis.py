#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from fractions import Fraction

# import our Random class from python/Random.py file
sys.path.append(".")
from Random2 import Random
seed = 5555
# main function for our DiceRollAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print
        sys.exit(1)

    H0 =sys.argv.index("-input0")
    H0 =sys.argv[H0+1]
    H1 =sys.argv.index("-input1")
    H1 =sys.argv[H1+1]


    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

#loads text and put text into an array for the LLR graph
random = Random(seed)
RollsH0 = np.loadtxt(H0)
RollsH1 = np.loadtxt(H1)
print(len(RollsH0),len(RollsH1))
a0 = []
a1 = []

prob1 = Fraction(1/10)
prob2 = Fraction(2/10)
prob3 = Fraction(1/10)
prob4 = Fraction(2/10)
prob5 = Fraction(1/10)
prob6 = Fraction(2/10)
total = prob1+prob2+prob3+prob4+prob5+prob6
prob1 = prob1 / total
prob2 = prob2 / total
prob3 = prob3 / total
prob4 = prob4 / total
prob5 = prob5 / total
prob6 = prob6 / total
print("prob1", prob1)
print("prob2", prob2)
print("prob3", prob3)
print("prob4", prob4)
print("prob5", prob5)
print("prob6", prob6)


               #have to manually change range to match Nexp. Not sure how to get it to change from command line
for j in range(0,100000):
    LLR0 = 0
    for l in range(0,10):
        if RollsH0[j][l] == 1:
           LLR0 = LLR0+math.log(prob1)
        elif RollsH0[j][l] == -1:
           LLR0 = LLR0+math.log(prob2)
        elif RollsH0[j][l] == 1:
           LLR0 = LLR0+math.log(prob3)
        elif RollsH0[j][l] == -1:
           LLR0 = LLR0+math.log(prob4)
        elif RollsH0[j][l] == 1:
           LLR0 = LLR0+math.log(prob5)
        elif RollsH0[j][l] == -1:
           LLR0 = LLR0+math.log(prob6)
        if RollsH0[j][l] == 1:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == -1:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 1:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == -1:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 1:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == -1:
           LLR0 = LLR0-math.log(1/6)
    a0.append(LLR0)

for j in range(0,100000):
    LLR1 = 0
    for l in range(0,10):
        if RollsH1[j][l] == 1:
           LLR1 = LLR1+math.log(prob1)
        elif RollsH1[j][l] == -1:
           LLR1 = LLR1+math.log(prob2)
        elif RollsH1[j][l] == 1:
           LLR1 = LLR1+math.log(prob3)
        elif RollsH1[j][l] == -1:
           LLR1 = LLR1+math.log(prob4)
        elif RollsH1[j][l] == 1:
           LLR1 = LLR1+math.log(prob5)
        elif RollsH1[j][l] == -1:
           LLR1 = LLR1+math.log(prob6)
        if RollsH1[j][l] == 1:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == -1:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 1:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == -1:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 1:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == -1:
           LLR1 = LLR1-math.log(1/6)
    a1.append(LLR1)

#flatten data files and sorts them for probability graph
RollH0 = RollsH0.flatten()
RollH1 = RollsH1.flatten()
RollH0.sort()
RollH1.sort()
a0.sort()
a1.sort()

#calculates the alpha of our experiment
Alpha = .05
a =len(a0)-int(len(a0)*Alpha)
print("Alpha", Alpha)
print("lambda", a0[a])

#calculate beta
count = float(0)
for x in range(0,len(a1)):
    if a1[x] < a0[a]:
        count += 1
        
beta = count/len(a1)
print("beta", beta)

#probability distribution graph
density0, bins0 =np.histogram(RollH0, density = True)
density1, bins1 =np.histogram(RollH1, density = True)
unity_density0 = density0 / density0.sum()
unity_density1 = density1 / density1.sum()

fig, ax = plt.subplots(figsize = (6,6))
widths = bins0[:-1] - bins0[1:]
ax.bar(bins0[1:], unity_density0, width=widths, color='blue', alpha = 1.0, align ='edge')
ax.bar(bins1[1:], unity_density1, width=widths, color='green', alpha = 0.75, align ='edge')

ax.set_xlim(-2,2)
ax.set_xlabel('Spin')
ax.set_ylabel('Probability')
ax.set_title('Probability distribution for spin 1, -1 or somthing else')
ax.legend(['Proton','something else'])

#LLR graph
plt.figure()
plt.hist(a0,20, alpha=.75, color='blue')
plt.hist(a1,20, alpha=.75, color='green')
plt.axvline(a0[a], color='red', label=['a = 0.5'])
plt.legend (['λ = 1.49','H0','H1'],loc = 'upper left' )
plt.xlabel('log(L$_H$$_1$/L$_H$$_0$)')
plt.ylabel('Frequency of number')
plt.title('LLR (10 rolls per experiment, 100000 exp)')
plt.text(-4, 19000,'a = 0.5', color = 'blue')
plt.text(-4, 18000,'b = 0.097 ', color = 'green')
plt.show()
