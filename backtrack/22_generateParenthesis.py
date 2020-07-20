class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(track):
            if track.count('(') == n and track.count(')') == n:
                if track not in res: res.append(track)
                return
            if track.count(')') > track.count('('):
                return
            
            if track.count('(')<n:backtrack(track+'(')
            if track.count(')')<n:backtrack(track+')')

        res = []
        backtrack('')
        return res
