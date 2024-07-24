# returns the reverse complement of a template dna strand
def reverseComplement(template: str):
    rc = ""
    for c in template:
        if c == 'A':
            rc += 'T'
        elif c == 'C':
            rc += 'G'
        elif c == 'G':
            rc += 'C'
        else:
            rc += 'A'
    return rc[::-1]
