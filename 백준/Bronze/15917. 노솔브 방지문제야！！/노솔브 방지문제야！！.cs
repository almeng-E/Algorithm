using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;  


namespace Algorithm
{
    class Program
    {
        static void Main()
        {

            var sr = new StreamReader(Console.OpenStandardInput());
            var sw = new StreamWriter(Console.OpenStandardOutput()) { AutoFlush = false };

            int Q = int.Parse(sr.ReadLine());

            for (int i = 0; i < Q; i++)
            {
                int b = int.Parse(sr.ReadLine());

                if ((b&(-b))==b)
                {
                    sw.WriteLine(1);
                }
                else
                {
                    sw.WriteLine(0);
                }
            }
            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}