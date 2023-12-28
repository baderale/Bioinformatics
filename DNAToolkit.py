# DNA Toolset/Code 
from structures import *

def validateSeq(dna_seq):
    """DNA Sequence Validation function"""
    tmpseq = dna_seq.upper() 
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq   # returns an uppercase version

def countNucFrequency(seq):
    """Count number of nucleotides in a DNA sequence"""
    tmpFreqDict = {'A':0, 'C':0, 'G':0, 'T':0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(seq):
    """DNA to RNA ---> Replaces Thymine(T) with Uracil(U)"""
    return seq.replace('T', 'U')

def reverse_complement(seq):
    """ Swaps Adenine(A) with Thymine(T) and Guanine(G) with Cytosine(C).
        Creates a reverse string"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

def gc_content(seq):
        """GC Content in a DNA/RNA sequence"""
        return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subsec(seq, k=20):
        """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
        res = []
        for i in range(0, len(seq) - k + 1, k):
            subseq = seq[i:i + k]
            res.append(
                round((subseq.count('C') + subseq.count('G')) / len(subseq) * 100))
        return res
