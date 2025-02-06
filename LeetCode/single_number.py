def singleNumber(nums: list[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor