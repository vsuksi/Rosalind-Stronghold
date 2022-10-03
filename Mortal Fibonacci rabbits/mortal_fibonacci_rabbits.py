# Number of months
n = 81
# Pairs of offspring
k = 1
# Rabbit life length
m = 17

# Total number of rabbits after n months if all rabbits live for m months
generations = [0]
while n >= 1:
    if sum(generations) == 0:
        generations.append(1)
    elif sum(generations) == 1:
        generations.append(1 * k)
    else:
        generations.append(sum(generations[-m : -1 ]) * k)
    n = n - 1

print(sum(generations[-m : -1]))
print(generations)
