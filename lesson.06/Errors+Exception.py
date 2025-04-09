# the last you write the first you get
# def compute():
#     number = int(input("Enter number: "))  # Convert input to integer
#     result = number * 2  # Example operation
#     return result  # Return the computed result

# # Call the function and store the result
# answer = compute()

# # Print the result
# print(f"The answer is {answer}")
def compute(n1, n2):
    answer = n1 / n2

    return answer




user_input_1 = input("Enter a number: ")

user_input_2 = input("Enter another number: ")

num1 = int(user_input_1)

num2 = int(user_input_2)

answer = compute(num1, num2)

print(f"{num1} / {num2} = {answer}")
