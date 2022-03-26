
def solution(S, B):
    '''
    consecutive_potholes: number of consecutive potholes
    e.g. 
        input: '...xxx..x....xxx.', 7
        consecutive_potholes: [3, 1, 3]
        ouput: 5
    '''
    ## edge case
    if B == 0 or S == '':
        return 0

    list_S = list(S) ## tranform string to list
    consecutive_potholes = []

    ## get the list of number of consecutive potholes
    count = 0
    for _, value in enumerate(list_S):
        if value == 'x':
            count += 1
        elif value == '.' and count > 0:
            consecutive_potholes.append(count)
            count = 0
    if count != 0:
        consecutive_potholes.append(count)
    
    consecutive_potholes.sort(reverse = True)

    ## calculate the number of potholes that can be fixed
    num_fixed = 0
    for _, value in enumerate(consecutive_potholes):
        B -= 1 ## K consecutive potholes costs K+1
        if B - value >= 0: ## the budget is sufficient
            B -= value
            num_fixed += value
        else: ## the budget is insufficient
            num_fixed += B
            return num_fixed

    return num_fixed

if __name__ == '__main__':
    ans = solution('..xxxxx', 4)
    print(ans)