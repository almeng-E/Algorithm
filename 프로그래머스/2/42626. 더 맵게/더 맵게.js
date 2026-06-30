class MinHeap {
    constructor() {
        this.heap = [null]; // 1-index
        this.lastIdx = 0;
    }
    
    // peek
    peek() {
        if (this.lastIdx === 0) return null;
        return this.heap[1];
    }
    
    // push
    push(val) {
        this.heap.push(val);
        this.lastIdx++;
        this.heapifyUp(this.lastIdx);
    }    
    
    // pop
    pop() {
        if (this.lastIdx === 0) return null;
        
        [this.heap[1], this.heap[this.lastIdx]] = [this.heap[this.lastIdx], this.heap[1]];
        
        const ret = this.heap.pop();
        this.lastIdx--;
        this.heapifyDown(1);
        
        return ret;
    }
    
    // heapify-down
    heapifyDown(idx) {
        let cur = idx;
        while (cur <= this.lastIdx) {
            let nxt = cur;
            
            const lc = cur*2;
            if ((lc <= this.lastIdx) && (this.heap[nxt] > this.heap[lc])) {
                nxt = lc;
            }
            const rc = lc+1;
            if ((rc <= this.lastIdx) && (this.heap[nxt] > this.heap[rc])) {
                nxt = rc;
            }
            
            if (nxt === cur) {
                break;
            }
            else {
                [this.heap[cur], this.heap[nxt]] = [this.heap[nxt], this.heap[cur]];
                cur = nxt;
            }
        }
    }
    
    // heapify-up
    heapifyUp(idx) {
        let cur = idx;
        while (cur > 1) {
            const par = cur >> 1;
            if (this.heap[cur] >= this.heap[par]) {
                break;
            }
            else {
                [this.heap[cur], this.heap[par]] = [this.heap[par], this.heap[cur]];
                cur = par;
            }
        }
    }
    
    // size
    size() {
        return this.lastIdx;
    }
    
}


function solution(scoville, K) {
    let answer = 0;

    const hq = new MinHeap();
    
    for (const sc of scoville) {
        hq.push(sc);
    }

    while (hq.size() >= 2 && hq.peek() < K) {
        const sc1 = hq.pop();
        const sc2 = hq.pop();
        hq.push(sc1 + 2*sc2);
        answer++;
    }
       
    if (hq.peek() < K) return -1;
    
    return answer;
}