#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
# import our Random class from python/Random.py file
sys.path.append(".")

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


#loads text and put text into an array for the LLR graph
RollsH0 = np.loadtxt(H0)
RollsH1 = np.loadtxt(H1)
print(len(RollsH0),len(RollsH1))
a0 = []
a1 = []
#Use RollsH0.shape or len(RollsH0) to determine the hsape/length of your data; Can you recover Nrolls and Nexp from these data files? If so:
Nrolls = 
Nexp = 
               #have to manually change range to match Nexp. Not sure how to get it to change from command line
for j in range(0,Nexp):
    LLR0 = 0
    for l in range(0,Nrolls???):
        if RollsH0[j][l] == 1:
           LLR0 = LLR0+math.log(1/10)
        elif RollsH0[j][l] == 2:
           LLR0 = LLR0+math.log(1/10)
        elif RollsH0[j][l] == 3:
           LLR0 = LLR0+math.log(1/10)
        elif RollsH0[j][l] == 4:
           LLR0 = LLR0+math.log(2/10)
        elif RollsH0[j][l] == 5:
           LLR0 = LLR0+math.log(2/10)
        elif RollsH0[j][l] == 6:
           LLR0 = LLR0+math.log(3/10)
        if RollsH0[j][l] == 1:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 2:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 3:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 4:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 5:
           LLR0 = LLR0-math.log(1/6)
        elif RollsH0[j][l] == 6:
           LLR0 = LLR0-math.log(1/6)
    a0.append(LLR0)

for j in range(0,Nexp):
    LLR1 = 0
    for l in range(0,Nrolls???):
        if RollsH1[j][l] == 1:
           LLR1 = LLR1+math.log(1/10)
        elif RollsH1[j][l] == 2:
           LLR1 = LLR1+math.log(1/10)
        elif RollsH1[j][l] == 3:
           LLR1 = LLR1+math.log(1/10)
        elif RollsH1[j][l] == 4:
           LLR1 = LLR1+math.log(2/10)
        elif RollsH1[j][l] == 5:
           LLR1 = LLR1+math.log(2/10)
        elif RollsH1[j][l] == 6:
           LLR1 = LLR1+math.log(3/10)
        if RollsH1[j][l] == 1:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 2:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 3:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 4:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 5:
           LLR1 = LLR1-math.log(1/6)
        elif RollsH1[j][l] == 6:
           LLR1 = LLR1-math.log(1/6)
    a1.append(LLR1)

#flatten data files and sorts them for probability graph
RollH0 = RollsH0.flatten()
RollH1 = RollsH1.flatten()
RollH0.sort()
RollH1.sort()

#calculates the alpha of our experiment
Alpha = .05
a =len(a0)-int(len(a0)*Alpha)

#probability distribution graph
density0, bins0 =np.histogram(RollH0,bins=np.arange(8)-0.5, density = True)
density1, bins1 =np.histogram(RollH1,bins=np.arange(8)-0.5, density = True)
unity_density0 = density0 / density0.sum()
unity_density1 = density1 / density1.sum()

fig, ax = plt.subplots(figsize = (6,6))
widths = bins0[:-1] - bins0[1:]
ax.bar(bins0[1:], unity_density0, width=widths, color='blue', alpha = 1.0, align ='edge')
ax.bar(bins1[1:], unity_density1, width=widths, color='green', alpha = 0.75, align ='edge')

ax.set_xlim(0,7)
ax.set_xlabel('Dice number')
ax.set_ylabel('Probability')
ax.set_title('Probability distribution for a single diceroll')
ax.legend(['fair dice','unfair dice'])

#LLR graph
plt.figure()
plt.hist(a0,10, alpha=.75, color='blue')
plt.hist(a1,10, alpha=.75, color='green')
plt.axvline(a0[a], color='red', label=['a = 0.5'])
plt.legend (['λ = 0.26','H0','H1'],loc = 'upper left' )
plt.xlabel('log(L$_H$$_1$/L$_H$$_0$)')
plt.ylabel('Frequency of number')
plt.title('LLR (' + str(Nrolls) + ' rolls per experiment, ' + str(Nexp) + ' exp)')
plt.text(-5.3, 20000,'a = 0.5', color = 'blue')
plt.text(-5.3, 19000,'b = 0.038 ', color = 'green')
plt.show()
