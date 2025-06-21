class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        print(f'Your linked list for n = {n}:')
        current = self.head
        llist = []
        while current:
            llist.append(str(current.data))
            current = current.next
        llist.append(str(current))
        llist = " -> ".join(llist)
        print(llist)

    def get_elem(self):
        n = 0
        current = self.head
        while current:
            n += 1
            current = current.next

        if n <= 1:
            return None
        else:
            pos = int(2*n/3) - 1
            current = self.head
            for i in range(pos):
                if current is not None:
                    current = current.next

            return current.data


def main():
    linked_list = LinkedList()
    n = 3

    for i in range(n):
        linked_list.append(i)

    linked_list.print_list()
    if linked_list.get_elem() is None:
        print("\nn <=1, you get null")
    else:
        print(f'\nElement [2*n/3]-1: {linked_list.get_elem()}')


if __name__ == '__main__':
    main()