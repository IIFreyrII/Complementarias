from collections import deque

def uso_doble_cola():
    deque_doble = deque()
    deque_doble.append("Inicio") 
    deque_doble.appendleft("Primero")  
    print("Eliminando del final:", deque_doble.pop())  
    print("Eliminando del principio:", deque_doble.popleft())  

uso_doble_cola()
