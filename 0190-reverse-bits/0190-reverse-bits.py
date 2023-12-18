class Solution:
    def reverseBits(self, n: int) -> int:
        string = bin(n)[2:]
        reverse_string = string[::-1]

        gap = 32 - len(reverse_string)

        if gap != 0:
            for _ in range(gap):
                reverse_string = reverse_string + '0'

        return int(reverse_string, 2)