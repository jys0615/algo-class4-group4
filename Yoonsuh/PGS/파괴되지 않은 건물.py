def solution(board, skill):
    n = len(board)
    m = len(board[0])

    temp = [[0] * (m + 1) for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        d = degree if type == 2 else -degree

        temp[r1][c1] += d
        temp[r1][c2 + 1] -= d
        temp[r2 + 1][c1] -= d
        temp[r2 + 1][c2 + 1] += d

        for i in range(n):
            for j in range(1, m):
                temp[i][j] += temp[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                temp[i][j] += temp[i-1][j]
        
        answer = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] + temp[i][j] > 0:
                    answer += 1
    return answer