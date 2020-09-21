#순열
Size = 4
Q = [0] * Size
f, rear = 0,0
def enQueue(item): # 
    global rear
    if (rear+1) % Size == f:
        print('full')
    else:
        rear = (rear+1)%Size
        Q[rear] = item


def deQueue():
    global f
    if rear == f:
        print('Empty')
    else:
        f = (f+1)%Size
        return Q[f]


enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
print(Q)
print(deQueue())
print(deQueue())
print(deQueue())
enQueue(5)
enQueue(6)
enQueue(6)
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)