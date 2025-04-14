# Algoritmo eficiente de mediana móvil

Este repositorio contiene la implementación un algoritmo eficiente de mediana movil, utilizando una estructura de datos basada en montículos. Esta técnica permite obtener la mediana de un conjunto de datos dentro de una ventana deslizante de tamaño fijo, de manera rápida y eficiente. Es especialmente útil para aplicaciones como análisis de datos, procesamiento de señales y estadísticas, especialmente cuando se trabaja con flujos de datos.

## Características

- **Inserción eficiente**: Los datos se insertan en el montículo manteniendo el balance entre los montículos de mínimo y máximo.
- **Obtención de la mediana**: La mediana se obtiene dinámicamente al insertar o eliminar elementos.
- **Ventana deslizante**: Soporte para una ventana de tamaño fijo, eliminando automáticamente los elementos más antiguos cuando se excede el límite.
- **Rebalanceo automático**: Los montículos se rebalancean automáticamente para garantizar que la diferencia de tamaño entre ellos sea como máximo 1.

## Ejemplo de uso 
```
from monticulo_med import MonticuloMediana

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
```

## El proyecto esta organizado de la siguiente manera:

```
monticulo_mediana_movil/
├── .vscode/               
│   └── settings.json      # archivo de configuración de directorios
│
├── ejemplo/               
│   └── ejemplo.py         # ejemplo de uso
│
├── modules/               # directorio con los módulos principales
│   ├── cola.py            
│   ├── monticulo_med.py   
│   ├── monticulo.py       
│   └── registro.py        
│
├── LICENSE                
│
└── README.md              
```

## Licencia
Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE.md para más detalles.

## DOI

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15214365.svg)](https://doi.org/10.5281/zenodo.15214365)

