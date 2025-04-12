from modulos.monticulo_med import MonticuloMediana

monticulo = MonticuloMediana(5)
valores = []

# mediana de una serie de valores
for i in range(11):
    print(f"Mediana de valores {valores}: ", monticulo.mediana)
    monticulo.insertar(i)
    valores.append(i)
    
# ----------------
# Salida esperada:
# ----------------
# Mediana de valores []:  None
# Mediana de valores [0]:  0
# Mediana de valores [0, 1]:  0.5
# Mediana de valores [0, 1, 2]:  1
# Mediana de valores [0, 1, 2, 3]:  1.5
# Mediana de valores [0, 1, 2, 3, 4]:  2
# Mediana de valores [0, 1, 2, 3, 4, 5]:  3
# Mediana de valores [0, 1, 2, 3, 4, 5, 6]:  4
# Mediana de valores [0, 1, 2, 3, 4, 5, 6, 7]:  5
# Mediana de valores [0, 1, 2, 3, 4, 5, 6, 7, 8]:  6
# Mediana de valores [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:  7