def solution(numbers, target):
    
    
    answer = 0
    def solve(cur_sum, cur_idx):
        nonlocal answer
        
        if cur_idx ==len(numbers):
            if cur_sum == target:
                answer +=1
            return
        
        solve(cur_sum+numbers[cur_idx], cur_idx+1)
        solve(cur_sum-numbers[cur_idx], cur_idx+1)
        
    
    solve(0, 0)
        
    
    
    return answer