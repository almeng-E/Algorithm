using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main()
    {
        using (var sr = new StreamReader(Console.OpenStandardInput()))
        using (var sw = new StreamWriter(Console.OpenStandardOutput()))
        {
            string firstLine = sr.ReadLine();
            if (string.IsNullOrEmpty(firstLine)) return;

            string[] nm = firstLine.Split(' ', StringSplitOptions.RemoveEmptyEntries);
            int N = int.Parse(nm[0]);
            int M = int.Parse(nm[1]);

            int[,] map = new int[N, M];
            for (int i = 0; i < N; i++)
            {
                string line = sr.ReadLine();
                for (int j = 0; j < M; j++)
                {
                    map[i, j] = line[j] - '0';
                }
            }

            Solution sol = new Solution();
            int answer = sol.solution(N, M, map);

            sw.WriteLine(answer);
        } // using 블록 끝
    }
}

public class Solution {
    public int solution(int N, int M, int[,] board) {
        var dx = new int[]{0, 0, 1, -1};
        var dy = new int[]{1, -1, 0, 0};

        // V[x,y,횟수] = 거리
        var V = new int[N,M,2];
        for (int i=0; i<N; ++i) {
            for (int j=0; j<M; ++j) {
                for (int k=0; k<2; ++k) {
                    V[i,j,k] = -1;
                }
            }
        }
        var q = new Queue<(int x, int y, int k)>();
        q.Enqueue((0, 0, 0));
        V[0,0,0] = 1;

        while (q.Count > 0) {
            var it = q.Dequeue();
            int x = it.x;
            int y = it.y;
            int k = it.k;
            if (x == N-1 && y == M-1) {
                return V[x,y,k];
            }
            for (int i=0; i<4; ++i) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (nx<0 || nx>=N || ny<0 || ny>=M) continue;
                
                if (k == 0 && board[nx,ny] == 1 && V[nx,ny,1] == -1) {
                    V[nx,ny,1] = V[x,y,0]+1;
                    q.Enqueue((nx,ny,1));
                }
                if (board[nx,ny] == 0 && V[nx,ny,k] == -1) {
                    V[nx,ny,k] = V[x,y,k]+1;
                    q.Enqueue((nx, ny, k));
                }
            }
        }
        return -1;
    }
}