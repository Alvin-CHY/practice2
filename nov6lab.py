'''
[1, 4, 9]
[[-1, -2, -3], [4, 5, 6], [-7, -8, -9]]
(373, 571, 510, 872)
'''
def cluster_investigation(lst):
    min_sum = sum(lst[0])
    min_index = 0
    max_sum = sum(lst[0])
    max_index = 0
    
    for i in range(1, len(lst)):
        current_sum = sum(lst[i])
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = i
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i
            
    print(f"Smallest cluster is cluster {min_index + 1} with a value of {min_sum}")
    print(f"Largest cluster is cluster {max_index + 1} with a value of {max_sum}")

cluster_investigation([[5, 10, 2], [1, 1, 1], [20, 30, 40], [8, 9]])

def trim_two_digits(lst):
    result = []
    for t in lst:
        cleaned_tuple = ()
        has_single_digit = False
        for num in t:
            if num < 10:
                has_single_digit = True
                break
            if num not in cleaned_tuple:
                cleaned_tuple += (num,)
        if not has_single_digit:
            result.append(cleaned_tuple)
    return result
my_data = [(12, 45, 12), (5, 80, 90), (15, 22, 15, 30)]

print(trim_two_digits(my_data))

def safe_travels():
    