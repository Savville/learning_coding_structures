def two_sum_brute_force(nums, target):
    """
    Brute force approach
    
    Time Complexity: O(n²) - nested loops iterate through all pairs
    Space Complexity: O(1) - only uses constant extra space
    
    Explanation:
    - Outer loop runs n times
    - Inner loop runs (n-1) + (n-2) + ... + 1 = n(n-1)/2 times total
    - This gives us O(n²) time complexity
    - No additional data structures used, so O(1) space
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # Return indices
                # Or return [nums[i], nums[j]] for values
    return None  # No solution found

def two_sum_hash_map(nums, target):
    """
    Hash map approach
    
    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(n) - hash map stores up to n elements
    
    Explanation:
    - Single loop through n elements: O(n)
    - Hash map lookup and insertion are O(1) on average
    - Hash map can store up to n key-value pairs in worst case
    - Most efficient solution for time complexity
    """
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]  # Return indices
            # Or return [complement, num] for values
        num_to_index[num] = i
    
    return None  # No solution found

def two_sum_sorted(nums, target):
    """
    Two pointer approach (requires sorting)
    
    Time Complexity: O(n log n) - dominated by sorting step
    Space Complexity: O(n) - for storing indexed pairs
    
    Explanation:
    - Creating indexed pairs: O(n)
    - Sorting the pairs: O(n log n) 
    - Two pointer traversal: O(n)
    - Total: O(n log n) due to sorting
    - Space: O(n) for the indexed_nums list
    - Good when you don't need to preserve original indices
    """
    # Create pairs of (value, original_index) to preserve indices
    indexed_nums = [(nums[i], i) for i in range(len(nums))]
    indexed_nums.sort()  # Sort by value
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None  # No solution found

# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9),      # Expected: [0, 1] (2 + 7 = 9)
        ([3, 2, 4], 6),           # Expected: [1, 2] (2 + 4 = 6)
        ([3, 3], 6),              # Expected: [0, 1] (3 + 3 = 6)
        ([1, 2, 3, 4, 5], 8),     # Expected: [2, 4] (3 + 5 = 8)
        ([1, 2, 3, 4, 5], 10),    # Expected: None (no solution)
    ]
    
    for i, (nums, target) in enumerate(test_cases):
        print(f"Test case {i + 1}: nums = {nums}, target = {target}")
        
        # Test all three approaches
        result1 = two_sum_brute_force(nums, target)
        result2 = two_sum_hash_map(nums, target)
        result3 = two_sum_sorted(nums, target)
        
        print(f"  Brute force: {result1}")
        print(f"  Hash map:    {result2}")
        print(f"  Two pointer: {result3}")
        
        # Verify results (sort indices for comparison since order might differ)
        if result1: result1.sort()
        if result2: result2.sort()
        if result3: result3.sort()
        
        print(f"  All match:   {result1 == result2 == result3}")
        print()

# Additional utility function to return values instead of indices
def two_sum_values(nums, target):
    """
    Returns the actual values that sum to target, not indices
    
    Time Complexity: O(n) - two passes through the array
    Space Complexity: O(n) - hash map stores unique elements
    
    Explanation:
    - First loop to count occurrences: O(n)
    - Second loop to find complement: O(n) worst case
    - Hash map operations are O(1) on average
    - Space used by hash map depends on number of unique elements
    """
    num_to_count = {}
    
    # Count occurrences of each number
    for num in nums:
        num_to_count[num] = num_to_count.get(num, 0) + 1
    
    for num in nums:
        complement = target - num
        
        # Check if complement exists
        if complement in num_to_count:
            # If it's the same number, make sure we have at least 2 of them
            if complement == num and num_to_count[num] < 2:
                continue
            return [num, complement]
    
    return None


"""
COMPLEXITY ANALYSIS SUMMARY:

Method                | Time Complexity | Space Complexity | Best Use Case
---------------------|-----------------|------------------|------------------
two_sum_brute_force  | O(n²)          | O(1)            | Small arrays, no extra memory
two_sum_hash_map     | O(n)           | O(n)            | General case, fastest solution
two_sum_sorted       | O(n log n)     | O(n)            | When sorting is acceptable
two_sum_values       | O(n)           | O(n)            | When you need values, not indices

TRADE-OFFS:
- Hash map approach is usually the best choice for most scenarios
- Brute force is good for very small arrays or when memory is extremely limited
- Sorted approach is useful when the array can be modified or when you need sorted output
- All approaches handle duplicate numbers correctly

PERFORMANCE COMPARISON (for array of size n):
- Brute Force: ~n²/2 operations, minimal memory
- Hash Map: ~n operations, up to n memory slots
- Sorted: ~n log n operations (sorting dominates), n memory slots
"""