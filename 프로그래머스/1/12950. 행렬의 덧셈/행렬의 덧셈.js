function solution(arr1, arr2) {
    const answer = arr1;
    const N = arr1.length;
    const M = arr1[0].length;
    
    for (let i=0; i<N; ++i) {
        for (let j=0; j<M; ++j) {
            answer[i][j] += arr2[i][j];
        }
    }
    
    
    return answer;
}