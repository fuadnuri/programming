# bruteforce
# complexity O(n^2)
def two_sum_algo1(nums,target):
    for i in range(len(nums)-1):
        first_num = nums[i]
        for j in range(i+1,len(nums)):
            second_num = nums[j]
            if first_num + second_num == target:
                return (first_num,second_num)

    return -1


# complexity time o(nlog(n)) space o(n)
def two_sum_algo2(nums: list,target: int):
    nums: list = sorted(nums)
    left_pointer: int = 0
    right_pointer: int = len(nums)-1

    while left_pointer != right_pointer:
        sums: int = nums[left_pointer] + nums[right_pointer]
        if sums == target:
            return nums[left_pointer], nums[right_pointer]
        if sums > target:
            right_pointer -= 1
        else:
            left_pointer += 1
    return -1

# complexity time O(n) space O(n)
def two_sum_algo3(nums: list, target: int):
    nums_dict: dict = {}

    for i in range(len(nums)):
        n = target - nums[i]
        if nums_dict.get(n) is None:
            nums_dict[nums[i]] = True
        else:
            return nums[i], n

    return -1

print(two_sum_algo1([3,5,-4,8,11,1,-1,6],10))
print(two_sum_algo2([3,5,-4,8,11,1,-1,6],10))
print(two_sum_algo3([3,5,-4,8,11,1,-1,6],10))
