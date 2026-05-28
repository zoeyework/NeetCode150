class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      seem = {}
      for num in nums:
       seem[num] = seem.get(num, 0) + 1
       print(seem)
      buckets = [[] for _ in range(len(nums) + 1)]
      print(buckets)
      for num, freq in seem.items():
          buckets[freq].append(num)
      print(buckets)
      res = []
      for i in range(len(buckets) - 1, 0, -1):  
          for num in buckets[i]:
              res.append(num)
              if len(res) == k:  
                  return res
