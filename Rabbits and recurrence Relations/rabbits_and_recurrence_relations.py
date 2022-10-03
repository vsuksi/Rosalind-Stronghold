#number of months
n = 35
#litter size in pairs
k = 5
#element in list up to which the rabbits are reproduction age as they mature in one month
c = 0
mature_generations = [0]
while n > 1:
    if sum(mature_generations) == 0:
        mature_generations.append(1)
    elif sum(mature_generations) == 1:
        mature_generations.append(1 * k)
    else:
        mature_generations.append(sum(mature_generations[:c]) * k)
    n = n - 1
    c += 1
print(sum(mature_generations))
print(mature_generations)
