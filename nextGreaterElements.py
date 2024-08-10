class Solution:
    """
    Time Complexity: O(N)
    We iterate through the array twice (2 * N), but each element is pushed and popped from the stack at most once.
    Thus, the overall time complexity is O(N)
    Space Complexity: O(N), The space complexity is O(N) due to the stack.
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        stack = []  # Stack to store indices of the elements
        result = [-1] * len(nums)  # Initialize result array with -1s

        # Iterate through the array twice to simulate the circular nature
        for i in range(2 * len(nums)):
            # Use modulo to wrap around the index when i >= len(nums)
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                popped = stack.pop()  # Pop the top element from the stack
                result[popped] = nums[i % len(nums)]  # Set the next greater element in the result array

            # Push the index onto the stack only for the first pass (i < len(nums))
            if i < len(nums):
                stack.append(i)
        
        return result
