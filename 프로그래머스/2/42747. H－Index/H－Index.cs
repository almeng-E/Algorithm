using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Array.Sort(citations, (a, b) => (b-a));
        Console.WriteLine(String.Join(" ", citations));
        for (int i=0; i<citations.Length; ++i) {
            if (citations[i] >= i+1){
                answer = i+1;
            }
            else {
                break;
            }
        }
        
        
        return answer;
    }
}