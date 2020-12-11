import sys

sys.stdin = open('input.txt', 'r')

A, B = input(), input()

if len(A) < len(B):
    std_string, com_string = A, B
else:
    std_string, com_string = B, A

for com_len in range(len(com_string) - 1, 0, -1):
    for com_start in range(0, len(com_string) - com_len):
        current_com_sting = com_string[com_start: com_start + com_len]

        for std_start in range(0, len(std_string) - com_start):
            if std_string[std_start: std_start + com_len] ==  current_com_sting:
                print(len(current_com_sting))
                print(current_com_sting)
                exit()
