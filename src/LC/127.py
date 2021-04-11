from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = collections.deque()
        queue.append(beginWord)
        visited = set(beginWord)
        step = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                wordArray = list(word)
                for j in range(len(word)):
                    originChar = wordArray[j]
                    for k in range(26):
                        wordArray[j] = chr(ord('a')+k)
                        nextWord = ''.join(wordArray)
                        if nextWord in wordSet:
                            if nextWord == endWord:
                                return step+1
                            if nextWord not in visited:
                                queue.append(nextWord)
                                visited.add(nextWord)
                    wordArray[j] = originChar
            step += 1
        return 0

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList)) # 5


