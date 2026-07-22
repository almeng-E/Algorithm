function solution(n, costs) {
    let answer = 0;
    
    function find(x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
    function union(a, b) {
        const rt_a = find(a);
        const rt_b = find(b);
        if (rt_a !== rt_b) {
            p[rt_a] = rt_b;
            return true;
        }
        else {
            return false;
        }
    }
    
    const p = [];
    for (let i=0; i<n; ++i) {
        p.push(i);
    }
    
    let cnt = 0;
    costs.sort((a, b) => {
        if (a[2] !== b[2]) return a[2] - b[2];
        else return 0;
    })
    
    for (const [a, b, c] of costs) {
        if (union(a, b)) {
            cnt++;
            answer += c;
        }
        
        if (cnt === n-1) break;
    }
    
    return answer;
}