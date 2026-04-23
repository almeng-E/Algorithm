using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(string[] operations) {
        // 구현이 안돼있다니 믿기지가 않는다...
        // var minPQ = new PriorityQueue<(int val, int idx)>();
        // var maxPQ = new PriorityQueue<(int val, int idx)>();
        // var isDead = new List<bool>();
        var treeSet = new SortedSet<(int val, int idx)>();
        int id = 0;
        for (int qi=0; qi<operations.Length; ++qi) {
            var op = operations[qi].Split();
            if (op[0] == "I") {
                int v = int.Parse(op[1]);
                treeSet.Add((v, id));
                id++;
            }
            else if (op[1] == "1") {
                if (treeSet.Count == 0) {
                    continue;
                }
                var max = treeSet.Max;
                treeSet.Remove(max);
            }
            else {
                if (treeSet.Count == 0) {
                    continue;
                }
                var min = treeSet.Min;
                treeSet.Remove(min);
            }
        }
        int[] answer = new int[2];
        if (treeSet.Count != 0) {
            answer[0] = treeSet.Max.val;
            answer[1] = treeSet.Min.val;
        }
        return answer;
    }
}