class Solution(object):
    def twoSum(self, nums, target):
        """
        #array of ints nums =[]
        #int = target 
        #num1 + num 2 = target
        use hashMap
            - key/target = lookup value in the table
            - value =  index where number appears 
        """
        seen =  {}
        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return[seen[needed],i]

            seen[num] = i