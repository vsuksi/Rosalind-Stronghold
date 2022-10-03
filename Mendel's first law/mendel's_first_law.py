#homozygous dominant for factor
k = 28
#heterozygous for factor
m = 30
#homozygous recessive for factor
n = 21

# Computing the probability of any offspring having a dominant allele.
population = k + m + n
kk_domprob = k/population * (k - 1)/(population - 1)
km_domprob = k/population * m/(population - 1)
kn_domprob = k/population * n/(population - 1)
mm_domprob = m/population * (m - 1)/(population - 1) * 0.75
mk_domprob = m/population * k/(population - 1)
mn_domprob = m/population * n/(population - 1) * 0.50
#nn_domprob = n/population * (n - 1)/(population - 1) * 0.00
nk_domprob = n/population * k/(population - 1)
nm_domprob = n/population * m/(population - 1) * 0.50

prob_X_dom = kk_domprob + km_domprob + kn_domprob + mm_domprob + mk_domprob + mn_domprob + nk_domprob + nm_domprob
print(round(prob_X_dom, 5))
