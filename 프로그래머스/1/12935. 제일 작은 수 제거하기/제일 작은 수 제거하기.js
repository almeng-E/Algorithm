function solution(arr) {
    const answer = [];
    let min = Math.min(...arr);
    for (const i of arr) {
        if (i===min) continue;
        answer.push(i);
    }
    if (answer.length === 0) answer.push(-1)
    return answer;
}