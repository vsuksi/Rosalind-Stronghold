rna_sequence = open("rosalind_prot.txt", "r").read()

# Translation of RNA into peptide according the two first codons.
peptide_sequence = []
while rna_sequence:
    codon = rna_sequence[:3]
    rna_sequence = rna_sequence[3:]
    if codon[0] == "G":
        if codon[1] == "U":
            peptide_sequence.append("V")
        elif codon[1] == "C":
            peptide_sequence.append("A")
        elif codon[1] == "A":
            if codon[2] == "U" or codon[2] == "C":
                peptide_sequence.append("D")
            else:
                peptide_sequence.append("E")
        else:
            peptide_sequence.append("G")
    elif codon[0] == "A":
        if codon[1] == "U":
            if codon[2] == "G":
                peptide_sequence.append("M")
            else:
                peptide_sequence.append("I")
        elif codon[1] == "C":
            peptide_sequence.append("T")
        elif codon[1] == "A":
            if codon[2] == "U" or codon[2] == "C":
                peptide_sequence.append("N")
            else:
                peptide_sequence.append("K")
        else:
            if codon[2] == "U" or codon[2] == "C":
                peptide_sequence.append("S")
            else:
                peptide_sequence.append("R")
    elif codon[0] == "C":
        if codon[1] == "U":
            peptide_sequence.append("L")
        elif codon[1] == "C":
            peptide_sequence.append("P")
        elif codon[1] == "A":
            if codon[2] == "U" or codon[2] == "C":
                peptide_sequence.append("H")
            else:
                peptide_sequence.append("Q")
        else:
            peptide_sequence.append("R")
    elif codon[0] == "U":
        if codon[1] == "U":
            if codon[2] == "U" or codon[2] == "C":
                peptide_sequence.append("F")
            else:
                peptide_sequence.append("L")
        elif codon[1] == "C":
            peptide_sequence.append("S")
        elif codon[1] == "A":
            if codon[2] == "U" or codon[2] == "C":
                peptide_sequence.append("Y")
            else:
                rna_sequence = []
        else:
            if codon[2] == "G":
                peptide_sequence.append("W")
            elif codon[2] == "A":
                rna_sequence = []
            else:
                peptide_sequence.append("C")
    else:
        pass

print("".join(peptide_sequence))
