using System;

public class Solution {
    public string solution(int[] numbers) {
        var arr = new string[numbers.Length];
        for (int i=0; i<numbers.Length; ++i) {
            arr[i] = numbers[i].ToString();
        }
        Array.Sort(arr, (a, b) => (b+a).CompareTo(a+b));
        
        string answer = string.Join("", arr);
        if (answer[0] == '0') return "0";
        return answer;
    }
}