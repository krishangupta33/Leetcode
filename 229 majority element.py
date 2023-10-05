class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        a=len(nums)//3
        b=[]
        for i in set(nums):
            if nums.count(i)>a:
                b.append(i)
        return b
    
obj=Solution()
print(obj.majorityElement([3,2,3]))

    