function solution(food) {
    let answer = '';
    
    const arr = [];
    for (let i=1; i<food.length; ++i) {
        for (let j=0; j<Math.floor(food[i]/2); ++j) {
            arr.push(i);
        }
    }

    answer = arr.join('') + '0' + arr.reverse().join('');
    
    return answer;
}