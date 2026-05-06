class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # dic
        anagram_dup = set()
        for st in strs:
            temp_counter = Counter(st)
            result[tuple(sorted(temp_counter.items()))].append(st)
        return list(result.values())
