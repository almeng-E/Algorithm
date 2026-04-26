using System;

public class Solution {
    public string solution(string my_string) {
        char[] s = new char[my_string.Length];
        for (int i=0; i<my_string.Length; ++i) {
            s[i] = char.ToLower(my_string[i]);
        }
        Array.Sort(s);
        string answer = "";
        for (int i=0; i<s.Length; ++i) {
            answer += s[i];
        }
        return answer;
    }
}