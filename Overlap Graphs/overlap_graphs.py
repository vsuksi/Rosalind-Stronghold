data = open("rosalind_grph.txt", "r").read().split(">")
sequence_list = []
name_list = []
for i in data:
    rows = i.strip().split("\n")
    for j in rows:
        if "Rosalind" in j:
            name_list.append(j)
            rows.remove(j)
            rows = "".join(rows)
            sequence_list.append(rows)
#length of suffix and prefix
k = 3

# Compute adjacency list of sequences with k as overlap
edge_names = []
for a, b in enumerate(sequence_list):
    for c, d in enumerate(sequence_list):
        if b == d:
            pass
        elif b[-k:] in d[:k]:
            edge_name = name_list[a], name_list[c]
            edge_names.append(name_list[a])
            edge_names.append(name_list[c])
        else:
            pass

with open("viimeinkin.txt", "w") as file:
    while edge_names:
            file.write(edge_names.pop(0))
            file.write(" ")
            file.write(edge_names.pop(0))
            file.write("\n")
