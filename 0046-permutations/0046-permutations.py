from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # 모든 경우의 순열 생성 (길이를 지정하지 않으면 전체 요소 사용)
        result = list(permutations(nums))

        return result
                


        