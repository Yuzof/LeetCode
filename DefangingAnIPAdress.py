class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))

A = Solution()
print(A.defangIPaddr(address = "255.100.50.0"))