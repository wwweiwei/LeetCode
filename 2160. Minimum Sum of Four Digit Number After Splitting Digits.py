class Solution:
    def minimumSum(self, num: int) -> int:
        digit_string = str(num)
        digit_map = map(int, digit_string)
        num_list = list(digit_map)
        
        num_list.sort()
                
        int_1 = int(num_list[0]*10+num_list[3])
        int_2 = int(num_list[1]*10+num_list[2])
        
        return int_1+int_2

        # int_3 = int(num_list[0]*10+num_list[2])
        # int_4 = int(num_list[1]*10+num_list[3])

        # return min(int_1+int_2, int_3+int_4)
        
if __name__ == '__main__':
    sol = Solution()
    ans = sol.minimumSum(2932)
    print(ans)