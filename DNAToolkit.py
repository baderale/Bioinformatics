# DNA Toolset/Code 
Nucleotides = ['A', 'C', 'T', 'G']

# DNA Sequence Validation fucntion
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq
