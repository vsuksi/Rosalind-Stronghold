data = open("rosalind_cons.txt", "r").read().split(">")
sequence_list = []
for i in data:
    rows = i.split("\n")
    for j in rows:
        if "Rosalind" in j:
            rows.remove(j)
            rows = "".join(rows)
            sequence_list.append(rows)

# Counting the number of different bases for each position in the sequences.
A = []
C = []
G = []
T = []
for sequence in sequence_list:
    for i, j in enumerate(sequence):
        try:
            if j == "A":
                A[i] += 1
            elif j == "C":
                C[i] += 1
            elif j == "G":
                G[i] += 1
            elif j == "T":
                T[i] += 1
        except IndexError:
            A.append(0)
            C.append(0)
            G.append(0)
            T.append(0)
            if j == "A":
                A[i] += 1
            elif j == "C":
                C[i] += 1
            elif j == "G":
                G[i] += 1
            elif j == "T":
                T[i] += 1

# Generating a consensus sequence based on the most prevalent base in each position.
consensus_sequence = []
for i, j in enumerate(A):
    highest_value = max(A[i], C[i], G[i], T[i])
    if highest_value == A[i]:
        consensus_sequence += "A"
    elif highest_value == C[i]:
        consensus_sequence += "C"
    elif highest_value == G[i]:
        consensus_sequence += "G"
    elif highest_value == T[i]:
        consensus_sequence += "T"

# Random tip: how to print list elements with space.
print("A:", *A)

lines = ["".join(consensus_sequence), " ".join(str(a) for a in A)]
with open("viimeinkin.txt", "w") as file:
    file.writelines("".join(consensus_sequence))
    file.write("\n")
    file.write("A: ")
    file.writelines(" ".join(str(a) for a in A))
    file.write("\n")
    file.write("C: ")
    file.writelines(" ".join(str(c) for c in C))
    file.write("\n")
    file.write("G: ")
    file.writelines(" ".join(str(g) for g in G))
    file.write("\n")
    file.write("T: ")
    file.writelines(" ".join(str(t) for t in T))
