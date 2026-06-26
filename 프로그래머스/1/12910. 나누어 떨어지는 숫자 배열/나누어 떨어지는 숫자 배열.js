function solution(arr, divisor) {
    const answer = [];
    
    for (const i of arr) {
        if (i%divisor === 0) answer.push(i);
    }
    
    answer.sort((a, b) => a-b);
    if (answer.length === 0) return [-1];
    
    return answer;
}