function solution(left, right) {
    let answer = 0;
    for (let x=left; x<=right; ++x) {
        if ((Math.floor(x**0.5) ** 2) === x) answer -= x; 
        else answer+=x;
    }
    return answer;
}