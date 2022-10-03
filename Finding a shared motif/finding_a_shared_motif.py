# Reading in data
sequence_list = []
data = open("rosalind_lcsm.txt", "r").read().split(">")
for i in data:
    rows = i.strip().split("\n")
    for j in rows:
        if "Rosalind" in j:
            rows.remove(j)
            rows = "".join(rows)
            sequence_list.append(rows)

# The following snippet is here for the checking of the result, since the sequences are too long to simply print.
print(len(sequence_list))
with open("viimeinkin_data.txt", "w") as file:
    for i in sequence_list:
        file.write(i)
        file.write("\n")

# For each count of n, add the longest string (first to satisfy the below condition) to a list of which max(len) is taken for the longest shared sequence
sequence = sequence_list[0]
n = 0
shared_substring = []
shared_substrings = []
fragment_end = len(sequence)
check = False
while n < len(sequence):
    for i in sequence_list:
        if i == sequence:
            pass
        elif sequence[n:fragment_end + 1] in i:
            shared_substring.append(sequence[n:fragment_end + 1])
        else:
            shared_substring = []
            break
    if shared_substring:
        shared_substrings.append(shared_substring[0])
        shared_substring = []
    if fragment_end == 1:
        n += 1
        fragment_end = len(sequence)
    else:
        fragment_end -= 1

    shared_substring = []

#Writing data to file
with open("viimeinkin.txt", "w") as file:
    file.write(max(shared_substrings, key=len))
