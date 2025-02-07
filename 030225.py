'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
'''

import random

# generates random list of class start and end times
def generate_list(size):
    if size < 2:
        return []

    li = [random.randint(1, 50)]
    for i in range(0, size-1):
        if i % 2 == 0:
            li.append(random.randint(li[-1] + 1, li[-1] + 100))
        else:
            li.append(random.randint(1, li[-1] - 1))
    
    x = list(zip(li[::2], li[1::2]))
    return x

x = generate_list(10)
print(x)
# x = [(21, 33), (22, 61), (7, 57), (48, 122)]
# given a list of start and end times, returns the minimum number of rooms required for all classes

def min_rooms(x):
    # sorts the rooms by start time
    x_sorted = sorted(x, key = lambda item: item[0])
    print(x_sorted)

    # sets the room end time to compare with and starts the current room list
    room = x_sorted[0][1]
    room_count = 1
    current_room_li  = [x_sorted[0]]
    x_sorted.pop(0)

    # iterates through the sorted list and adds rooms and to the room list based upon the whole list with any overlaps (i am sure there is a more efficient way to do this)
    while x_sorted != []:
        for i in x_sorted:
            if i[0] >= room:
                room = i[1]
                current_room_li.append(i)
                x_sorted.remove(i)

        # incase there is a multiple room chain at the end of the list
        if x_sorted == []:
            break


        print(current_room_li)
        room_count += 1
        room = x_sorted[0][1]
        current_room_li = [x_sorted[0]]
        x_sorted.remove(x_sorted[0])
    
    # prints the final chain of rooms
    print(current_room_li)
    return room_count

room_count = min_rooms(x)
print(room_count)