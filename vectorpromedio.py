# En una encuensta realizada por el INEI se encontraron diferentes
# estaturas 167,178,157,189,156,169, 158,175,191,171
# y se necesita mostrar el de cada uno
# si esta arriba del promedio general de estatura del Peru (159 cm)

promedio = 159

vector = [167, 178, 157, 189, 156, 169, 158, 175, 191, 171]
vectorprom = [0,0,0,0,0,0,0,0,0,0]
j=0
for i in range(10):

    if (vector[i] > promedio):
        vectorprom[j] = vector[i]
        j+=1

print(vectorprom)

##############################################
# [167, 178, 189, 169, 175, 191, 171, 0, 0, 0]
#
##############################################
