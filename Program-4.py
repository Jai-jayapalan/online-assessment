'''Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]'''

def count_multiples(nums):
    multiples = {i: 0 for i in range(1, 10)}
    for n in nums:
        for i in range(1, 10):
            if n % i == 0:
                multiples[i] += 1
    return multiples


# Taking input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Output:", count_multiples(nums))