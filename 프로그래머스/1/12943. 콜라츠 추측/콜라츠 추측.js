function solution(num) {
    let answer = 0;
    while (num !== 1) {
        answer++;
        num = num%2===0 ? num/2 : num*3 + 1;
    }
    
    
    
    return answer<=500 ? answer : -1;
}