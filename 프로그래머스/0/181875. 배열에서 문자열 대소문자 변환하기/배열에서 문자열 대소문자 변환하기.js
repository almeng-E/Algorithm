function solution(strArr) {
    const answer = [];
    const N = strArr.length;
    for (let i=0; i<N; ++i) {
        if (i&1) {
            answer.push(strArr[i].toUpperCase());
        }
        else {
            answer.push(strArr[i].toLowerCase());
        }
    }
    return answer;
}