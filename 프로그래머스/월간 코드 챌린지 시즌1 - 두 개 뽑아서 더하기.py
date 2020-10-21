def solution(numbers):
    N, answer = len(numbers), set()
    for i in range(N - 1):
        for j in range(i + 1, N):
            answer.add(numbers[i] + numbers[j])
    return sorted(list(answer))