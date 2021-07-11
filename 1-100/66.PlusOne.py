class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)

        result = [int(i) for i in str(int(num)+1)]

        for i in range(len(digits)):
            if digits[i] > 0:
                break

            if digits[i] == 0 and i != len(digits)-1:
                result.insert(0, 0)

        return result
