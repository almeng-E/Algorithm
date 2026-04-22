using System;

public class Solution {
    public int solution(int[] num_list) {
        int even=0;
        int odd=0;
        
        foreach (int num in num_list){
            if (num%2 == 0) {
                even *= 10;
                even += num;
            } else {
                odd *= 10;
                odd += num;
            }
        }
        
        return even+odd;
    }
}