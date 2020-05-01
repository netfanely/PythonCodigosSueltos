vector = [4,6,5,14,3,15,1,0,3]

n=7;
for i in range(9):
    for j in range(i+1, 9):
        if (vector[i] > vector [j]):
            auxiliar = vector[i];
            vector[i] = vector[j];
            vector[j] = auxiliar;

print(vector)
