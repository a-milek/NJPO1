# Dla # k kolejek zaimplementuj karuzelowy algorytm przydziału zadań. Przykładowo dla trzech kolejek:
# ABC
# DE
# F
# Zostaną obsłużone zadania wg. kolejności: ADFBEC.
from collections import deque


def carousel(q_list):
    did_nothing = False
    while not did_nothing:
        did_nothing = True
        for queue in q_list:
            if len(queue) != 0:
                print(queue[0])
                queue.popleft()
                did_nothing = False


if __name__ == '__main__':
    q1 = deque(['A', 'B', 'C'])
    q2 = deque(['D', 'E'])
    q3 = deque(['F'])
    queued_list = [q1, q2, q3]
    carousel(queued_list)
