from bio_lib import allKmers, hamming_distance
import sys


def median_string(dna: list[str], k: int) -> str:
    dist = float('inf')
    for pattern in allKmers(k):
        d = distance_between_pattern_and_strings(pattern, dna)
        if dist > d:
            dist = d
            median = pattern
    return median



def distance_between_pattern_and_strings(pattern: str, dna: list[str]):
    k = len(pattern)
    distance = 0
    for text in dna:
        hamDist = float('inf')
        for i in range(len(text) - k + 1):
            kmer = text[i:i+k]
            if hamDist > hamming_distance(pattern, kmer):
                hamDist = hamming_distance(pattern, kmer)
        distance += hamDist
    return distance