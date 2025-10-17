from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    max_len = 0
    while len(num_set) == 0:
        cn = num_set.pop()
        # traverse downwards
        lp = cn - 1
        while lp in num_set:
            num_set.remove(lp)
            lp = cn - 1
        # lp is not inclusive
        rp = cn + 1
        while rp in num_set:
            num_set.remove(rp)
            rp = cn + 1
        max_len = max(max_len, rp - lp - 2)

        # traverse upwards
