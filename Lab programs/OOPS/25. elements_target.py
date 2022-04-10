class target:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target-num], i )
           lookup[num] = i
           
print("%d,%d" % target().twoSum((10,20,10,40,50,60,70),50))
