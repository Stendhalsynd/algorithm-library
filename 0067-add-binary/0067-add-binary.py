class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # result = bin(int(a, 2) + int(b, 2))
        # return result[2:]

        int_a = int(a, 2)
        int_b = int(b, 2)

        def addBin(int_a, int_b):
            if int_b == 0: return int_a

            sum_bit = int_a ^ int_b # xor : 둘중 하나에만 포함된 원소
            carry = (int_a & int_b) << 1 # 둘다 포함된 원소들 집합을 1bit 만큼 left shift
            return addBin(sum_bit, carry)

        return bin(addBin(int_a, int_b))[2:]