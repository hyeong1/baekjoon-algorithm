def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        hh = schedules[i] // 100
        mm = schedules[i] % 100 + 10
        if mm >= 60:
            mm -= 60
            hh += 1
        time = hh * 100 + mm
        
        success = True
        for j in range(7):
            currentday = (startday + j - 1) % 7 + 1
            if currentday <= 5:
                if time < timelogs[i][j]:
                    success = False
                    break
        if success:
            answer += 1
            
    return answer