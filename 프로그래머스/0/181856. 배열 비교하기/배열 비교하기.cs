using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int[] ret = {0, 1, -1};
        int ans=0, len1, len2;
        len1 = arr1.Length;
        len2 = arr2.Length;
        if (len1 > len2) {
            ans = 1;
        } else if (len1 < len2) {
            ans = 2;
        } else {
            int sum1, sum2;
            sum1 = arr1.Sum();
            sum2 = arr2.Sum();
            if (sum1 > sum2){
                ans = 1;
            } else if (sum1 < sum2) {
                ans = 2;
            } 
        }
        return ret[ans];
    }
}