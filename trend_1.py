import re

def solution(N, S):
    '''
    isReserved: a 2-dimension list to record if the seat is reserved
    '''
    if S == '': ## no reserved
        return N*2

    isReserved = [] ## a 2D list
    for _ in range(N):
        row = [0] * 10 ## init (all the seat is not reserved)
        isReserved.append(row)

    ## parse the input string(S)
    dict_col = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'J':8, 'K':9}
    list_reserved = S.split(' ')
    if '' in list_reserved:
        list_reserved = list_reserved.remove('')

    ## update the seat condition
    for _, value in enumerate(list_reserved):
        seat = list(value)
        col = dict_col[seat[-1]]
        row = int(''.join(seat[:-1])) - 1
        isReserved[row][col] = 1 ## change the seat into reserved
    
    ## count how many four-person seats are available
    family = 0
    for _, row in enumerate(isReserved):
        if row[1:5] == [0,0,0,0]: ## across the aisle (BCDE)
            family += 1
            if row[5:9] == [0,0,0,0]: ## across the aisle (FGHJ)
                family += 1
        elif row[4:8] == [0,0,0,0]: ## center (DEFG)
            family += 1

    return family


if __name__ == '__main__':
    ans = solution(2, '1A 2F 1C')
    print('ans: ',ans)