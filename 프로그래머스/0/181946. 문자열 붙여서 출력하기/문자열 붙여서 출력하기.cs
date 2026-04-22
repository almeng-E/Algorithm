using System;
using System.Collections.Generic;

public class Example
{
    public static void Main()
    {
        String[] input;

        Console.Clear();
        input = Console.ReadLine().Split(' ');

        String s1 = input[0];
        String s2 = input[1];

        String ans = s1+s2;
        Console.WriteLine(ans);
        
    }
}