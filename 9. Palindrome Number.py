class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[len(str_x)-1-i]:
                return False
            if i == int(len(str_x)/2):
                return True
        # x_list = [int(i) for i in str(x)]
        # total_length = len(x_list)
        # for i in range(total_length):
        #     if x_list[i] != x_list[-i-1]:
        #         return False
        #     if i == int(total_length/2):
        #         return True
        