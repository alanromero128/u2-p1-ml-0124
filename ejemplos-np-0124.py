import numpy as np

califas=np.array([60,70,90])
print(" ---------- Ej 1 imprimir califas  ----------")
print(califas) #imprime la lista de califas
print(type(califas)) # muestra el tipo de arreglo
print(" ---------- Ej 0 dimensiones de un array  ----------")
califas=np.array(60)
print(califas) 
print("Dimension :", califas.ndim)
print(" ---------- Ej 1 dimension de un array  ----------")
califas=np.array([60,70,90])
print(califas) 
print("Dimension :", califas.ndim)
print(" ---------- Ej 2 dimensiones de un array  ----------")
califas=np.array([[
    60,70,90],
    [20,80,98]
    ]) #Un arreglo de 2 dimensiones es como una tabla en excel
print(califas) 
print("Dimension :", califas.ndim)
print(" ---------- Ej 3 dimensiones de un array  ----------")
califas=np.array([
    [
    [60,70,90],
    [50,80,98]
    ],
    [
    [60,70,90],
    [50,80,98]
    ]
    ]) #Un arreglo de 3 dimensiones es como una tabla en excel
print(califas) 
print("Dimension :", califas.ndim)
