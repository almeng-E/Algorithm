function solution(n, s, a, b, fares) {
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

    function djikstra(start) {
        const hq = new MinHeap();
        hq.push([0, start]);
        const dist = Array.from({length: n+1}, ()=>Infinity);
        dist[start] = 0;
        while (hq.size() > 0) {
            const [d, cur] = hq.pop();
            if (dist[cur] < d) continue;
            
            for (let i=0; i<G[cur].length; ++i) {
                const nxt = G[cur][i][0];
                const w = G[cur][i][1];
                
                const nd = d+w;
                
                if (dist[nxt] > nd) {
                    dist[nxt] = nd;
                    hq.push([nd, nxt]);
                }
            }
        }
        
        return dist;
    }
    
    const G = Array.from({length: n+1}, ()=>[]);
    for (const [a, b, w] of fares) {
        G[a].push([b, w]);
        G[b].push([a, w]);
    }
    
    const distA = djikstra(a);
    const distB = djikstra(b);
    const distS = djikstra(s);
    let answer = Infinity;
    
    // s->x 함께, x->a + x->b
    for (let x=1; x<=n; ++x) {
        const tmp = distS[x] + distA[x] + distB[x];
        answer = Math.min(answer, tmp);
    }

    return answer;
}