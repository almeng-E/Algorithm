function solution(n) {
    var answer = Number(String(n).split('').sort().reverse().join(''));
    return answer;
}