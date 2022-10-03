#1
"""
data = open("rosalind_rna.txt", "r")
rna_sequence = data.read().replace("T", "U")
print(rna_sequence)
"""

#2 If the data was on different rows and there were blank rows:
"""
data = open("rosalind_rna.txt", "r")
rna_sequence = data.read().replace("T", "U").split("\n")
stripped_rna_sequence = []
for i in rna_sequence:
    stripped_rna_sequence += i.strip("")
joined_rna_sequence = "".join(stripped_rna_sequence)
print(joined_rna_sequence)
"""
