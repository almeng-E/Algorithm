function solution(people, limit) {
    let answer = 0;
    const arr = people.sort((a, b) => (a-b));

    let [l, r] = [0, people.length-1];
    
    while (l <= r) {
        answer++        
        if (people[l] + people[r] <= limit) l++;
        r--;
    }
    
    return answer;
}