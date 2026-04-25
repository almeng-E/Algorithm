using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    int ans;
    int N;
    int[] col;
    int[] r_diag;
    int[] l_diag;

    public void change(int r, int c, int v) {
        col[c] = v;
        r_diag[r+c] = v;
        l_diag[r-c+N] = v;      
    }
    
    public void backtrack(int r_idx) {
        if (r_idx == N) {
            ans++;
            return;
        }
        for (int c_idx=0; c_idx<N; ++c_idx) {
            if (col[c_idx] == 0 && r_diag[r_idx+c_idx] == 0 && l_diag[r_idx-c_idx+N] == 0) {
                change(r_idx, c_idx, 1);
                backtrack(r_idx+1);
                change(r_idx, c_idx, 0);
            }
        }
    }   
    
    static void Main() {
        string input = Console.ReadLine();
        int n = int.Parse(input);
        
        Solution sol = new Solution();
        
        sol.ans = 0;
        sol.N = n;
        sol.col = new int[n];
        sol.r_diag = new int[2*n];
        sol.l_diag = new int[2*n];
        
        sol.backtrack(0);        
        
        Console.WriteLine(sol.ans);
    }
}