# Q5. Get Top 2 Largest Numbers
# Write a function that returns the two largest numbers in a list.
# Example:
# top_two([1, 9, 3, 7, 5]) -&gt; [9, 7]
# Starter Code:
# def top_two(numbers):
#     sorted_numbers = sorted(numbers)
#     print(sorted_numbers[-2::])

#     return sorted_numbers
# print(top_two([1, 9, 3, 7, 5]))
# def frequency_counter(lst):
#     freq_dict = {}
#     for item in lst:
#         if item in freq_dict:
#             freq_dict[item] += 1
#         else:
#             freq_dict[item] = 1
#     return freq_dict

# print(frequency_counter(['a', 'b', 'a', 'c', 'b']))
# Q7. Safe Division
# Write a function `safe_divide(a, b)` that divides a by b, but returns &#39;Error&#39; if b is 0.
# Example:
# def safe_divide(a, b):
#     if b != 0:
#         c = a / b
#         print("a / b =", c)
#         return c
#     else:
#         print("Error")
#         return None
# safe_divide(10, 2)
# safe_divide(5, 0) 
# Q9. Check if List is Sorted
# Write a function `is_sorted(lst)` that returns True if the list is sorted in ascending order.
# Example:
# Example:

# Starter Code:
def is_sorted(lst):
    sorted_lst=sorted(lst)
    if sorted_lst ==lst:
        print("True")
    else:
        print("false")
    
is_sorted([1, 2, 3]) 
is_sorted([3, 1, 2]) 

