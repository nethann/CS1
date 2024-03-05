# """
# Program Description: This program takes a given DNA sequence translates it to a protein sequence.

# Author:
# """

# import helper

# def transcription(dna_sequence):
#     complement = ''

#     # Create the Base Pair Complement

#     # Replace Thymine with Uracil

#     return mrna

# def translate(mrna):
#     protein = ''

#     # Split mrna into nucleotide triplets

#     # Replace Triplets with Amino Acids

#     return protein


# dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'




# Dictionary for Nucleotide to Amino Acid conversion
# This is a simplified version; you should use the full dictionary provided in the helper.py file
# Amino acids dictionary as provided
amino_acids_dict = {
    'UUU': 'Phe',
    'UUC': 'Phe',

    'UUA': 'Leu',
    'UUG': 'Leu',
    'CUU': 'Leu',
    'CUC': 'Leu',
    'CUA': 'Leu',
    'CUG': 'Leu',

    'AUU': 'Ile',
    'AUC': 'Ile',
    'AUA': 'Ile',

    'AUG': 'Met',

    'GUU': 'Val',
    'GUC': 'Val',
    'GUA': 'Val',
    'GUG': 'Val',

    'UCU': 'Ser',
    'UCC': 'Ser',
    'UCA': 'Ser',
    'UCG': 'Ser',
    'AGU': 'Ser',
    'AGC': 'Ser',

    'CCU': 'Pro',
    'CCC': 'Pro',
    'CCA': 'Pro',
    'CCG': 'Pro',

    'ACU': 'Thr',
    'ACC': 'Thr',
    'ACA': 'Thr',
    'ACG': 'Thr',

    'GCU': 'Ala',
    'GCC': 'Ala',
    'GCA': 'Ala',
    'GCG': 'Ala',

    'UAU': 'Tyr',
    'UAC': 'Tyr',

    'UAA': 'STOP',
    'UAG': 'STOP',

    'CAU': 'His',
    'CAC': 'His',

    'CAA': 'Gln',
    'CAG': 'Gln',

    'AAU': 'Asn',
    'AAC': 'Asn',

    'AAA': 'Lys',
    'AAG': 'Lys',

    'GAU': 'Asp',
    'GAC': 'Asp',

    'GAA': 'Glu',
    'GAG': 'Glu',

    'UGU': 'Cys',
    'UGC': 'Cys',

    'UGA': 'STOP',

    'UGG': 'Trp',

    'CGU': 'Arg',
    'CGC': 'Arg',
    'CGA': 'Arg',
    'CGG': 'Arg',
    'AGA': 'Arg',
    'AGG': 'Arg',

    'GGU': 'Gly',
    'GGC': 'Gly',
    'GGA': 'Gly',
    'GGG': 'Gly',
}

def transcription(dna_sequence):
    rna_sequence = dna_sequence.replace('T', 'U')
    mRNA_sequence = ''
    complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    for nucleotide in rna_sequence:
        mRNA_sequence += complement[nucleotide]

    return mRNA_sequence


def chunk_sequence(string, chunk_size):
    chunks = []  # Initialize an empty list to store the chunks
    for i in range(0, len(string), chunk_size):
        chunk = string[i:i+chunk_size]  # Extract a chunk of the given size
        chunks.append(chunk)  # Add the chunk to the list of chunks
    return chunks


def translation(mRNA_sequence):
    triplets = chunk_sequence(mRNA_sequence, 3)
    protein_sequence = []
    for triplet in triplets:
        amino_acid = amino_acids_dict.get(triplet, '')
        if amino_acid == 'STOP':
            protein_sequence.append('STOP')
            break
        elif amino_acid:
            protein_sequence.append(amino_acid)
    return ' '.join(protein_sequence)


dna_sequence = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'

mrna_sequence = transcription(dna_sequence)

protein_sequence = translation(mrna_sequence)

print(dna_sequence)
print(mrna_sequence)
print(protein_sequence)