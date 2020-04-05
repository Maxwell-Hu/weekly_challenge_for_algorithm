class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        for i in range(0,12):
            for j in range(0,60):
                if self.count1(i) + self.count1(j) == num:
                    str_j = str(j) if j >= 10 else '0' + str(j)
                    res.append(str(i) + ':' + str_j)
        return res

    def count1(self, val: int) -> int:
        count = 0
        while val:
            val = val & (val - 1)
            count += 1
        return count

class Solution_oneline:
    def readBinaryWatch(self, num: int) -> List[str]:
        return [f'{h}:{m:02d}' for h in range(0,12) for m in range(0,60) \
                if (bin(h)+bin(m)).count('1') == num]
