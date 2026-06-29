function solution(n) {
    function bitCounter(num) {
        let cnt = 0;
        for (let i=0; i<30; ++i) {
            const mask = 1<<i;
            cnt += mask&n ? 1 : 0;
        }   
        return cnt;
    }
    
    const nBit = bitCounter(n);
    
    while (true) {
        n++;
        if (nBit === bitCounter(n)) return n;
    }
}