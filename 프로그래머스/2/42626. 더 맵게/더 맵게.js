function solution(scoville, K) {
    let answer = 0;
    
    class MinHeap {
        constructor() {
            this.heap = [null];
        }
        
        push(val) {
            this.heap.push(val);
            this.siftUp();
        }
        pop() {
            if (this.size() < 1) return null;
            this.swap(1, this.size());
            const ret = this.heap.pop();
            this.siftDown();
            return ret;
        }
        peek() {
            if (this.size() >= 1) return this.heap[1];
            else return null;
        }
        size() {
            return this.heap.length-1;
        }
        swap(idx1, idx2) {
            const tmp = this.heap[idx1];
            this.heap[idx1] = this.heap[idx2];
            this.heap[idx2] = tmp;
        }
        
        siftUp() {
            if (this.size() < 1) return;
            let cur = this.size();
            while (cur > 1) {
                const par = Math.floor(cur/2);
                if (this.heap[cur] < this.heap[par]) {
                    this.swap(cur, par);
                    cur = par;
                    continue;
                }
                break;
            }
        }
        siftDown() {
            if (this.size() < 1) return;
            let cur = 1;
            while (cur <= this.size()) {
                let nxt = cur;
                const lc = cur * 2;
                const rc = lc + 1;
                if ((lc <= this.size()) && (this.heap[nxt] > this.heap[lc])) {
                    nxt = lc;
                }
                if ((rc <= this.size()) && (this.heap[nxt] > this.heap[rc])) {
                    nxt = rc;
                }
                if (nxt === cur) return;
                
                this.swap(cur, nxt);
                cur = nxt;
            }
        }
    }
    
    const HEAP = new MinHeap();
    for (const x of scoville) {HEAP.push(x);}
    
    while ((HEAP.peek() < K) && (HEAP.size() >= 2)) {
        const a = HEAP.pop();
        const b = HEAP.pop();
        HEAP.push(a + b*2);
        answer++;
    }
    
    return HEAP.peek() >= K ? answer : -1;
}