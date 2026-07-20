function solution(arr) {
    const answer = [];
    let MIN = Infinity;
    for (let i=0; i<arr.length; ++i) {
        if (MIN > arr[i]) {
            MIN = arr[i];
        }
    }
    for (const x of arr) {
        if (x === MIN) continue;
        answer.push(x);
    }
    
    
    return (answer.length > 0) ? answer : [-1];
}