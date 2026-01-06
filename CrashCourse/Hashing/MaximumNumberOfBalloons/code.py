class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = defaultdict(int)
        
        for char in text:
            if char == "b":
                balloonCounter["b"] += 1
            
            if char == "a":
                balloonCounter["a"] += 1    
            
            if char == "l":
                balloonCounter["l"] += 1
            
            if char == "o":
                balloonCounter["o"] += 1
            
            if char == "n":
                balloonCounter["n"] += 1
                
        answer = min(balloonCounter["b"],
                               balloonCounter["a"],
                               balloonCounter["l"] // 2,
                               balloonCounter["o"] // 2,
                               balloonCounter["n"]) 
        if answer >= 1:
            return answer
        
        return 0
                   
