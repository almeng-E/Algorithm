using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string myString, string pat) {
        string conv = myString.Replace("A", "b").Replace("B", "a");
        
        return conv.Contains(pat.ToLower()) ? 1: 0;
        
    }
}