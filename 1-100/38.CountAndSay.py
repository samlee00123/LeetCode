class Solution:
    def say(self, s: str) -> str:
        result = ""
        head = 0
        tail = head
        
        while tail != len(s):
            if s[head] == s[tail]:
                tail += 1
            else:
                result += str(tail - head) + s[head]
                head = tail
                tail += 1

        
        result += str(tail - head) + s[head]   

        s = result
        return s
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        sequence = "1"
        
        for i in range(n-1):
            sequence = self.say(sequence)

        return sequence
        
        