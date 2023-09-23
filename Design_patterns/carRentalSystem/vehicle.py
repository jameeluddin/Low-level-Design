nums = [-4, -1, 0, 3, 10]


def sorted_array(nums):
    left = 0
    right = len(nums) - 1
    idx = len(nums) - 1

    arr = [0 for x in nums]

    while idx >= 0:
        val1 = nums[left] * nums[left]
        val2 = nums[right] * nums[right]

        if val1 > val2:
            arr[idx] = val1
            left+=1
        else:
            arr[idx] = val2
            right-=1

        idx -= 1

    return arr

print(sorted_array(nums))

