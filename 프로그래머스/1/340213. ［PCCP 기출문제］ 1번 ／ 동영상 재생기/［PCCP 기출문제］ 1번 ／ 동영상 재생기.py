def solution(video_len, pos, op_start, op_end, commands):
    video_sec = int(video_len[:2]) * 60 + int(video_len[3:])
    pos_sec = int(pos[:2]) * 60 + int(pos[3:])
    start_sec = int(op_start[:2]) * 60 + int(op_start[3:])
    end_sec = int(op_end[:2]) * 60 + int(op_end[3:])
    
    if start_sec <= pos_sec < end_sec:
            pos_sec = end_sec
    
    for command in commands:
        if command == 'next':
            pos_sec += 10
            pos_sec = min(pos_sec, video_sec)
        else:
            pos_sec -= 10
            pos_sec = max(pos_sec, 0)
        
        if start_sec <= pos_sec < end_sec:
            pos_sec = end_sec
    
    return f'{pos_sec // 60:02}:{pos_sec % 60:02}'