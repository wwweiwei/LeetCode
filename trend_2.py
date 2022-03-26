import math

def solution(A):
    '''
    list_sum: a list to save sum of neighbouring pairs
    dict_number: {sum_1: count_1, sum_2: count_2, ...}
    '''
    if A is None: ## no element
        return 0
    elif len(A) == 1: ## just one element
        return 1

    ## calculate all the sum of neighbouring pairs
    list_sum = []
    last_value = A[-1]
    for i, value in enumerate(A):
        list_sum.append(value+last_value)
        last_value = value

    ## calculate the freqency of each sum
    dict_number = {}
    for i, key in enumerate(list_sum):
        if key not in dict_number:
            last = -2
            count = 0
            for j, value in enumerate(list_sum):
                if i == 0 and j == len(list_sum)-1: ## can not use the last element twice
                    break
                if j - last > 1 and value == key: ## not use the same element
                    count += 1
                    last = j
            dict_number[key] = count ## {key, count}

    ## sort the dictionary(dict_number) by count
    list_order = sorted(dict_number.items(), key=lambda x:x[1])

    return list_order[0][1]

if __name__ == '__main__':
    ans = solution([14, 21, 16, 35, 22])
    print('ans: ', ans)