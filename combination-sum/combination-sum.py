class Solution:
    def explore(self, subset, start, candidates, target):
        if target < 0:
            return
        
        elif target == 0:
            self.result.append(subset)
            return
        
        for i in range(start, len(candidates)):
            self.explore(subset + [candidates[i]], i, candidates, target-candidates[i])
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        subset = []
        self.explore(subset, 0, candidates, target)
        return self.result
    
            
            
        
        