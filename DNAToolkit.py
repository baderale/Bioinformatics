# DNA Toolset/Code 
from structures import *

Nucleotides = ['A', 'C', 'T', 'G']

# DNA Sequence Validation fucntion
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper() 
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq   # returns an uppercase version

# Count number of nucleotides in a DNA sequence
def countNucFrequency(seq):
    tmpFreqDict = {'A':0, 'C':0, 'G':0, 'T':0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

# Create a complemantary DNA sequence, DNA--->RNA
def transcription(seq):
    """DNA to RNA ---> Replaces Thymine(T) with Uracil(U)"""
    return seq.replace('T', 'U')

# Create a DNA reverse complement
DNA_ReverseComplement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} # Dictionary with complements
def reverse_complement(seq):
    """ Swaps Adenine(A) with Thymine(T) and Guanine(G) with Cytosine(C).
        Creates a reverse string"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]