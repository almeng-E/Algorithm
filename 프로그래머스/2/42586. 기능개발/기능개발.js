function solution(progresses, speeds) {
    const answer = [];
    const N = progresses.length;
    
    const remain = [];
    for (let i=0; i<N; ++i) {
        const [p, s] = [progresses[i], speeds[i]];
        remain.push(Math.ceil((100-p) / s));
    }
    
        let deployDay = remain[0];
    let count = 1;

    for (let i = 1; i < N; ++i) {
        if (remain[i] <= deployDay) {
            count++;
        } else {
            answer.push(count);

            deployDay = remain[i];
            count = 1;
        }
    }

    answer.push(count);

    return answer;
    
}