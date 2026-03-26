dna = list(input())[::-1]

for base in range(len(dna)):
    if (dna[base] == 'A'):
        dna[base] = 'T'
    elif (dna[base] == 'T'):
        dna[base] = 'A'
    elif (dna[base] == 'C'):
        dna[base] = 'G'
    elif (dna[base] == 'G'):
        dna[base] = 'C'

print(*dna, sep = '')