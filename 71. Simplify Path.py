class Solution:
    def simplifyPath(self, path: str) -> str:
        output_path = []
        tmp = ''
        path += '/'
        for c in path:
            if c == '/':
                if tmp == '..':
                    if output_path:
                        output_path.pop()
                elif tmp != '.' and tmp:
                    output_path.append(tmp)
                tmp = ''
            else:
                tmp += c

        output_string = ''
        for file_name in output_path:
            output_string += '/'
            output_string += file_name
        if output_path == []:
            output_string = '/'

        print(output_string)
        return output_string


if __name__ == '__main__':
    sol = Solution()
    sol.simplifyPath("/a//b////c/d//././/..")