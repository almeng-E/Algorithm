
'''
DP 테이블 두개를 돌립시다.
DP[0] = 1 은 그냥 쌈빡한 방법이니 참고 : 
바로 알 수는 없고
모든 조건들의 기저 조건이 DP[0] 을 가리키고 있었음.
조건문을 나눠주기 보다 DP[0]으로 처리하면 한번에 처리 가능
'''



T = int(input())
coins = []
for _ in range(int(input())):
    coins.append(list(map(int, input().split())))

coins.sort(key=lambda x: x[0])

bef_coin = [0] * (T+1)    # 1-index
bef_coin[0] = 1


for coin, cnt in coins:             # 동전 종류
    aft_coin = [0] * (T + 1)
    for i in range(coin, T+1):      # i : 현재 내가 처리할 '값'의 위치
        for n in range(1, cnt+1):   # n : 동전 사용 개수
            # index out 방지
            if i - coin*n < 0: break

            aft_coin[i] += bef_coin[i - coin*n]
    
    # 루프 준비 : 이전 단계의 값들과 현 단계의 값 더해서 다음 루프로 넘기기
    for i in range(T+1):
        bef_coin[i] += aft_coin[i]

print(bef_coin[T])