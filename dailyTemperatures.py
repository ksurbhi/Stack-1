class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)    
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Edge case: if the input list is None or empty, return an empty list
        if temperatures == None or len(temperatures) == 0:
            return []

        stack = []  # Stack to keep track of indices of temperatures that haven't found a warmer day yet
        result = [0] * len(temperatures)  # Initialize the result list with 0s

        # Iterate through each temperature in the list
        for i in range(len(temperatures)):
            # While the stack is not empty and the current temperature is greater than
            # the temperature at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()  # Pop the top index from the stack
                result[popped] = i - popped  # Calculate the number of days until a warmer temperature

            # Push the current index onto the stack
            stack.append(i)

        return result

 
