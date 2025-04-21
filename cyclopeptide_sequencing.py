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
