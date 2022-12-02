class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushNodeIntoHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pushNodeIntoLast(self, data):
        new_node = Node(data)
        temp = self.head

        if self.head is None:
            self.head = new_node
            return

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def pushNodeAfterNode(self, prev_node, new_data):
        new_node = Node(new_data)

        if prev_node is None:
            print('This node does not existed in linked list')
            return

        new_node.next = prev_node.next

        prev_node.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if self.head is None:
            print('This node does not existed in linked list')
            return

        if temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp is not None:
            prev = temp
            temp = temp.next

            if temp.data == key:
                prev.next = temp.next
                temp = None
                break

    def calculateLength(self):
        temp = self.head
        llist_length = 0

        if self.head is None:
            print('The linked list length is 0')
            return

        while temp is not None:
            temp = temp.next
            llist_length += 1

        print(f'The linked list length is {llist_length}')

    def search_node(self, key):
        temp = self.head

        if self.head is None:
            print('The linked list is empty')
            return

        while temp is not None:
            if temp.data == key:
                print('Found it')
                return True

            temp = temp.next

        print('Not found')
        return False

    def reverseLinkedList(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.pushNodeIntoHead(5)
    llist.pushNodeIntoHead(8)
    llist.pushNodeIntoLast(7)
    llist.pushNodeAfterNode(llist.head.next, 6)
    llist.deleteNode(8)
    llist.calculateLength()
    llist.search_node(5)
    llist.reverseLinkedList()
    llist.printLinkedList()
