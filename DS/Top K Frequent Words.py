#https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))
        return sorted_words[:k]