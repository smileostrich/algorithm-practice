class ListNode:
    data = 0
    prev = None
    next = None

    def __init__(self):
        self.data = 0
        self.prev = self
        self.next = self

    def appendListNode(head, data):
        node = ListNode()
        node.data = data
        if head == None:
            head = node
        else:
            last = head.prev
            last.next = node
            head.prev = node
            node.prev = last
            node.next = head
        return head

    def removeListNode(head, node):
        if head == head.next:
            return None
        else:
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            if head == node:
                return nextNode
            else:
                return head


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        data = list(map(int, input().split()))
        head = None
        for i in range(N):
            head = ListNode.appendListNode(head, data[i])

        node = head
        while head != head.next:
            nextNode = node.next
            head = ListNode.removeListNode(head, node)
            node = nextNode.next.next

        print("#%d %d" % (test_case, head.data))


if __name__ == "__main__":
    main()