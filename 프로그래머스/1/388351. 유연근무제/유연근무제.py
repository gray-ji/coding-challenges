def solution(schedules, timelogs, startday):
    success = schedules[:]
    
    for i, timelog in enumerate(timelogs):
        day = startday
        for time in timelog:
            if day < 6:
                max_time = schedules[i] + 10
                if str(max_time)[-2:] >= '60':
                    max_time += 40
                if time > max_time:
                    success.remove(schedules[i])
                    break
            day = 1 if day == 7 else (day + 1)
    return len(success)