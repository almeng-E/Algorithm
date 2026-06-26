function solution(left, right) {
    let answer = 0;
    
    for (let i=left; i<=right; i++) {
        answer += Math.sqrt(i)%1 === 0 ? -i : i;
        
    }
    
    return answer;
}