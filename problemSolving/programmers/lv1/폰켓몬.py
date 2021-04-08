def solution(nums):
    set_size = len(set(nums))
    size = len(nums)//2
    if size >= set_size:
        return set_size
    else:
        return size