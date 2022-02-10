class Solution:
    import heapq
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3
        left_heap = []
        cur_sum = 0
        for i in range(n):
            heapq.heappush(left_heap, -nums[i])
            cur_sum+=nums[i]
        left_sums=[cur_sum]
        
        right_heap = []
        cur_sum = 0
        for i in range(2*n, 3*n):
            heapq.heappush(right_heap, nums[i])
            cur_sum+=nums[i]
        right_sums=[cur_sum]      
        
        for i in range(n,2*n):
            pop = heapq.heappushpop(left_heap, -nums[i])
            left_sums.append(left_sums[-1] + nums[i] + pop)
        
        for i in range(2*n-1,n-1,-1):
            pop = heapq.heappushpop(right_heap, nums[i])
            right_sums.append(right_sums[-1] + nums[i] - pop)
            
        return min(left_sums[i]-right_sums[n-i] for i in range(n+1))
