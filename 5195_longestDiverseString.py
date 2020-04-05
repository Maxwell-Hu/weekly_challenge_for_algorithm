class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a': min(a, (b+c+1)*2), 'b': min(b, (a+c+1)*2), 'c': min(c, (a+b+1)*2)}
        n = sum(d.values())
        res = []
        for i in range(n):
            candidate = set(['a', 'b', 'c'])
            if len(res)>1 and res[-1] == res[-2]:
                candidate.remove(res[-1])
            tmp = max(candidate, key=lambda x: d[x])
            res.append(tmp)
            d[tmp] -= 1
        return ''.join(res)
