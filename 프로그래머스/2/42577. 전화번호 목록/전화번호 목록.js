function solution(phone_book) {
    let answer = true;
    
    const arr = phone_book.sort((a, b) => {
        if (a.length !== b.length) {
            if (a.length > b.length) return 1;
            else return -1;
        }
        if (a > b) return 1;
        else return -1;
    });
    const used = new Set();
    const lengths = new Set();
    for (const s of arr) {
        for (const l of lengths) {
            if (used.has(s.slice(0, l))) return false;
        }        
        
        used.add(s);
        lengths.add(s.length);
    }
    
    return true;
}