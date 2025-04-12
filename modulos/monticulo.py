class Monticulo:
    def __init__(self, tipo='min'):
        self.lista_monticulo = [None]
        self.tamano_actual = 0
        self.__tipo = tipo #por defecto es de min
    
    def infilt_arriba(self, i):
        """
        Sube el elemento en la posición i hacia arriba en el montículo,
        asegurando que se mantenga la propiedad del montículo.

        Args:
            i: Índice del elemento a subir.
        """
        while i // 2 > 0:
            if self.__tipo == 'min':
                if self.lista_monticulo[i] < self.lista_monticulo[i // 2]:
                    self.lista_monticulo[i // 2], self.lista_monticulo[i] = self.lista_monticulo[i], self.lista_monticulo[i // 2]
                    self.lista_monticulo[i // 2].indice = i // 2
                    self.lista_monticulo[i].indice = i
            else:
                if self.lista_monticulo[i] > self.lista_monticulo[i // 2]:
                    self.lista_monticulo[i // 2], self.lista_monticulo[i] = self.lista_monticulo[i], self.lista_monticulo[i // 2]
                    self.lista_monticulo[i // 2].indice = i // 2
                    self.lista_monticulo[i].indice = i
            i = i // 2
        return i

    def insertar(self, reg):
        """
        Inserta un nuevo elemento en el montículo y lo coloca en la posición correcta.

        Args: 
            reg: Registro a insertar en el montículo.
        """
        self.lista_monticulo.append(reg)
        self.tamano_actual += 1
        reg.indice = self.tamano_actual
        self.infilt_arriba(self.tamano_actual)
        
    def infilt_abajo(self, i):
        """
        Baja el elemento en la posición i hacia abajo en el montículo,
        asegurando que se mantenga la propiedad del montículo.

        Args: 
            i: Índice del elemento a bajar.
        """
        while (i * 2) <= self.tamano_actual:
            h = self.hijo(i)
            if self.__tipo == 'min':
                if self.lista_monticulo[i] > self.lista_monticulo[h]:
                    self.lista_monticulo[i], self.lista_monticulo[h] = self.lista_monticulo[h], self.lista_monticulo[i]
                    self.lista_monticulo[i].indice = i
                    self.lista_monticulo[h].indice = h
            else:
                if self.lista_monticulo[i] < self.lista_monticulo[h]:
                    self.lista_monticulo[i], self.lista_monticulo[h] = self.lista_monticulo[h], self.lista_monticulo[i]
                    self.lista_monticulo[i].indice = i
                    self.lista_monticulo[h].indice = h
            i = h

    def hijo(self, i):
        """
        Devuelve el índice del hijo del elemento en la posición i.

        Args:
            i: Índice del elemento padre.
        """
        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.__tipo == 'min': #tipo de monticulo: min - hijo min
                if self.lista_monticulo[i * 2] < self.lista_monticulo[i * 2 + 1]:
                    return i * 2
                else:
                    return i * 2 + 1
            # elif self.__tipo == 'max': #tipo de monticulo: max - hijo max
            else:
                if self.lista_monticulo[i * 2] > self.lista_monticulo[i * 2 + 1]:
                    return i * 2
                else:
                    return i * 2 + 1

    def eliminar_raiz(self):
        """
        Elimina la raíz del montículo y devuelve su valor.
        """
        valor_sacado = self.lista_monticulo[1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.lista_monticulo[1].indice = 1
        self.tamano_actual -= 1
        self.lista_monticulo.pop()
        self.infilt_abajo(1)
        return valor_sacado
    
    def eliminar(self, reg):
        """
        Elimina un elemento en una posición arbitraria del montículo y devuelve su valor.

        Args:
            reg: Registro a eliminar del montículo.
        """
        i = reg.indice
        valor_sacado = self.lista_monticulo[i]
        if i == self.tamano_actual:
            self.lista_monticulo.pop()
            self.tamano_actual -= 1
            return valor_sacado
        else:
            self.lista_monticulo[i] = self.lista_monticulo[self.tamano_actual]
            self.lista_monticulo[i].indice = i
            self.tamano_actual -= 1
            self.lista_monticulo.pop()
            self.infilt_arriba(i)
            self.infilt_abajo(i)
            return valor_sacado
        
    def eliminar_insertar(self, i, nuevo_reg):
        """
        Elimina un elemento en una posición arbitraria del montículo y lo reemplaza por un nuevo registro.

        Args:
            i: Índice del elemento a eliminar.
            nuevo_reg: Registro a insertar en el montículo.
        """
        valor_sacado = self.lista_monticulo[i]
        self.lista_monticulo[i] = nuevo_reg
        nuevo_reg.indice = i
        self.infilt_arriba(i)
        self.infilt_abajo(i)
        return valor_sacado
    
    def obtener_raiz(self):
        """
        Devuelve el valor de la raíz del montículo sin eliminarla.
        """
        return self.lista_monticulo[1]
    
    def __str__(self):
        return str([self.lista_monticulo[i].dato for i in range(1, self.tamano_actual + 1)])
