# import sys
# input = sys.stdin.readline

n = int(input())
m = int(input())

nominate = list(map(int, input().split()))

frame = dict()
for i in range(m):
    if len(frame) < n:
        if nominate[i] not in frame:
            frame[nominate[i]] = [1, i]
        else:
            frame[nominate[i]][0] += 1
    else:
        if nominate[i] not in frame:
            # 삭제
            least_key = 101
            least_value = 1001
            tmp_order = 1001
            for key, value in frame.items():
                if value[0] < least_value:
                    least_value = value[0]
                    least_key = key
                    tmp_order = value[1]
                elif value[0] == least_value:
                    if value[1] < tmp_order:
                        least_key = key
                        tmp_order = value[1]
                else:
                    continue
            del frame[least_key]
            frame[nominate[i]] = [1, i]
        else:
            frame[nominate[i]][0] += 1
print(*sorted(frame.keys()))


