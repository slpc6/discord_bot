"""Clase que implementa una cola de reproducción de audio"""

#External libraries
from collections import deque

class AudioQueue:
    """Clase que implementa una cola de reproducción de audio"""

    def __init__(self):
        """Inicializa la cola de reproducción"""
        self.queue = deque()


    def add(self, item):
        """Agrega un elemento a la cola
        args:
            item: str - Elemento a agregar

        """
        self.queue.append(item)


    def pop(self):
        """Extrae y devuelve el primer elemento de la cola
        returns:
            str - Elemento extraído
            
        """
        return self.queue.popleft()


    def get_queue(self):
        """Devuelve una lista con los elementos de la cola
        returns:
            list - Elementos de la cola

        """
        return list(self.queue)


    def is_empty(self):
        """Verifica si la cola está vacía
        returns:
            bool - True si la cola está vacía, False en caso contrario

        """
        return len(self.queue) == 0
    