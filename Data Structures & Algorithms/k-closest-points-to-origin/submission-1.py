class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            euc = math.sqrt((0 - points[i][0])**2 + (0 - points[i][1])**2)
            heap.append((euc, points[i][0], points[i][1] ))
        heapq.heapify(heap)
        final_answer = []
        for _ in range(k):
            point = heapq.heappop(heap)
            final_answer.append([point[1], point[2]])
        return final_answer

