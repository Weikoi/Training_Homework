import random
import time


class Node(object):
    def __init__(self, count):
        self.num = random.randint(0, 100)
        self.count = count
        self.next = None

    def __repr__(self):
        return str([self.num, self.count])


def main(target_time):
    queue = []
    hash_map = {}
    time_count = 0
    while True:
        new_item = Node(time_count)
        if new_item.num not in hash_map:
            queue.append(new_item.num)
            hash_map[new_item.num] = queue.index(new_item.num)

        else:
            queue.remove(new_item.num)
            queue.append(new_item.num)
        time_count += 1
        if len(queue) > 60:
            hash_map.pop(queue[0])
            queue.pop(0)

        if new_item.count == target_time:
            print(queue)


if __name__ == '__main__':
    main(30)
