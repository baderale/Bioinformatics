from DNAToolkit import *
from utilities import colored
import random

rndDNAseq = 'atgctgatgctg'

#validateSeq(rndDNAseq)

#Creating a random list of n-nucleotides from the Nucleotide list
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr) # Creating a validated, random DNA sequence

print(f'Sequence: {colored(DNAStr)}') # Returns a validated sequence
print(colored(f'[1] *** Nucleotide Frequency: {countNucFrequency(DNAStr)}')) # Return the count of nucleotides in a validated sequence
print(f'[2] *** Complementary RNA sequence: {colored(transcription(DNAStr))}') #Returns the complementary RNA sequence (transcription)
print(f"[3] *** DNA Sequence + Reverse Complement:\n        5' {colored(DNAStr)} 3' ")
print(f"           {''.join(['|' for c in range(len(DNAStr))])}")
print(f"        3' {colored(reverse_complement(DNAStr))} 5'")