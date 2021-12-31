def solution(nums):
    res = 0
    sieve = [False, False] + [True]*2999
    
    for i in range(2, 55):
        if (sieve[i]):
            for j in range(i + i, 3001, i):
                sieve[j] = False
    
    primes = set(i for i in range(2, 3001) if (sieve[i]))
    
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if ((nums[i] + nums[j] + nums[k]) in primes):
                    res += 1

    return res