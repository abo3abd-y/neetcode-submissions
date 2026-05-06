class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        size = len(customers)
        # add base customers
        base_satisfy = sum(customers[i] for i in range(size) if grumpy[i] == 0)

        # max satisfied
        max_val = float('-inf')
        curr_max_val = sum(customers[i] for i in range(minutes-1) if grumpy[i] == 1)
        max_range = []
        for i in range(minutes-1, size):
            if grumpy[i] == 1:
                curr_max_val += customers[i]
            if curr_max_val > max_val:
                max_val = curr_max_val
                max_range = [i - minutes + 1,i + 1]
            left_idx = i + 1 - minutes
            if grumpy[left_idx] == 1:
                curr_max_val -= customers[left_idx]
            
        max_satisfy = base_satisfy + sum(customers[i] for i in range(*max_range) if grumpy[i] == 1)
        return max_satisfy
