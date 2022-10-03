data = open("rosalind_hamm.txt", "r").read()
sequence = data.split("\n")
a = sequence[0]
b = sequence[1]

# Computing the hamming_distance, that is how many positions differ.
hamming_distance = 0
for i, j in enumerate(a):
    if j != b[i]:
        hamming_distance += 1
    else:
        pass

print(hamming_distance)
