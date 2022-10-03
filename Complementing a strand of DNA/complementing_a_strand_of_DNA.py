data = open("rosalind_revc.txt", "r")
sequence = data.read()

# Creating reverse complement of sequence
reverse_sequence = []
for base in reversed(sequence):
    reverse_sequence += base
complemented_reverse_sequence = []
for i in reverse_sequence:
    if i == "A":
        complemented_reverse_sequence += "T"
    if i == "T":
        complemented_reverse_sequence += "A"
    if i == "C":
        complemented_reverse_sequence += "G"
    if i == "G":
        complemented_reverse_sequence += "C"

print("".join(complemented_reverse_sequence))
