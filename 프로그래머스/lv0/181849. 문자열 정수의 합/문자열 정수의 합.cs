using System;
using System.Collections.Generic;

public class Solution {
    public int solution(string num_str) {
        int answer = 0;
        foreach (char c in num_str){
            answer += c - '0';
        }
        
        return answer;
    }
}