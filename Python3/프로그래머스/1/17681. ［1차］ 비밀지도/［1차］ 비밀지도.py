def get_binary(num, n): 
    tmp = ""
    if num == 0:
        return '0' * n
    
    while num > 0:
        tmp = str(num % 2) + tmp
        num //= 2
    
    sup = n - len(tmp)
    tmp = '0' * sup + tmp
    return tmp

def solution(n, arr1, arr2):
    answer = []
    
    arr11 = []
    for ele1 in arr1:
        arr11.append(get_binary(ele1, n))
        
    arr22 = []
    for ele2 in arr2:
        arr22.append(get_binary(ele2, n))
    
    for i in range(n):
        row_str = "" 
        for j in range(n):
            bit_or = int(arr11[i][j]) | int(arr22[i][j])
            
            if bit_or == 1:
                row_str += "#"
            else:
                row_str += " "
        
        answer.append(row_str)
        
    return answer