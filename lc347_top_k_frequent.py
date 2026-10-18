# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         k_map = {}
#         for i, num in enumerate(nums):
#             k_map[num] = k_map.get(num, 0) + 1
        
#         sorted_nums = sorted(k_map.items(), key=lambda x:x[1], reverse=True)
#         k_freq = []
#         for i in range(k):
#             k_freq.append(sorted_nums[i][0])
        
#         return k_freq
    

# nums = [1,3, 4, 2,1, 4, 2, 1, 1]
# k = 2

# sol = Solution()
# print(sol.topKFrequent(nums, k))



class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        k_map = {}
        for i, num in enumerate(nums):
            k_map[num] = k_map.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums))]
        for key, v in k_map.items():
            buckets[v-1].append(key)

        k_freq = []
        k_freq_added_count = 0
        for _, bucket in enumerate(reversed(buckets)):
            if bucket:
                for _, ele in enumerate(bucket):
                    k_freq.append(ele)
                    k_freq_added_count += 1
                    if k_freq_added_count == k:
                        break
                if k_freq_added_count == k:
                    break   
        return k_freq 
        

nums = [1]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))