N, M = map(int, input().split())
x, y, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]
move = 0

while True:
    for i in range(4):
        nx = x + pos[(direction + i) % 4][0] 
        ny = y + pos[(direction + i) % 4][1]  

        if(board[nx][ny] == 0):
            direction = (direction + i) % 4
            board[nx][ny] = 2
            x, y = nx, ny
            move += 1
            continue

    if(board[nx][ny] != 0):
        x -= pos[direction][0]
        y -= pos[direction][1]

        if(board[x][y] == 1):
            break

print(move)