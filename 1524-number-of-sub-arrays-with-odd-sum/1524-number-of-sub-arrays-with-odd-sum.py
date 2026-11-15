class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        # An empty prefix has a sum of 0, which is even.
        even_count = 1
        odd_count = 0
        
        prefix_sum = 0
        total_odd_subarrays = 0
        
        for num in arr:
            prefix_sum += num
            
            # If the current prefix sum is ODD:
            # Subtracting any previous EVEN prefix sum gives an ODD subarray sum.
            if prefix_sum % 2 == 1:
                total_odd_subarrays = (total_odd_subarrays + even_count) % MOD
                odd_count += 1
                
            # If the current prefix sum is EVEN:
            # Subtracting any previous ODD prefix sum gives an ODD subarray sum.
            else:
                total_odd_subarrays = (total_odd_subarrays + odd_count) % MOD
                even_count += 1
                
        return total_odd_subarrays