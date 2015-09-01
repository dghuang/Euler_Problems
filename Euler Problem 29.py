#Problem 29: For 2 <= a <= 100 and 2 <= b <= 100, for all permutations of a^b and b^a, how many distinct terms are generated

terms = []
for x in range(2, 101):
    for y in range(2, 101):
        if x**y not in terms:
            terms.append(x**y)
        if y**x not in terms:
            terms.append(y**x)

print len(terms)