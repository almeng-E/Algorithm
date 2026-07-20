function solution(array, commands) {
    const answer = [];
    
    for (const cmd of commands) {
        const [i, j, k] = cmd;
        
        const cur = array.slice(i-1, j).sort((a,b) => a-b)[k-1];
        answer.push(cur);
    }

    return answer;
}