using System;
using System.Collections.Generic;


public class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = arr;
        
        int len = arr.Length;
        if (len%2 == 0){
            // 짝수
            for (int i=1; i<len; i+=2){
                arr[i] += n;
            }
        } else {
            // 홀수
            for (int i=0; i<len; i+=2){
                arr[i] += n;
            }
        }
        
        return answer;
    }
}