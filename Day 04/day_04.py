def solution(arr):

    hash_arr = []

    for elem in arr:
        if elem > 0:
            hash_arr[elem] = elem

    return hash_arr


def main():
    # test_list = [3, 4, -1, 1]
    # test_list = [1, 2, 0]
    test_list = [2, 4, -8, 10, 15, 0, 0, -1, 1]
    # test_list = [0, 0, 0]
    print(solution(test_list))


if __name__ == '__main__':
    main()