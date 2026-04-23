using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));

    static int ReadInt()
    {
        int ret = 0;
        int c = sr.Read();
        while (c <= 32)
        {
            if (c == -1) return 0; // 파일의 끝(EOF)
            c = sr.Read();
        }
        do
        {
            ret = ret * 10 + (c - '0');
            c = sr.Read();
        } while (c > 32);
        
        return ret;
    }

    static void Main(string[] args)
    {
        int N = ReadInt();
        int M = ReadInt();

        int[] lights = new int[N];
        for (int i = 0; i < N; i++)
        {
            lights[i] = ReadInt();
        }

        int LEN = 1;
        while (LEN < N) {
            LEN <<= 1;
        }
        int SIZE = LEN << 1;

        int[] tree = new int[SIZE];
        for (int i=0; i<N; ++i){
            tree[i+LEN] = lights[i];
        }
        for (int i=LEN-1; i>0; --i) {
            tree[i] = Math.Max(tree[i*2], tree[i*2 + 1]);
        }

        var ans = new List<int>();
        
        for (int mid=M-1; mid<N-M+1; ++mid) {
            int l = mid-M+1 + LEN;
            int r = mid+M-1 + LEN;
            
            int max = 0;

            while (l <= r) {
                if (l%2 == 1) {
                    max = Math.Max(max, tree[l]);
                    l += 1;
                }
                if (r%2 == 0) {
                    max = Math.Max(max, tree[r]);
                    r -= 1;
                }
                l >>= 1;
                r >>= 1;
            }
            ans.Add(max);
        }
        Console.WriteLine(string.Join(" ", ans));       
        
    }
}