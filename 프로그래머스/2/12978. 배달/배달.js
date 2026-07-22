function solution(N, road, K) {
    class MinHeap {
        constructor() {
            this.heap = [[null, null]];
        }

        size(){
            return this.heap.length-1;
        }
        peek(){
            if (this.size() > 1) return this.heap[1];
            else return [null, null];
        }
        smallerThan(idx1, idx2){
            if (this.heap[idx1][0] < this.heap[idx2][0]) return true;
            return false;
        }
        swap(idx1, idx2){
            const tmp = this.heap[idx1];
            this.heap[idx1] = this.heap[idx2];
            this.heap[idx2] = tmp;
        }
        
        push(val){
            this.heap.push(val);
            this.siftUp();
        }
        pop(){
            if (this.size() < 1) return [null, null];
            this.swap(1, this.size());
            const ret = this.heap.pop();
            this.siftDown();
            
            return ret
        }

        siftUp(){
            let cur = this.size();
            while (cur > 1) {
                const par = Math.floor(cur/2);
                
                if (this.smallerThan(cur, par)) {
                    this.swap(cur, par);
                    cur = par;
                    continue;
                }
                break;                
            }
        }
        siftDown(){
            if (this.size() < 1) return;
            
            let cur = 1;
            while (cur <= this.size()) {
                let nxt = cur;
                const lc = cur * 2;
                const rc = lc + 1;
                
                if (lc <= this.size() && this.smallerThan(lc, nxt)) {
                    nxt = lc;
                }
                if (rc <= this.size() && this.smallerThan(rc, nxt)) {
                    nxt = rc;
                }
                
                if (nxt === cur) return;
                
                this.swap(cur, nxt);
                cur = nxt;
            }
        }
        
    }
    
    
    
    let answer = 0;
    const G = Array.from({length: N+1}, () => []);
    const D = Array.from({length: N+1}, () => Infinity);
    
    for (const [a, b, c] of road) {
        G[a].push([b, c]);
        G[b].push([a, c]);
    }
    
    // djikstra
    
    const hq = new MinHeap();
    D[1] = 0;
    hq.push([0, 1])
    
    while (hq.size() > 0) {
        const [d, cur] = hq.pop();
        if (D[cur] < d) continue;
        
        for (let i=0; i<G[cur].length; ++i) {
            const nxt = G[cur][i][0];
            const w = G[cur][i][1];
            
            const nd = d+w;
            if (D[nxt] > nd) {
                D[nxt] = nd;
                hq.push([nd, nxt]);
            }
        }
    }
    
    for (let i=1; i<=N; ++i) {
        if (D[i] <= K) answer++;
    }
    
    return answer;
}