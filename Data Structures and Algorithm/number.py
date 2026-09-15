def contains_duplicate(nums):
    new_nums = set()

    for number in nums:
        if number in new_nums:
            return True
        else:
            new_nums.add(number)
    print(new_nums)
    return False

print(contains_duplicate([1,2,4,5,2,1,4]))