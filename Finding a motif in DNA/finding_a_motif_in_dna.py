data = open("rosalind_subs.txt", "r").read().split("\n")
string = data[0]
substring = data[1]

# Finding starting positions of the motif (substring) in the sequence (string).
locations = []
for i, j in enumerate(string):
    if substring in string[i : i + len(substring)]:
        locations.append(i + 1)

for i in locations:
    print(i, "", end = "")
