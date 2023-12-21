# DNA Toolset/Code 
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