class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        lo, hi, score = 0, len(tokens) - 1, 0
        while(lo < hi):
            if tokens[lo] <= power:
                power -= tokens[lo]
                score += 1
                lo += 1
            elif score:
                power += tokens[hi]
                score -= 1
                hi -= 1
            else:   break
        
        return score + 1 if lo == hi and tokens[lo] <= power else score