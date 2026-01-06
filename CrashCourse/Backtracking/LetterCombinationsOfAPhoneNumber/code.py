class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        answer = []
        if not digits:
            return answer

        def backtrack(curr, i):
            if i == len(digits):
                answer.append("".join(curr[:]))
                return

            for char in mapping[int(digits[i])]:
                curr.append(char)
                backtrack(curr, i + 1)
                curr.pop()

        mapping = collections.defaultdict(list)

        letter = 97
        for digit in range(2, 9 + 1):
            mapping[digit] = [chr(letter), chr(letter + 1), chr(letter + 2)]
            letter += 3
            
            if digit in [7, 9]:
                mapping[digit].append(chr(letter))
                letter += 1
        
        #print(mapping)
        backtrack([], 0)

        return answer
