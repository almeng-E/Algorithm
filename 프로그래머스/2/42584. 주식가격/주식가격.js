function solution(prices) {
    const N = prices.length
    const answer = Array.from({length: N}, ()=>0);
    
    const stack = []; // [가격, 시점]
    for (time=0; time<N; ++time) {
        while ((stack.length > 0) && (stack[stack.length-1][0] > prices[time])) {
            const [, idx] = stack.pop();
            answer[idx] = time-idx;
        }
        
        stack.push([prices[time], time]);
    }
    while (stack.length > 0) {
        const [, idx] = stack.pop();
        answer[idx] = N-1-idx;
    }
    
    
    return answer;
}