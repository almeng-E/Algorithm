function solution(s) {
    const answer = [];
    
    const arr = s.replace('{{', '').replace('}}', '').split('},{');
    for (let i=0; i<arr.length; ++i) {
        arr[i] = new Set(arr[i].split(','));
    }
    arr.push(new Set());
    arr.sort((a, b) => {
        if (a.size < b.size) return -1;
        else return 1;
    })
    
    for (let i=1; i<arr.length; ++i) {
        const [x] = arr[i].difference(arr[i-1])
        answer.push(Number(x));
    }
    return answer;
}