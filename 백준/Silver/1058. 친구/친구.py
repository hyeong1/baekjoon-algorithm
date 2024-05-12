N = int(input())
friends = [list(map(str, input())) for _ in range(N)]

max_friend = 0
for i in range(N):
    i_friend = []
    friend_cnt = 0
    for j in range(N):
        if i == j:
            continue
        if friends[i][j] == 'Y':
            friend_cnt += 1
            i_friend.append(j)
    for j in range(N):
        if i == j:
            continue
        if friends[i][j] == 'N':
            for f in i_friend:
                if friends[j][f] == 'Y':
                    friend_cnt += 1
                    break
    max_friend = max(max_friend, friend_cnt)

print(max_friend)
