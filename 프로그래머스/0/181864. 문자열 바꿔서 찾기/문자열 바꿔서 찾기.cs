using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string myString, string pat) {
        int N = myString.Length;
        List<char> li = new List<char>();
        for (int i=0; i<N; ++i) {
            if (myString[i] == 'A') {
                li.Add('B');
            } else {
                li.Add('A');
            }
        }
        int M = pat.Length;
        for (int i=0; i<N-M+1; ++i) {
            if (pat == new string(li.GetRange(i, M).ToArray())){
                return 1;
            }
        }
        return 0;
    }
}