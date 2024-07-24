from bio_lib import profile, hamming_distance
import numpy


def consensus(motifs):
    cString = ""
    prof = numpy.transpose(profile(motifs))
    for i in prof:
        mValue = max(i)
        if i[0] == mValue:
            cString += "A"
        if i[1] == mValue:
            cString += "C"
        if i[2] == mValue:
            cString += "G"
        if i[3] == mValue:
            cString += "T"
    print(cString)
    return cString


def score(motifs):
    cString = consensus(motifs)
    netScore = 0
    for motif in motifs:
        netScore += hamming_distance(motif, cString)
    return netScore



m = "TCGGGGGTTTTT CCGGTGACTTAC ACGGGGATTTTC TTGGGGACTTTT AAGGGGACTTCC TTGGGGACTTCC TCGGGGATTCAT TCGGGGATTCCT TAGGGGAACTAC TCGGGTATAACC".split()
consensus(m)