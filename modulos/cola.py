class Cola:
    def __init__(self):
        """
        Inicializa una cola vacía.
        """
        self.primero = None
        self.ultimo = None
        self.tamano = 0
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        """
        return self.primero is None
    
    def insertar(self, reg):
        """
        Inserta un nuevo elemento al final de la cola.
        
        Args:
            reg: Registro a insertar en la cola.
        """
        if self.esta_vacia():
            self.primero = reg
            self.ultimo = reg
        else:
            self.ultimo.siguiente = reg
            self.ultimo = reg
        
        self.tamano += 1
    
    def eliminar(self):
        """
        Elimina el primer elemento de la cola y lo devuelve.
        """
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        
        valor_eliminado = self.primero
        self.primero = self.primero.siguiente
        
        # Si al eliminar, la cola queda vacía
        if self.primero is None:
            self.ultimo = None
        
        self.tamano -= 1
        return valor_eliminado
    
    def obtener_primero(self):
        """
        Devuelve el primer elemento de la cola sin eliminarlo.
        """
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        
        return self.primero.dato
    
    def obtener_ultimo(self):
        """
        Devuelve el último elemento de la cola sin eliminarlo.
        """
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
                
        return self.ultimo.dato
    
    def __str__(self):
        if self.esta_vacia():
            return "Cola vacía"
        
        elementos = []
        actual = self.primero
        while actual is not None:
            elementos.append(f'({actual.dato}, {actual.indice}, {actual.tipo_mont})')
            actual = actual.siguiente
        
        elementos.reverse()
        return " -> ".join(elementos)

