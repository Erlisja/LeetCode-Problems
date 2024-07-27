"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(self,nums:list [int]) -> bool:
    # Create an empty hash set to store the values of the array
    hash_set = set()
    # iterate through the array
    for num in nums:
        # check if the num is already in the set
        if num in hash_set:
            # return true because we found a duplicate
            return True
        else:
            # add num to the set
            hash_set.add(num)
    # no duplicates were found, return false
    return False
