function solution(arr, divisor) {
    const answer = [];
    
    for (const x of arr) {
        if ((x % divisor) === 0) {
            answer.push(x);
        }
    }
    if (answer.length === 0) answer.push(-1);
    answer.sort((a, b) => a-b);
    
    return answer;
}