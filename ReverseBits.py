class Solution:
    def reverseBits(self, n: int) -> int:
        sum = 0
        i = 31
        print(bin(n))
        for element in bin(n)[:1:-1]:
            sum += int(element) * 2 ** i
            i -= 1
        return sum

A = Solution()
print(A.reverseBits(n = 0b00000010100101000001111010011100))