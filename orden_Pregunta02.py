vector = [4,6,5,14,13,15,1,0,3]

n=9;
k=1;
for k in range(1,n,k*3+1):
    while k>0:
        for i in range(int(k),int(n)):
            j=i;
            auxiliar=vector[i];
            while j>=k and vector[int(j-k)]>auxiliar:
                vector[j]=vector[j-k];
                j=j-k;
            vector[j]=auxiliar;
        k=k/2;

print(vector);
