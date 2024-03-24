import sys
sys.setrecursionlimit(10**9)

nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break


def solve(start, end):
    if start > end:
        return

    parent = nums[start]
    div_idx = end+1 # 만약 왼쪽 / 오른쪽 안잘리면, end 다음 번호가 div_idx이어야함
    for i in range(start+1,end+1):
        if parent < nums[i]:
            div_idx = i
            break
            

    # 다음으로 넘어가기
    solve(start+1,div_idx-1)
    solve(div_idx,end)

    print(nums[start])
    
solve(0,len(nums)-1)
