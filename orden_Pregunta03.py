vector = [4,6,5,14,3,15,1,0,3]
n = len(vector)
i=0
for i in range(n):
    indice = vector[i]
    k = i-1
    while (k >= 0 and vector[k] > indice):
      vector[k+1] = vector[k]
      k = k-1
    vector[k+1] = indice

print(vector)
