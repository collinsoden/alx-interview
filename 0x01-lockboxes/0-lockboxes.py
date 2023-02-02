def canUnlockAll(boxes):
    # Create a set to store all the keys
    keys = set()

    # Add the first box to the set
    keys.add(0)

    # Iterate through all the boxes and add their keys to the set
    for i in range(len(boxes)):
        for key in boxes[i]:
            keys.add(key)

    # Check if all boxes can be opened by comparing the size of the set with n, which is the number of boxes
    if len(keys) == len(boxes):
        return True

    return False
