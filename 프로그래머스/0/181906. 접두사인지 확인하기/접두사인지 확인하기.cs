using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string my_string, string is_prefix) {
    int l1 = my_string.Length;
    int l2 = is_prefix.Length;
    
    if (l1 < l2) return 0;
    
    string pref = "";
    for (int i=0; i<l2; ++i) {
        pref += my_string[i];
    }
    
    if (pref == is_prefix) {
        return 1;
    }
    return 0;
    }
}