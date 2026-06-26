function solution(s){
    let answer = true;
    let p = 0;
    let y = 0;
    
    for (const c of s) {
        if (c.toLowerCase() === 'p') {
            p += 1;
        }
        else if (c.toLowerCase() === 'y') {
            y += 1;
        }
    }
    
    return p===y;
}