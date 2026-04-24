using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int rows, int columns, int[,] queries) {
        List<int> ret = new List<int>();
        var board = new int[rows,columns];
        // 초기화
        int cnt=1;
        for (int i=0; i<rows; ++i) {
            for (int j=0; j<columns; ++j) {
                board[i,j] = cnt;
                cnt++;
            }
        }
        
        // 쿼리
        for (int qi=0; qi<queries.GetLength(0); ++qi) {
            int x1=queries[qi,0]-1,y1=queries[qi,1]-1,
                x2=queries[qi,2]-1, y2=queries[qi,3]-1;
            var tmp = new List<int>();
            tmp.Add(board[x1+1,y1]);
            // >
            for (int j=y1; j<y2; ++j) {
                tmp.Add(board[x1,j]);
            }
            // v
            for (int i=x1; i<x2; ++i) {
                tmp.Add(board[i,y2]);
            }
            // <
            for (int j=y2; j>y1; --j) {
                tmp.Add(board[x2,j]);
            }
            // ^
            for (int i=x2; i>x1; --i) {
                tmp.Add(board[i,y1]);
            }
            
            // 붙여넣기
            int minVal = cnt;
            int idx = 0;
            // >
            for (int j=y1; j<y2; ++j) {
                board[x1,j] = tmp[idx];
                minVal = Math.Min(minVal, tmp[idx]);                
                idx++;
            }
            // v
            for (int i=x1; i<x2; ++i) {
                board[i,y2] = tmp[idx];
                minVal = Math.Min(minVal, tmp[idx]);                
                idx++;
            }
            // <
            for (int j=y2; j>y1; --j) {
                board[x2,j] = tmp[idx];
                minVal = Math.Min(minVal, tmp[idx]);                
                idx++;
            }
            // ^
            for (int i=x2; i>x1; --i) {
                board[i,y1] = tmp[idx];
                minVal = Math.Min(minVal, tmp[idx]);                
                idx++;
            }
            ret.Add(minVal);    
        }        
        
        int[] answer = ret.ToArray();
        return answer;
    }
}