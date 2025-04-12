from modulos.monticulo import Monticulo
from modulos.registro import Registro
from modulos.cola import Cola

class MonticuloMediana:
    def __init__(self, k): 
        self.__mont_max = Monticulo('max')  
        self.__mont_min = Monticulo()     
        self.__mediana = None
        self.__ventana = k
        self.__cola_mont = Cola()

    @property
    def mediana(self):
        """
        Devuelve la mediana del montículo
        """
        return self.__mediana

    @mediana.setter
    def mediana(self, mediana):
        raise Exception ("Operación no permitida.")

    def construir_monticulo(self, iterable) :
        for i in iterable:
            self.insertar(i)

    def insertar(self, dato):
        """
        Inserta un número en el montículo de mediana móvil.

        Descripción:
        Este método inserta un número en el montículo de mediana móvil, ajustando los montículos de mínimo y máximo según sea necesario, 
        y recalculando la mediana. Si el tamaño de la ventana excede el límite, elimina el elemento más antiguo.

        Args:
            dato: El valor a insertar en el montículo. Debe ser un valor válido (comparable entre si)
        """
        reg = Registro(dato)
        
        if self.__cola_mont.tamano + 1 > self.__ventana:
            reg_elim = self.__cola_mont.eliminar()
            if reg_elim.tipo_mont == 'min':
                self.__mont_min.eliminar(reg_elim)
            else:
                self.__mont_max.eliminar(reg_elim)

        self.__cola_mont.insertar(reg)

        if self.mediana is None:
            self.__mont_max.insertar(reg)
            self.__actualizar_mediana()
            reg.tipo_mont = 'max'
        elif reg.dato > self.mediana:
            reg.tipo_mont = 'min'
            self.__mont_min.insertar(reg)
        else:
            reg.tipo_mont = 'max'
            self.__mont_max.insertar(reg)

        self.__rebalancer_monticulo()

        self.__actualizar_mediana()

    def __rebalancer_monticulo(self):
        """
        Rebalancea los montículos de máximo y mínimo para mantener la propiedad de mediana móvil.   
        """
        if self.__mont_max.tamano_actual > self.__mont_min.tamano_actual + 1:
            raiz = self.__mont_max.eliminar_raiz()
            raiz.tipo_mont = 'min'
            self.__mont_min.insertar(raiz)
        elif self.__mont_min.tamano_actual > self.__mont_max.tamano_actual + 1:
            raiz = self.__mont_min.eliminar_raiz()
            raiz.tipo_mont = 'max'
            self.__mont_max.insertar(raiz)

    def __actualizar_mediana(self):   
        """
        Actualiza el valor de la mediana en función de los montículos de máximo y mínimo.
        """     
        if self.__mont_max.tamano_actual == self.__mont_min.tamano_actual:
            self.__mediana = (self.__mont_max.obtener_raiz().dato / 2) + (self.__mont_min.obtener_raiz().dato / 2)
        elif self.__mont_max.tamano_actual > self.__mont_min.tamano_actual:
            self.__mediana = self.__mont_max.obtener_raiz().dato
        else:
            self.__mediana = self.__mont_min.obtener_raiz().dato

    def __len__(self):
        return self.__mont_max.tamano_actual + self.__mont_min.tamano_actual
    
    def __str__(self):
        return str(self.__mont_max) + str(self.__mont_min)

if __name__ == '__main__':
    monticulo = MonticuloMediana(5)

    monticulo.construir_monticulo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Mediana: ", monticulo.mediana)
    print("Monticulos: ", monticulo)

    try:
        monticulo.mediana = 4
    except Exception as e:
        print(e)


