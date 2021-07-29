class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __print_all__(self):
        while self:
            print(self.val, end=' ')
            self = self.next

head = ListNode(1, ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
# def test(head):
#     tmp1 = tmp2 = head
#     tmp2.val = 7
#     tmp1.val = 8
#     print(tmp1, tmp2)

# test(head)

#
#
# test = [1,2,3,4,5]
# l1 = l2 = test
# l2[0] = 7
# print(l1,l2)
#
# test = [1,2,3,4,5]
# l2 = test
# l1 = l2
# l1[0] = 7
# print(l1,l2)

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         odd_head = odd_cur = head
#         even_head = even_cur = head.next
#         while odd_cur.next and even_cur.next:
#             odd_cur.next = even_cur.next
#             odd_cur = odd_cur.next
#
#             even_cur.next = odd_cur.next
#             even_cur = even_cur.next
#             print('odd_cur', odd_cur.__print_all__())
#             if even_cur:
#                 print('even_cur', even_cur.__print_all__())
#             print('odd', odd_head.__print_all__())
#             print('even', even_head.__print_all__())
#             print('head', head.__print_all__())
#
#         print('odd_head', odd_head.__print_all__())
#         odd_cur.next = even_head
#         odd_head.__print_all__()
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            even = even.next
            odd = odd.next
        odd.next = even_head
        return head
tmp = Solution
print(tmp.oddEvenList(head, head))