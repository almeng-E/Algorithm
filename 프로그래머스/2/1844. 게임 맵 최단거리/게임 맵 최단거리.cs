using System;
using System.Collections.Generic;
using System.Linq;

class Solution {
    int[] dx = new int[] {0, 0, 1, -1};
    int[] dy = new int[] {1, -1, 0, 0};
    
    public int solution(int[,] board) {
        int N = board.GetLength(0);
        int M = board.GetLength(1);
        int INF = (int)1e9;
        
        var dist = new int[N][];
        for (int i = 0; i<N; ++i) {
            dist[i] = new int[M];
            Array.Fill(dist[i], INF);
        }
        dist[0][0] = 1;
        var q = new Queue<(int x, int y)>();
        q.Enqueue((0, 0));
        
        while (q.Count > 0) {
            var item = q.Dequeue();
            int x = item.x;
            int y = item.y;
            if (x==N-1 && y==M-1) break;
            for (int i=0; i<4; ++i) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (nx < 0 || nx >= N || ny < 0 || ny >= M || board[nx,ny] == 0 || dist[nx][ny] != INF) {
                    continue;
                }
                dist[nx][ny] = dist[x][y] + 1;
                q.Enqueue((nx, ny));
            }
        }
        int answer = -1;
        if (dist[N-1][M-1] != INF){
            answer = dist[N-1][M-1];
        }
        return answer;
    }
}