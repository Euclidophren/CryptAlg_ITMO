def lcg_generate(nums, modulo, a, c, seed):
    result = [(a * seed + c) % modulo]
    for i in range(1, nums):
        result.append((a * result[i - 1] + c) % modulo)
    return result
