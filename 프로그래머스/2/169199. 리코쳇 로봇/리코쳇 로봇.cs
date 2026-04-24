using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(string[] board) {
        
        int N = board.Length;
        int M = board[0].Length;

        int tx=-1;
        int ty=-1;
        
        int sx=-1;
        int sy=-1;
        
        // 우, 하, 좌, 상
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        
        for (int i=0; i<N; ++i) {
            for (int j=0; j<M; ++j) {
                if (board[i][j] == 'R') {
                    sx = i;
                    sy = j;
                }
                else if (board[i][j] == 'G') {
                    tx = i;
                    ty = j;
                }
            }
        }
        
        
        var q = new Queue<(int x, int y)>();
        q.Enqueue((sx, sy));
        var v = new int[N,M];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                v[i, j] = -1;
            }
        }
        v[sx,sy] = 0;
        
        while (q.Count>0) {
            var cur = q.Dequeue();
            int x, y;
            x = cur.x;
            y = cur.y;
            
            if (x==tx && y==ty) return v[x,y];
            
            for (int d=0; d<4; ++d) {
                int nx, ny;
                nx = x;
                ny = y;
                while (nx + dx[d] >= 0 && nx + dx[d] < N && 
                       ny + dy[d] >= 0 && ny + dy[d] < M && 
                       board[nx + dx[d]][ny + dy[d]] != 'D') {
                    nx += dx[d];
                    ny += dy[d];
                }
                if (v[nx,ny] == -1) {
                    v[nx,ny] = v[x,y]+1;
                    q.Enqueue((nx, ny));
                }
                
            }
        }
        
        return -1;
    }
}