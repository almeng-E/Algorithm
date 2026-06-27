function solution(topping) {
    let answer = 0;
    const N = topping.length;
    const L = new Set();
    const pref = new Array(N+1).fill(0);
    
    for (let i=0; i<N; ++i) {
        L.add(topping[i]);
        pref[i+1] = L.size;
    }
    

    const R = new Set();
    for (let i=N-1; i>=0; --i) {
        R.add(topping[i]);
        if (pref[i] === R.size) answer++;
    }
    
    return answer;
}