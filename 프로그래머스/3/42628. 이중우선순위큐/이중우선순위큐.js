function solution(operations) {
    class MinHeap {
        constructor() {
            this.heap = [null];
        }
        
        push(value, vId) {
            this.heap.push([value, vId]);
            this.siftUp();
        }
        pop() {
            if (this.size() < 1) return null;
            
            this.swap(1, this.size()-1);
            const ret = this.heap.pop();
            this.siftDown();
            
            return ret
        }
        peek() {
            if (this.size() > 1) return this.heap[1];
            else return null;
        }
        size() {
            return this.heap.length;
        }        
        swap(idx1, idx2) {
            [this.heap[idx1], this.heap[idx2]] = 
                [
                this.heap[idx2],
                this.heap[idx1]
            ]
        }
        
        siftUp() {
            let cur = this.size()-1;
            while (cur > 1) {
                const par = Math.floor(cur/2);
                if (this.heap[cur][0] >= this.heap[par][0]) return;
                
                this.swap(cur, par);
                cur = par;
            }
        }
        siftDown() {
            let cur = 1;
            while (cur < this.size()) {
                let nxt = cur;
                const lc = nxt * 2;
                const rc = lc + 1;
                
                if (lc < this.size() && 
                   this.heap[nxt][0] > this.heap[lc][0]) {
                    nxt = lc;
                }
                if (rc < this.size() &&
                   this.heap[nxt][0] > this.heap[rc][0]) {
                    nxt = rc;
                }
                
                if (nxt === cur) return;
                
                this.swap(cur, nxt);
                cur = nxt;
            }
        }
    }  
    
    const LEN = operations.length;
    const used = Array.from({length:LEN}, ()=>false);
    
    const minHeap = new MinHeap();
    const maxHeap = new MinHeap();
    
    for (let i=0; i<LEN; ++i) {
        let [cmd, val] = operations[i].split(" ");
        val = Number(val);
        
        if (cmd === "I") {
            minHeap.push(val, i);            
            maxHeap.push(-val, i);            
        }
        else if (cmd === "D") {
            if (val === 1) {
                while (maxHeap.size() > 1) {
                    const [pVal, pVid] = maxHeap.pop();
                    if (used[pVid]) continue;
                    
                    used[pVid] = true;
                    break;
                }                
            }   
            else {
                while (minHeap.size() > 1) {
                    const [pVal, pVid] = minHeap.pop();
                    if (used[pVid]) continue;
                    
                    used[pVid] = true;
                    break;
                }
            }
        }
    }
    
    while (minHeap.size() > 1 && used[minHeap.peek()[1]]) {
        minHeap.pop();
    }
    while (maxHeap.size() > 1 && used[maxHeap.peek()[1]]) {
        maxHeap.pop();
    }
    
    if (minHeap.size() <= 1 || maxHeap.size() <= 1) {
        return [0, 0];
    }
    else {
        return [-maxHeap.peek()[0], minHeap.peek()[0]];
    }
    
}