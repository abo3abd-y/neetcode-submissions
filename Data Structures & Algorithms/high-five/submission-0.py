class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        heap = []
        for i in range(len(items)):
            heap.append((items[i][0], -items[i][1]))
        heapq.heapify(heap)
        final_answer = []
        print(heap)
        while len(heap) >= 5:
            curr_id = heap[0][0]
            print(heap[0])
            average = sum(-heapq.heappop(heap)[1] for _ in range(5))//5
            while heap and heap[0][0] == curr_id : heapq.heappop(heap)
            final_answer.append([curr_id, average])
        return final_answer