'''
Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
'''

def generate_series(a):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    return result

a = int(input("Enter a number: "))
series = generate_series(a)
print("Output:", ', '.join(map(str, series)))