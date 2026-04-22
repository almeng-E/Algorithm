using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string binomial) {
        string[] li = binomial.Split(' ');
        int a = int.Parse(li[0]);
        int b = int.Parse(li[2]);
        string op = li[1];
        
        if (op == "+") return a+b;
        if (op == "-") return a-b;
        if (op == "*") return a*b;
        
        return 0;
    }
}