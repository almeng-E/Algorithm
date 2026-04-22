using System;
using System.Collections.Generic;

public class Solution {
    public string solution(int n) {
        List<int> li = new List<int>();
        while (n > 0) {
            li.Add(n%10);               
            n /= 10;
        }
        li.Reverse();
        string answer = string.Join("", li);
        
        return answer;
    }
}