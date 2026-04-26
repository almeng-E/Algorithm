using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] solution(string myString) {
        string[] answer = myString.Split("x").Where(s => s!="").OrderBy(s=>s).ToArray();

        
        return answer;
    }
}