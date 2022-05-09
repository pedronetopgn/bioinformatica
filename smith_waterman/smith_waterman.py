# Recebendo arquivo de entrada
with open('entrada.txt') as f:
  content = f.readlines()
content = [x.rstrip('\n') for x in content] 

sequencia1 = content[0]
sequencia2 = content[1]

print('Sequencias iniciais:')
print(sequencia1)
print(sequencia2)

mismatch = -1
match = 3
gap = -2

# Inicializando a lista de scores
score = []
for i in range(len(sequencia1)+1):
  row = []
  for j in range(len(sequencia2)+1):
    if i == 0:
      row.append(j*gap)
      continue
    if j == 0: 
      row.append(i*gap)
      continue    
    row.append(0)
  score.append(row)

backtrace = [] # Pode se imaginar como um gerador dos scores do código
for i_idx, i in enumerate(sequencia1):
  backtrace_row = []
  for j_idx, j in enumerate(sequencia2):
    if i == j:
      aux = match
    else:
      aux = mismatch
    score_diagonal = score[i_idx][j_idx] + aux
    
    score_vertical = score[i_idx][j_idx+1] + gap

    score_horizontal = score[i_idx+1][j_idx] + gap

    max_score = max([score_diagonal, score_vertical, score_horizontal])

    if score_diagonal == max_score:
      backtrace_row.append((i_idx-1, j_idx-1))
    elif score_vertical == max_score:
      backtrace_row.append((i_idx-1, j_idx))
    elif score_horizontal == max_score:
      backtrace_row.append((i_idx, j_idx-1))

    score[i_idx+1][j_idx+1] = max_score
  backtrace.append(backtrace_row)

max_score = -float('inf') #Vai ser sempre menor na primeira comparação
max_indice = 0
for i in range(len(score) -1, 0, -1):
  if max_score < max(score[i][1:]):
    max_score = max(score[i][1:])
    max_indice = (i-1, score[i][1:].index(max_score))

seqCorrigida1 = ''
seqCorrigida2 = ''

# Posição mais alta da matriz  
aux = (len(backtrace)-1, len(backtrace[0])-1)
while(True):
  aux1 = aux
  aux = backtrace[aux1[0]][aux1[1]]

  # Apenas ultimo caso, quando se considera apenas uma direção
  if aux1[0] < 0:
    for i in range(aux1[1], -1, -1):
      seqCorrigida1 += '-'
      seqCorrigida2 += sequencia2[i]
    break      

  # Apenas ultimo caso, quando se considera apenas uma direção
  if aux1[1] < 0:
    for i in range(aux1[0], -1, -1):
      seqCorrigida1 += sequencia1[i]
      seqCorrigida2 += '-'
    break

  # Direção de onde veio o array
  if aux[0] == aux1[0]:               # Voltou na horizontal
    seqCorrigida1 += '-'
    seqCorrigida2 += sequencia2[aux1[1]]
  elif aux[1] == aux1[1]:             # Voltou na vertical
    seqCorrigida1 += sequencia1[aux1[0]]
    seqCorrigida2 += '-'
  else:                               # Voltou na diagonal
    seqCorrigida1 += sequencia1[aux1[0]]
    seqCorrigida2 += sequencia2[aux1[1]]
  
  if aux1 == (-1, -1):
    break

print('-'*50)

print('Score Final:')
print(score[-1][-1])

print('-'*50)
print("Sequencia 1 gerada:", seqCorrigida1[len(seqCorrigida1)::-1])
print("Sequencia 2 gerada:", seqCorrigida2[len(seqCorrigida1)::-1])