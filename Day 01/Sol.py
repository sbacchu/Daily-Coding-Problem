def solution(list, k):
    while(True):
        if(len(list)>0):
            num = k - list.pop(0)
            if(num in list):
                return True
        else:
            return False
