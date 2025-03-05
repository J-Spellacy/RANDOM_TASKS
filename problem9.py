'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
import random

# generates the integar lists for random tests
def int_list_gen(length):
    int_list = []
    for i in range(length):
        n = random.randint(-9,9)
        int_list.append(n)
    return int_list

# creates a dictionary of all values and their index and sorts them by value, removing any negative and zero values as they don't help at all
# runs through the sorted list and checks if the sum should keep the values based on their neighbors in the original list

# important: doesn't work

def create_index_value_dict(int_list: list):
    return {index: value for index, value in enumerate(int_list)}


def non_adj_sum(int_list: list):
    int_dict = create_index_value_dict(int_list)
    sorted_int_dict = {k: v for k, v in reversed(sorted(int_dict.items(), key=lambda item: item[0])) if v > 0} # sorted and filtered
    for k in list(sorted_int_dict.keys()): # copies keys as a list so that for loop doesn't alter dictionary mid loop
        if (sorted_int_dict.get(k+1, 0) + sorted_int_dict.get(k-1, 0)) >= sorted_int_dict[k]: # get(k, 0) defaults the value to 0 if the item doesn't exist
            del sorted_int_dict[k]
    sum_max = sum(sorted_int_dict.values())
    return sorted_int_dict, sum_max


# attempt at making it run in O(N), not working
def opt_method(int_list: list):
    sum_list = int_list.copy()
    i_diff = 0
    for i in range(len(int_list)):
        if int_list[i] <= 0:
            del sum_list[i-i_diff]
            i_diff+=1
        elif get_list_value(int_list, i-1)+get_list_value(int_list, i+1) > int_list[i]:
            # print(f'YES {sum_list[i-i_diff]}, {get_list_value(int_list, i-1)}+{get_list_value(int_list, i+1)}={get_list_value(int_list, i-1)+get_list_value(int_list, i+1)} ')
            if get_list_value(int_list, i-2) < get_list_value(int_list, i-1) or get_list_value(int_list, i+2) < get_list_value(int_list, i+1):
                # print(f'for {int_list[i]} {get_list_value(int_list, i-2)} < {get_list_value(int_list, i-1)} or {get_list_value(int_list, i+2)} < {get_list_value(int_list, i+1)}')
                del sum_list[i-i_diff]
                i_diff+=1
        # else:
            # print(f'NO {sum_list[i-i_diff]}, {get_list_value(int_list, i-1)}+{get_list_value(int_list, i+1)}={get_list_value(int_list, i-1)+get_list_value(int_list, i+1)} ')
        # print(f'{int_list} {sum_list} {i-i_diff}')
    sum_max = sum(sum_list)
    return sum_list, sum_max

def get_list_value(list, index, default =0):
    if index >= 0:
        try:
            if list[index]>0:
                return list[index]
            else:
                return default
        except IndexError:
            return default
    else:
        return default


if __name__ == '__main__':
    # int_list = int_list_gen(5)
    int_list = [5, 9, 5, 5, 5]
    print(int_list)
    print(non_adj_sum(int_list))
    # int_list = [5,1,1,5]
    # print(int_list)
    # print(non_adj_sum(int_list))
    # int_list=[2, 4, 6, 2, 5]
    # print(int_list)
    # print(non_adj_sum(int_list))

    int_list = int_list_gen(7)
    int_list = [5, 9, 5, 9, 5, 9, 5]
    print(int_list)
    print(opt_method(int_list))
    int_list = [5,1,1,5]
    print(int_list)
    print(opt_method(int_list))
    int_list=[2, 4, 6, 2, 5]
    print(int_list)
    print(opt_method(int_list))
