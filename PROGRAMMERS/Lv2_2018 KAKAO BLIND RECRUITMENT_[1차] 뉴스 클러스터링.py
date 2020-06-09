def solution(str2, str1):
    set_list = []
    tmp1 = []
    tmp2 = []
    intersection = 0
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            tmp1.append(str1[i:i+2].upper())

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            tmp2.append(str2[i:i+2].upper())
            if str2[i:i+2].upper() in tmp1:
                intersection += 1
                tmp1.remove(str2[i:i+2].upper())

    union = len(tmp1 + tmp2)

    if union  == 0:
        return 65536
    elif intersection == 0:
        return 0
    else:
        return (intersection / union * 65536) // 1