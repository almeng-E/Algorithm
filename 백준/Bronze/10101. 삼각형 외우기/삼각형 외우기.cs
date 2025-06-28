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


            int a = int.Parse(sr.ReadLine());
            int b = int.Parse(sr.ReadLine());
            int c = int.Parse(sr.ReadLine());

            if (a == 60 && b == 60 && c == 60)
            {
                sw.WriteLine("Equilateral");
            }
            else if (a + b + c == 180)
            {
                if (a == b || b == c || c == a)
                {
                    sw.WriteLine("Isosceles");
                }
                else
                {
                    sw.WriteLine("Scalene");
                }
            }
            else
            {
                sw.WriteLine("Error");
            }




            sw.Flush();
            sw.Close();
            sr.Close();
        }
    }
}