from DNAToolkit import *
from utilities import colored
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr) 

print(f'Sequence: {colored(DNAStr)}') 
print(f'[1] *** Sequence Length: {len(DNAStr)}')
print(colored(f'[2] *** Nucleotide Frequency: {countNucFrequency(DNAStr)}')) 
print(f'[3] *** Complementary RNA sequence: {colored(transcription(DNAStr))}') 
print(f"[4] *** DNA Sequence + Reverse Complement:\n        5' {colored(DNAStr)} 3' ")
print(f"           {''.join(['|' for c in range(len(DNAStr))])}")
print(f"        3' {colored(reverse_complement(DNAStr))} 5'")
print(f'[5] *** G/C Content: {gc_content(DNAStr)}%')