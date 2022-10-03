# Number of pairs according to the alleles for a trait. For example: kk is a pair where both parents are homozygous dominant.
# k = homozygous dominant, m = heterozygous and n = homozygous recessive
kk = 18504
km = 18989
kn = 18415
mm = 16692
mn = 17318
nn = 18694

# Calculating expected offspring displaying the dominant phenotype if  each pair begets two offspring.
kk_domprob = kk * 2
km_domprob = km * 2
kn_domprob = kn * 2
mm_domprob = (0.75 * mm) * 2
mn_domprob = (0.50 * mn) * 2

# Summing the offspring of each pair for the total expected offspring displaying the dominant phenotype.
expected_dom_offspring = kk_domprob + km_domprob + kn_domprob + mm_domprob + mn_domprob

print(expected_dom_offspring)
