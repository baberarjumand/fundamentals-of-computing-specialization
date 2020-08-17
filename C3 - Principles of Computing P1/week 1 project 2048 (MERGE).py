"""
Merge function for 2048 game.
Demo: http://www.codeskulptor.org/#user47_AcOdII4L6p_1.py
"""

def slide_items_left(line):
    """
    Slides all items to the left in a list
    """    
    input_list = list(line)
    slide_list = [0] * len(input_list)
    slide_list_idx = 0
    for val in input_list:        
        if val != 0:
            slide_list.insert(slide_list_idx, val)
            slide_list_idx += 1
            slide_list.pop()
    return slide_list


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """    
    input_list = list(line)    
    slid_items = slide_items_left(input_list)
    for idx in range(0, len(slid_items) - 1):
        if slid_items[idx] == slid_items[idx + 1]:
            slid_items[idx] *= 2
            slid_items[idx + 1] = 0            
    output_list = slide_items_left(slid_items)    
    return output_list


print merge([2, 0, 2, 2])
print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])