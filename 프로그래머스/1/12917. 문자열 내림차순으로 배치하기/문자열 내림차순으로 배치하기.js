function solution(s) {
    let answer = '';
    
    const arr = [...s].sort().reverse();
   
    answer = arr.join('');
    return answer;
}