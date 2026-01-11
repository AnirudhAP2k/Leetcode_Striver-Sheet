class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def combinations(idx, comb, total):
            if target == total:
                res.append(comb[:])
                return

            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            combinations(idx, comb, total + candidates[idx])
            comb.pop()
            combinations(idx + 1, comb, total)

            return res

        return combinations(0, [], 0)