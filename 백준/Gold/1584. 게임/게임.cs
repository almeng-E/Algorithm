using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Program {
    static void Main() {
        using (var sr = new StreamReader(Console.OpenStandardInput()))
        using (var sw = new StreamWriter(Console.OpenStandardOutput()))
        {
            string firstLine = sr.ReadLine();
            if (string.IsNullOrEmpty(firstLine)) return;
            
            int N = int.Parse(firstLine.Trim());
            int[,] dangerZones = new int[N, 4];
            for (int i = 0; i < N; i++)
            {
                string[] parts = sr.ReadLine().Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                dangerZones[i, 0] = int.Parse(parts[0]);
                dangerZones[i, 1] = int.Parse(parts[1]);
                dangerZones[i, 2] = int.Parse(parts[2]);
                dangerZones[i, 3] = int.Parse(parts[3]);
            }

            int M = int.Parse(sr.ReadLine().Trim());
            int[,] deathZones = new int[M, 4];
            for (int i = 0; i < M; i++)
            {
                string[] parts = sr.ReadLine().Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                deathZones[i, 0] = int.Parse(parts[0]);
                deathZones[i, 1] = int.Parse(parts[1]);
                deathZones[i, 2] = int.Parse(parts[2]);
                deathZones[i, 3] = int.Parse(parts[3]);
            }

            Solution sol = new Solution();
            int answer = sol.solution(N, dangerZones, M, deathZones);

            sw.WriteLine(answer);
        }
    }
}

public class Solution {
    public int solution(int N, int[,] dangerZones, int M, int[,] deathZones) {
        int answer = -1;
        int[] dx = new int[]{0, 0, 1, -1};
        int[] dy = new int[]{1, -1, 0, 0};
        int[,] board = new int[501,501];

        int x1, y1, x2, y2;
        for (int i=0; i<N; ++i) {
            x1 = Math.Min(dangerZones[i, 0], dangerZones[i, 2]);
            y1 = Math.Min(dangerZones[i, 1], dangerZones[i, 3]);
            x2 = Math.Max(dangerZones[i, 0], dangerZones[i, 2]);
            y2 = Math.Max(dangerZones[i, 1], dangerZones[i, 3]);
            for (int x=x1; x<=x2; ++x) {
                for (int y=y1; y<=y2; ++y) {
                    board[x,y] = 1;
                }
            }
        }
        board[0,0] = 0;
        for (int i=0; i<M; ++i) {
            x1 = Math.Min(deathZones[i, 0], deathZones[i, 2]);
            y1 = Math.Min(deathZones[i, 1], deathZones[i, 3]);
            x2 = Math.Max(deathZones[i, 0], deathZones[i, 2]);
            y2 = Math.Max(deathZones[i, 1], deathZones[i, 3]);
            for (int x=x1; x<=x2; ++x) {
                for (int y=y1; y<=y2; ++y) {
                    board[x,y] = -1;
                }
            }
        }
        int INF = (int)1e9;
        int[,] V = new int[501,501];
        for (int i=0; i<=500; ++i) {
            for (int j=0; j<=500; ++j) {
                V[i,j] = INF;
            }
        }
        V[0,0] = 0;
        
        var PQ = new SortedSet<(int d, int x, int y)>();
        PQ.Add((0, 0, 0));

        while (PQ.Count > 0) {
            var top = PQ.Min;
            PQ.Remove(top);
            int d = top.d;
            int x = top.x;
            int y = top.y;
            if (V[x,y] < d) continue;

            for (int i=0; i<4; ++i) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (nx<0 || nx>500 || ny<0 || ny>500 || board[nx,ny] == -1) continue;
                int nd = d+board[nx,ny];
                if (V[nx,ny] > nd) {
                    V[nx,ny] = nd;
                    PQ.Add((nd, nx, ny));
                }
            }
        }
        if (V[500,500] != INF) {
            answer = V[500,500];
        }
        return answer;
    }
}
