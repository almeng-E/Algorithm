using System;

public class Solution {
    public string[] solution(string[] str_list) {
        int idx = 0;
        int dir = -1;
        for (int i=0; i<str_list.Length; ++i){
            if (str_list[i] == "l") {
                dir = 0;
                idx = i;
                break;
            } else if (str_list[i] == "r") {
                dir = 1;
                idx = i;
                break;
            }
        }
        
        if (dir == 0) {
            string[] answer = new string[idx];
            for (int i=0; i<idx; ++i) {
                answer[i] = str_list[i];
            }
            return answer;
        } else if (dir == 1) {
            string[] answer = new string[str_list.Length-idx-1];
            for (int i=0; i<str_list.Length-idx-1; ++i) {
                answer[i] = str_list[i+idx+1];
            }
            return answer;
        } else {
            string[] answer = new string[]{};
            return answer;
        }
    }
}