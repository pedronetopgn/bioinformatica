kmers = input().split(',')

prefix = []
sufix = []

for kmer in kmers:
  prefix.append([kmer[:len(kmer)-1], False]) 
  sufix.append([kmer[1:], False])

cont = 0
for idx, pre in enumerate(prefix):
  if sufix.count(pre) == 0:
    cont += 1
    start = kmers[idx]
if cont != 1:
  print("Tamanho de K insuficiente para encontrar inicio")
  exit()

cont = 0
for idx, suf in enumerate(sufix):
  if prefix.count(suf) == 0:
    cont +=1
    end = kmers[idx]
if cont != 1:
  print("Tamanho de K insuficiente para encontrar final")
  exit()

newPre = []
for i in prefix:
  if i not in newPre:
    newPre.append(i)
  else:
    newPre.append([i[0], True])
pre = newPre

arestas = {}
paresDeIndices = []
arestas[start[:-1]] =[[start[1:], False]]
verifySufix = sufix.copy()
for idxPre, pre in enumerate(prefix):
  for idxSuf, suf in enumerate(sufix):
    if pre[0] == suf[0] and idxPre != idxSuf and (not pre[1] and not suf[1]) and sufix not in verifySufix:
      if pre[0] in arestas.keys():
        arestas[pre[0]].append([kmers[idxPre][1:], False]) # 0 = vertice de destino; 1 = verificação de saída
      else:
        arestas[pre[0]] = [[kmers[idxPre][1:], False]]
      paresDeIndices.append([idxPre, idxSuf])
      pre[1] = True
      suf[1]
      verifySufix.remove(suf)
arestas[end[1:]] =[[start[:-1], False]]

def percorreArestas(start, grafo, listaDeVertices, caminhosPossiveis=[]):
  path = []
  while True:
    path.append(start)
    thereIsNoWay = True
    thereIsNewWay = False
    for destino in grafo[start]:
      if not destino[1]:
        start = destino[0]
        destino[1] = True
        thereIsNoWay = False
        thereIsNewWay = True
        break
    
    if thereIsNewWay:
      continue
    
    lifeGoesOn = False
    if thereIsNoWay:
      caminhosPossiveis.append(path)
      path = []
      for cam in caminhosPossiveis:
        for vertex in cam:
          for destino in grafo[vertex]:
            if not destino[1]:
              start = vertex
              lifeGoesOn = True
    if lifeGoesOn:
      continue
    return caminhosPossiveis

caminhos = percorreArestas(start[:-1], arestas, arestas.keys())

finalPath = []

def remonta(caminhoAtual, idx = 0):
  global finalPath
  global caminhos
  caminhoAux = caminhoAtual.copy()
  for vertices in caminhoAux:
    finalPath.append(vertices[0])
    if idx + 1 < len(caminhos):
      if vertices in caminhos[idx+1][0]:
        remonta(caminhos[idx+1][1:], idx + 1)
  caminhos.remove(caminhos[idx])
  
remonta(caminhos[0])
finalPath.pop()
for i in range(2, len(end)):
  finalPath.append(end[i])

for i in finalPath:
  print(i, end='')

finalPath = []