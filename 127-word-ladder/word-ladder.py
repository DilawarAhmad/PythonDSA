class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord,1)])
        while queue:
            word , step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in words:
                        queue.append((newWord,step+1))
                        words.remove(newWord)
        return 0
        