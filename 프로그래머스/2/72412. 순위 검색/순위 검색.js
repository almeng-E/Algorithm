function solution(info, query) {
    const answer = [];

    
    function lowerBound(arr, tg) {
        let l=0;
        let r=arr.length-1;
        while (l<=r) {
            const mid = Math.floor((l+r)/2);
            if (arr[mid] >= tg) {
                r = mid-1;
            }
            else {
                l = mid+1;
            }
        }
        return arr.length - l;
    }
    
    const infoMap = new Map();
    
    for (const x of info) {
        const [a, b, c, d, scoreText] = x.split(" ");
        const spec = [a, b, c, d];        
        const score = Number(scoreText);
        
        for (let mask=0; mask<16; ++mask) {
            const parts = [];
            for (let i=0; i<4; ++i) {
                if (mask & (1<<i)) {
                    parts.push(spec[i]);
                }
                else {
                    parts.push('-');
                }
            }
            const key = parts.join(' ');
            if (!infoMap.has(key)) infoMap.set(key, []); 
            infoMap.get(key).push(score);
        }
    }
    
    for (const k of infoMap.keys()) {
        infoMap.get(k).sort((a, b) => a-b);
    }
    
    
    for (const qq of query) {
        const qryText = qq.split(' ');
        const qSpec = [qryText[0], qryText[2], qryText[4], qryText[6]];
        const qKey = qSpec.join(' ');
        const qScore = Number(qryText[7]);
        if (!infoMap.has(qKey)) answer.push(0);
        else {
            answer.push(lowerBound(infoMap.get(qKey), qScore));
        }
    }
    
    
    
    return answer;
}