using System;
using System.Linq;

public class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = num_list.OrderBy(x=>x).Take(5).ToArray();
        return answer;
    }
}