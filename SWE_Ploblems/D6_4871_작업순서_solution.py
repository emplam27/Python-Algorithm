# 10일차 - 작업순서
def dfs(v):  # 방문하지 않은 후행작업이 있을 경우, 방문하는 함수
             # 해당노드의 더이상 방문할 후행작업이 없을 경우, 해당 노드의 순서를 결정하면 됨

    visited[v] = 1  # 해당 노드의 방문하지 않은 후행작업이 있으면 해당노드를 방문

    for i in range(1, V+1):
        if mat[v][i] == 1 and visited[i] == 0:  # 해당 노드를 선행 작업으로 둔 후행노들을 찾으면서, 방문하지 않은 노드들을 찾음
            dfs(i)      # 찾은 노드들로 dfs 를 한번 더 들어감. 계속해서 자신 후행 노드를 찾아서감
    stack.append(v)     # 마지막 노드에 도닥하게 되면 append 하고 이전 노드로 돌아감
                        # dfs 로 들어간 모든 후행노드들이 찍힌 후에 처음 노드가 찍히게됨
                        # 결국 수행 역순의 stack이 만들어짐

for tc in range(1,11):
    V, E = map(int,input().split())
    # 인접행렬 : 각 노드의 후행작업 목록
    # 인접행렬의 전치행렬 : 각노드의 선행작업 목록
    mat = [[0]*(V+1) for _ in range(V+1)]
    tran_mat = [[0]*(V+1) for _ in range(V+1)]

    # 노드 방문 여부 표시하는 방문배열
    visited = [0]*(V+1)
    # 작업 순서를 저장할 스택 : 나중에 실행할 작업부터  push
    stack = list()

    # 노드간 간선 정보: 2개씩 끊어서 읽으면 됩니다
    numbers = list(map(int, input().split()))
    for i in range(0, len(numbers), 2):
        s, e = numbers[i], numbers[i+1]
        mat[s][e] = 1   # 후행작업 목록
        tran_mat[e][s] = 1  # 선행 작업 목록

    # 모든 선행작업이 없는 작업들을 확인하면서, dfs 실행
    for i in range(1,V+1):
            # 선행작업이 없으면...
        if tran_mat[i].count(1) == 0:
            dfs(i)

    # 후행작업부터 push했으니.. 가장 늦게 push된 것부터 꺼내면 됨
    print("#%d" % tc, end=" ")
    print(*stack[::-1])




