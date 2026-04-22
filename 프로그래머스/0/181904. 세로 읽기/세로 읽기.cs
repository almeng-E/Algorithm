using System;

public class Solution {
    public string solution(string my_string, int m, int c) {
        string answer = "";
        int len = my_string.Length;
        for (int i=0; i<len/m; ++i) {
            answer += my_string[i*m+c-1];
        }
        
        return answer;
    }
}