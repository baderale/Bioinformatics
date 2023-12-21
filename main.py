from DNAToolkit import *
import random

rndDNAseq = 'atgctgatgctg'

#validateSeq(rndDNAseq)

#Creating a random list of n-nucleotides from the Nucleotide list
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)

print(validateSeq(randDNAStr)) # Returns a validated sequence
print(countNucFrequency(DNAStr)) # Counts nucleotides in a validated sequence