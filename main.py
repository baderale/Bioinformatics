from DNAToolkit import *
import random

rndDNAseq = 'atgctgatgctg'

#validateSeq(rndDNAseq)

#Creating a random list of n-nucleotides from the Nucleotide list
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr) # Creating a validated, random DNA sequence

print(f'Validated Sequence: {validateSeq(randDNAStr)}') # Returns a validated sequence
print(f'[1] + The nucleotide count of the validated sequence is {countNucFrequency(DNAStr)}') # Return the count of nucleotides in a validated sequence
print(f'[2] + The complemenrary RNA sequence is: {transcription(DNAStr)}') #Returns the complementary RNA sequence (transcription)