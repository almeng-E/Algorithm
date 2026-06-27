function solution(s) {
    const answer = [];
    
    const arr = s.replace('{{', '').replace('}}', '').split('},{');
    for (let i=0; i<arr.length; ++i) {
        arr[i] = new Set(arr[i].split(','));
    }
    arr.sort((a, b) => a.size - b.size);

    for (let i=arr.length-1; i>0; --i) {
        arr[i] = arr[i].difference(arr[i-1]);
    }
    for (let i=0; i<arr.length; ++i) {
        answer.push(Number(arr[i].values().next().value));
    }
    

    return answer;
}