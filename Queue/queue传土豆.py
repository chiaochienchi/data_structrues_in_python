from Queue.queue import Queue


def hotpotato(namelist, number):
    q = Queue()
    for name in namelist:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()
