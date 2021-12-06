#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes
can be opened.
'''


def unlockTest(d, n):
    '''
    Test if everything was unlocked
    '''
    return all([d[i]['unlocked'] for i in range(n)])


def canUnlockAll_helper(d, key_list):
    '''
    Helper function
    '''
    if type(key_list) is not list:
        key_list = [key_list]
    for i in key_list:
        try:
            if not d[i]['unlocked']:
                d[i]['unlocked'] = True
                canUnlockAll_helper(d, d[i]['keys'])
        except KeyError:
            # Means a key without a box
            pass


def canUnlockAll(boxes):
    '''
    Returns True or False depending on if all boxes
    were unlocked
    '''
    n_box = len(boxes)
    if n_box == 1:
        return True
    box_dict = {0: {'keys': boxes[0], 'unlocked': True}}
    for i in range(1, n_box):
        box_dict[i] = {'keys': boxes[i], 'unlocked': False}
    canUnlockAll_helper(box_dict, box_dict[0]['keys'])
    # debug
    # print(box_dict)
    return(unlockTest(box_dict, n_box))
