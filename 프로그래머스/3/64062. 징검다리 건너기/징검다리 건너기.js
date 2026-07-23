function solution(stones, k) {
    let answer = 0;
    
    let l = 1;
    let r = 200_000_000;
    stones.push(200_000_000);
    
    while (l <= r) {
        const mid = Math.floor((l+r)/ 2);
        let maxJump = 0;
        let curJump = 1;
        for (const st of stones) {
            if (st >= mid) {
                maxJump = Math.max(maxJump, curJump);
                curJump = 1;
            }
            else {
                curJump++;
            }
        }
        if (maxJump <= k) {
            answer = Math.max(answer, mid);
            l = mid + 1;
        }
        else {
            r = mid - 1;
        }
    }
    
    return answer;
}