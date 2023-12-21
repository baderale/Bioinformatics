from DNAToolkit import *
import random

rndDNAseq = 'atgctgatgctg'

#validateSeq(rndDNAseq)

#Creating a random list of n-nucleotides from the Nucleotide list
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr) # Creating a validated, random DNA sequence

print(f'Sequence: {validateSeq(randDNAStr)}') # Returns a validated sequence
print(f'[1] + The nucleotide count of the validated sequence is {countNucFrequency(DNAStr)}') # Return the count of nucleotides in a validated sequence
print(f'[2] + The complementary RNA sequence is: {transcription(DNAStr)}') #Returns the complementary RNA sequence (transcription)
print(f"[3] + The reverse complement is:\n5' {DNAStr} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print()