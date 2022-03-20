from aminoacidos import aminoacidos

def gera_amino(rna_m):
    start = False
    for n in range(0, len(rna_m)-1, 3):
        trinca = rna_m[n:n+3]
        if 'Metionina' in aminoacidos[trinca]:
            start = True
        if start:
            print(aminoacidos[trinca])
            if 'Âmbar' in trinca or 'Ocre' in trinca or 'Opala' in trinca:
                print()
                break           

i = 0
while True:
  try:
    i +=1
    rna_m = input()
    print('\nChamada', i, '\nRNAm ', rna_m,)
    gera_amino(rna_m)
  except EOFError:
    break