using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        using (var sr = new StreamReader(Console.OpenStandardInput()))
        using (var sw = new StreamWriter(Console.OpenStandardOutput()))
        {
            string firstLine = sr.ReadLine();
            if (string.IsNullOrEmpty(firstLine)) return;
            int T = int.Parse(firstLine);

            Solution sol = new Solution();

            for (int t = 0; t < T; t++)
            {
                string[] nm = sr.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries);
                int N = int.Parse(nm[0]);
                int M = int.Parse(nm[1]);

                int[][] edges = new int[M][];
                for (int i = 0; i < M; i++)
                {
                    string[] edgeStr = sr.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries);
                    edges[i] = new int[] { int.Parse(edgeStr[0]), int.Parse(edgeStr[1]), int.Parse(edgeStr[2]) };
                }

                int K = int.Parse(sr.ReadLine());
                string[] friendsStr = sr.ReadLine().Split(' ', StringSplitOptions.RemoveEmptyEntries);
                int[] friends = new int[K];
                for (int i = 0; i < K; i++)
                {
                    friends[i] = int.Parse(friendsStr[i]);
                }
                
                int answer = sol.solution(N, edges, friends);
                sw.WriteLine(answer);
            }
        } // using 블록 끝
    }
}

public class Solution 
{
    public int solution(int N, int[][] edges, int[] friends) 
    {
        int INF = (int)1e9;
        var V = new int[N][];
        for (int i=0; i<N; ++i) {
            V[i] = new int[N];
            for (int j=0; j<N; ++j) {
                V[i][j] = INF;
            }
            V[i][i] = 0;
        }
        
        for (int m = 0; m < edges.Length; ++m) {
            int a = edges[m][0];
            int b = edges[m][1];
            int w = edges[m][2];

            V[a-1][b-1] = w;
            V[b-1][a-1] = w;
        }

        for (int k=0; k<N; ++k) {
            for (int a=0; a<N; ++a) {
                for (int b=0; b<N; ++b) {
                    V[a][b] = Math.Min(V[a][b], V[a][k]+V[k][b]);
                }
            }
        }

        int tgRoom = -1;
        int minDist = INF;
        for (int rn=0; rn<N; ++rn) {
            int tmp=0;
            foreach (int st in friends) {
                tmp += V[st-1][rn];
            }
            if (minDist > tmp) {
                minDist = tmp;
                tgRoom = rn;
            }
        }
        
        return tgRoom+1;
    }
}