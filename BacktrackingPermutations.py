def permute(sequence: list, left_index, right_index):
    if left_index == right_index:
        print(sequence)
    else:
        for index in range(sequence, right_index + 1):
            sequence[index], sequence[left_index] = sequence[left_index], sequence[index]
            permute(sequence, left_index + 1, right_index)
            sequence[index], sequence[left_index] = sequence[left_index], sequence[index]


# The first parameter represents the sequence, and the other 2 represent the left and right indexes of the sequence
permute([1, 2, 3, 4], 0, 3)