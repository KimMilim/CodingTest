def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
      
        combined = arr1[i] | arr2[i]
        
        # bin(9) -> '0b1001' 
        binary_str = bin(combined)[2:]

        binary_str = binary_str.zfill(n)
        
        row = binary_str.replace('1', '#').replace('0', ' ')
        answer.append(row)
        
    return answer
