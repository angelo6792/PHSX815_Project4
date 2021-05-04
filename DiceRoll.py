#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
from fractions import Fraction 
# import our Random class from python/Random.py file
sys.path.append(".")
from Random2 import Random

# main function for our dice roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default dice roll  probability for "1"
    prob1 = Fraction(1,6)
    prob2 = Fraction(1,6)
    prob3 = Fraction(1,6)
    prob4 = Fraction(1,6)
    prob5 = Fraction(1,6)
    prob6 = Fraction(1,6)

    #default number of probs i.e. # of sides of the dice
    num_probs = 6
    
    #initiate list of probabilities
    prob_list = []
    
    # default number of rolls (per experiment)
    Nroll = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line and change dice probabilities (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    #read num_probs i.e. number of dice sides
    if '-num_probs' in sys.argv:
        p = sys.argv.index('-num_probs')
        num_probs = int(sys.argv[p+1])
    #this lets you have a smaller number of inputs! Instead of -p1 0.1 -p2 0.2 ... you can just do -prob_list 0.1 0.2 0.3 ...
    if '-prob_list' in sys.argv:
        p = sys.argv.index('-prob_list')
        for i in range(num_probs):
            ptemp = float((sys.argv[p+1+i]))
            if ptemp >= 0 and ptemp <= 1:
                prob_list = np.append(prob_list, ptemp)
            else:
                print("Error: probabilities must be in the range [0,1]")
                sys.exit(1)
    if '-Nroll' in sys.argv:
        p = sys.argv.index('-Nroll')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nroll = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True
        
    #extract individual probabilities from list; may have to automate if you choose to work with dice w/o 6 sides
    prob1, prob2, prob3, prob4, prob5, prob6 = prob_list[0], prob_list[1], prob_list[2], prob_list[3], prob_list[4], prob_list[5]

    # class instance of our Random class using seed
    random = Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.Diceroll(prob1,prob2,prob3,prob4,prob5,prob6))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.Diceroll(prob1,prob2,prob3,prob4,prob5,prob6), end=' ')
            print(" ")
