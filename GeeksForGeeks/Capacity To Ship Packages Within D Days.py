class Solution:
    def leastWeightCapacity(self, n, d, arr):
        def canShip(capacity):
            days_needed = 1
            current_weight = 0

            for weight in arr:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = 0

                current_weight += weight
                if days_needed > d:
                    return False
            return True

        left = max(arr)  # Minimum possible capacity
        right = max(arr)  # Maximum possible capacity
        result = right

        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                result = mid
                right = mid - 1  # Try for a smaller capacity
            else:
                left = mid + 1  # Increase the capacity

        return result


# Test case
n = 3
arr = [1, 2, 1]
d = 2
s = Solution()
print(s.leastWeightCapacity(n, d, arr))
