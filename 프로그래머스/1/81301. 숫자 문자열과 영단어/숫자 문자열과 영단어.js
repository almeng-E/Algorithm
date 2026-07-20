function solution(s) {
    let answer = 0;
    
    const arr = new Map([
        ['zero', '0'],
        ['one', '1'],
        ['two', '2'],
        ['three', '3'],
        ['four', '4'],
        ['five', '5'],
        ['six', '6'],
        ['seven', '7'],
        ['eight', '8'],
        ['nine', '9'],
    ])
    
    for (let [k, v] of arr) {
        s = s.replaceAll(k, v);
    }
    
    
    
    return Number(s);
}