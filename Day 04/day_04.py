from numpy import array


def solution(list):
    # First remove all negative numbers
    list[:] = [x for x in list if x > 0]

    # keep track of numbers using negatives
    list_len = len(list)
    for elem in list:
        elem_abs = abs(elem)
        if (elem_abs > 0 and elem_abs < list_len):
            # To take care of duplicate numbers
            list[elem_abs] = -abs(list[elem_abs])

    for x, val in enumerate(list):
        if val > 0 and x != 0:
            return x

    return list_len + 1


def main():
    # test_list = [3, 4, -1, 1]
    # test_list = [1, 2, 0]
    # test_list = [2, 4, -8, 10, 15, 0, 0, -1, 1]
    test_list = [0, 0, 0]
    print(solution(test_list))


if __name__ == '__main__':
    main()