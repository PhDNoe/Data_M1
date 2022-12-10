class Estructura_Pila(object):
    def __init__(self):
        self.__list = []

    # Agregar un elemento a la Pila
    def push(self, item):
        self.__list.append(item)

    # Quitar un elemento de la Pila
    def pop(self):
        return self.__list.pop()

# Obtener el elemento superior de la pila
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    # Determinar si la Pila está vacía
    def is_empty(self):
        return self.__list == []

    # Devuelve el número de elementos en la Pila
    def size(self):
        return len(self.__list)