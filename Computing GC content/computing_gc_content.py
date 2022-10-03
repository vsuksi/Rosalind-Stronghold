data = open("rosalind_gc.txt", "r").read()
sequence_labeled = data.split(">")
sequences = []
labels = []
for i in sequence_labeled:
    rows = i.split("\n")
    for j in rows:
        if "Rosalind" in j:
            labels.append(j)
            rows.remove(j)
        rows = "".join(rows)
        if rows in sequences:
            pass
        else:
            sequences.append(rows)
while "" in sequences:
    sequences.remove("")

#computing GC content of sequences and finding the sequence with highest GC content.
max_label = 0
max_content = 0
for j, i in enumerate(sequences):
    if len(i) != 0:
        if ((i.count("G") + i.count("C")) / len(i)) > max_content:
            max_label = labels[j]
            max_content = (i.count("G") + i.count("C")) / len(i)
    else:
        pass

print(max_label)
print(round(max_content * 100, 6))
