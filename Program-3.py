'''With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]'''

def generate_odd_sequence(max_value):
    odd_numbers = []
    count = max_value if max_value % 2 == 1 else max_value - 1
    
    for i in range(count):
        odd_numbers.append(str(2 * i + 1))
    
    return odd_numbers

user_input = int(input("Enter a number: "))
result_sequence = generate_odd_sequence(user_input)
print("Output:", ", ".join(result_sequence))