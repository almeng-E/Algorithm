function solution(s){

    let left = 0;
    for (const c of s) {
        if (c === '(') {
            left++;
        }
        else {
            if (left <= 0) return false;
            left--;
        }
    }

    return left===0 ? true : false;
    
    
}