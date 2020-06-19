import sys
sys.stdin = open('../못푼문제/input.txt', 'r')


# 함수는 최대한 간소화할 것.
# 조합의 경우에는 조합을 위한 함수만 다로둘 것
# 조합을 끝내고 이후에 다른 일을 하는 함수로 들어가게 할 것
# isnumeric() : string을 넣었을때, 숫자로 변환 가능하면 True를 반환
# N이 1, 0같은거 꼭 예외처리 해주기.. 안하면 런타임에러남
# max_result 같은 경우는 꼭 음수로 해두기


def calculate(num1, num2, oper):
    if oper == '+':
        return str(int(num1) + int(num2))
    elif oper == '-':
        return str(int(num1) - int(num2))
    elif oper == '*':
        return str(int(num1) * int(num2))


def find_result_cal(selected):

    # 선택된 연산자들을 정리한다.
    # 먼저 개산하여 새로운 number, operator배열에 너어준다.
    # 이후 두 배열을 이용하여 계산을 진행한다.
    tmp_numbers, tmp_operators = [], []

    # 연산자 먼저 정리
    for i in range(len(selected)):
        if selected[i] == 0:
            tmp_operators.append(operators[i])

    # 숫자 정리
    i = 0
    while i < len(selected):
        if selected[i] == 1:
            tmp_numbers.append(calculate(numbers[i], numbers[i + 1], operators[i]))
            i += 2
        else:
            tmp_numbers.append(numbers[i])
            i += 1

    if selected[-1] == 0:
        tmp_numbers.append(numbers[-1])

    # 결과값 구하기
    tmp = tmp_numbers[0]
    for i in range(len(tmp_operators)):
        tmp = calculate(tmp, tmp_numbers[i + 1], tmp_operators[i])

    return int(tmp)


def combination(idx, selected):
    global max_result
    # 재귀함수를 돌면서 연산자를 선택할지 안할지
    # 연산자를 선택할경우 결과를 위한 변수에 연산을 하고, 다다음 연산자를 탐색하여 들어간다.
    # 연산자를 선택하지 않을 경우 다음 연산자로 넘어간다.

    if idx >= len(operators):
        tmp_result = find_result_cal(selected)
        if max_result < tmp_result:
            max_result = tmp_result
        return

    # 연산자를 선택할 경우
    selected[idx] = 1
    combination(idx + 2, selected)
    # 연산자를 선택하지 않을 경우
    selected[idx] = 0
    combination(idx + 1, selected)


N = int(input())
equation = input()

# 숫자와 연산자 구분하기
numbers, operators = [], []
for char in equation:
    if char.isnumeric():
        numbers.append(char)
    else:
        operators.append(char)

max_result = -(2**31)
if N > 1:
    selected = [0] * len(operators)
    combination(0, selected)
else:
    max_result = int(equation)
print(max_result)
