# output the sorted mass spectrum of a cyclic peptide

def peptide_mass(pep: str) -> int:  # return the mass of a peptide
    AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186, '': 0}
    m = 0
    for a in pep.upper():
        m += AminoAcidMass[a]
    return m
