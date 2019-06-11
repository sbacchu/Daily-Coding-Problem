def solution(list):
    product = 1
    for num in list:
        product = product*num

    for i in range(len(list)):
        list[i] = int(product/list[i])

    return list