class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def findValidNeighbors(word):
            neighbors = []
        
            for index, char in enumerate(list(word)):
                for asci in range(97, 123):
                    nextWord = list(word)
                    if ord(char) == asci:
                        continue
                    else:
                        char = chr(asci)
                        nextWord[index] = char
                        nextWord = "".join(nextWord)
                        if nextWord in wordList:
                            neighbors.append(nextWord)
            
            return neighbors

        queue = collections.deque([(beginWord, 1)])
        seen = {beginWord}
        wordList = set(wordList)                     # Convert wordList to a set for faster lookup

        while queue:
            currentWord, count = queue.popleft()

            if currentWord == endWord:
                return count

            for neighbor in findValidNeighbors(currentWord):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, count + 1))

        return 0
