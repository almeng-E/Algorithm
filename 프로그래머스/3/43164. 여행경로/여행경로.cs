using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    int _tCnt;
    Stack<string> _path;
    bool _found;
    bool[] _used;
    Dictionary<string, List<Tuple<string, int>>> _g;
    
    
    public void backtrack(string cur, int cnt) {
        if (cnt == _tCnt) {
            _found = true;
            return;
        }
        if (!_g.ContainsKey(cur)) return;
        
        foreach (var item in _g[cur]) {
            string nxt = item.Item1;
            int tId = item.Item2;
            if (_used[tId]) continue;
            _path.Push(nxt);
            _used[tId] = true;
            backtrack(nxt, cnt+1);
            if (_found) {
                return;
            }
            _used[tId] = false;
            _path.Pop();
        }
    }
    
    public string[] solution(string[,] tickets) {
        _tCnt = tickets.GetLength(0);
        _path = new Stack<string>();    
        _found = false;
        _used = new bool[_tCnt];
        
        _g = new Dictionary<string, List<Tuple<string, int>>>();
        for (int i=0; i<tickets.GetLength(0); ++i) {
            string a = tickets[i, 0];
            string b = tickets[i, 1];
            if (!_g.ContainsKey(a)) {
                _g[a] = new List<Tuple<string, int>>();
            }
            _g[a].Add(new Tuple<string, int>(b, i));
        }
        foreach (var v in _g.Values) {
            v.Sort();
        }
        _path.Push("ICN");
        backtrack("ICN", 0);
        
        
        string[] answer = _path.Reverse().ToArray();
        return answer;
    }
    
}