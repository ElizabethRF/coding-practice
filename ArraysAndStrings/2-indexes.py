def two_sum(nums: list[int], target: int) -> list[int]:
    hm = {}  # key : expected element to target, value: position of complement
    for x in range(len(nums)):
        if nums[x] in hm:
            return [hm[nums[x]], x]
        else:
            comp = target - nums[x]
            hm[comp] = x


if __name__ == '__main__':
    tests = [
        [[2, 7, 1, 5], 9],
        [[3, -1, 0, 1], 0]
    ]
    for val, targ in tests:
        print(two_sum(val, targ))