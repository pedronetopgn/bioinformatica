def transcreveDNA(dna):
    rna = ''
    for i in dna:
        if i == 'A': rna += 'U'
        if i == 'T': rna += 'A'
        if i == 'G': rna += 'C'
        if i == 'C': rna += 'G'
    print('RNAm', rna)
    print()

i = 0
while True:
  try:
    i +=1
    dna = input()
    print('Chamada', i, '\nDNA ', dna)
    transcreveDNA(dna)
  except EOFError:
    break