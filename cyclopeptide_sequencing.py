def peptide_mass(pep: str) -> int:
    AminoAcidMass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113,
                 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186, '': 0}
    m = 0
    for a in pep.upper():
        m += AminoAcidMass[a]
    return m


def prefix_mass(pep: str):
    for i in range(len(pep) + 1):
        yield peptide_mass(pep[:i])


def linear_spectrum(pep: str) -> list[int]:
    pmass = list(prefix_mass(pep))
    spectrum = [0]
    for i in range(len(pep)):
        for j in range(i+1, len(pep) + 1):
            spectrum.append(pmass[j] - pmass[i])
    spectrum.sort()
    return spectrum


def cyclic_spectrum(pep: str) -> list[int]:
    pmass = list(prefix_mass(pep))
    pep_mass = pmass[-1]
    c_spec = [0]
    for i in range(len(pep)):
        for j in range(i+1, len(pep) + 1):
            c_spec.append(pmass[j] - pmass[i])
            if i > 0 and j < len(pep):
                c_spec.append(pep_mass - c_spec[-1])
    c_spec.sort()
    return c_spec


def cyclopeptide_sequencing(spectrum: list[int]) -> list[list[int]]:
    candidates = [""]   # candidate peptides
    final = []          # final peptides
    parent_mass = max(spectrum) 

    while len(candidates) > 0:
        candidates = list(expand(candidates))
        
        for i in range(len(candidates) - 1, -1, -1):
            peptide = candidates[i]
            if peptide_mass(peptide) == parent_mass:
                if (cyclic_spectrum(peptide) == spectrum 
                    and peptide not in final):
                    final.append(peptide)
                del candidates[i]
            elif not set(linear_spectrum(peptide)).issubset(spectrum):
                del candidates[i]

    return final
