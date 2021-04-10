class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = 0;
        y = 0;
        mul = 1;

        current = l1
        while current:
            x += (current.val) * mul
            mul *= 10
            current = current.next

        mul = 1
        current = l2
        while current:
            y += (current.val) * mul
            mul *= 10
            current = current.next

        z = x + y

        ans_head = ListNode(z % 10);
        z //= 10
        current = ans_head

        while z:
            new_node = ListNode(z % 10)
            current.next = new_node
            current = current.next
            z = z // 10

        return ans_head