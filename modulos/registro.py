class Registro:
    def __init__(self, dato, indice=None, tipo_mont=None):
        """
        Inicializa un registro con un dato, un índice y un tipo de montículo (max o min).
        """
        self.dato = dato
        self.indice = indice
        self.tipo_mont = tipo_mont # max o min
        self.siguiente = None

    def __lt__(self, otro):
        """
        Compara dos registros basándose en su dato.
        """
        if self.dato < otro.dato:
            return True
        return False




