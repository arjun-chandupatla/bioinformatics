# find sequences within a strand of dna that encode for a specific peptide sequence
def protein_translate(rna: str):    # translate rna to protein
    genCode = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    peptide = ""

    rna2 = ""

    for base in rna:
        if not base.isspace():
            rna2 += base
            
    for i in range(0, len(rna2), 3):
        nextAminoAcid = genCode[rna2[i:i+3]]
        if nextAminoAcid == "STOP":
            return peptide.strip()
        else:
            peptide += nextAminoAcid
    
    return peptide

def transcribe(dna: str) -> str:
    rna = ""
    for base in dna.upper():
        if base == "T":
            rna += "U"
        else:
            rna += base
    return rna


def reverse_transcribe(rna: str) -> str:
    dna = ""
    for base in rna.upper():
        if base == "U":
            dna += "T"
        else:
            dna += base
    return dna

def reverse_complement_rna(template: str) -> str:
    rc = ""
    rcDict = {"A": "U",
              "C": "G",
              "G": "C",
              "U": "A"}

    for base in range(len(template)):
        rc += rcDict[template[base]]
    return rc[::-1]

def complement(template: str) -> str:
    c = ""
    cDict = {"A": "T",
              "C": "G",
              "G": "C",
              "T": "A"}

    for base in range(len(template)):
        c += cDict[template[base]]
    return c

def get_rna_strands(dna: str) -> list[str]: 
    rnaStrands = []
    rna = transcribe(dna)
    rnaStrands.append(rna)
    rnaStrands.append(reverse_complement_rna(rna))

    return rnaStrands

def protein_encode(rnaSet: list[str], peptide: str) -> list[str]:
    dnaStrands = []
    k = 3 * len(peptide)
    for x in range(2):
        rna = rnaSet[x]
        for i in range(len(rna) - k + 1):
            win = rna[i:i+k]
            temp = ""
            for j in range(i, i + len(win), 3):
                temp += protein_translate(rna[j:j+3])
            if temp == peptide:
                if x == 1:      # reverse strand
                    win = win[::-1]
                    win = reverse_transcribe(win)
                    dnaStrands.append(complement(win))
                    #dnaStrands.append(len(rna) - i)
                else: 
                    dnaStrands.append(reverse_transcribe(win))
                    #dnaStrands.append(i)
                

    return dnaStrands
