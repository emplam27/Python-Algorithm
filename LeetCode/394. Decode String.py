class Solution:
    def decodeString(self, s: str) -> str:

        # []가 여러번 겹쳐 나올 수 있으므로 stack을 사용
        # stack에 아무것도 없으면 문자 출력
        #
        # 괄호 전 숫자를 괄호가 열리면 stack에 추가
        #
        # 괄호가 닫힐 때 len(stack)이 1이라면 (문자 * 숫자)를 결과값에 추가
        # len(stack) > 1 이라면 stack의 마지막 값에 (문자 * 숫자) 한것을 더해주기

        stack, result = [], ''
        current_num, current_str = 0, ''
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            elif char == '[':
                stack.append(current_str)
                stack.append(current_num)
                current_num, current_str = 0, ''

            elif char == ']':
                tmp_num = stack.pop()
                last_str = stack.pop()
                current_str = last_str + current_str * tmp_num

            else:
                current_str += char

        return current_str
