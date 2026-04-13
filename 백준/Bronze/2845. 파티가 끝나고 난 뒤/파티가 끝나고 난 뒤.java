import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt() * sc.nextInt();
        
        int[] num = new int[5];
        for (int i=0; i<5; ++i){
            num[i] = sc.nextInt();
        }
        sc.close();

        for (int i=0; i<5; ++i){
            num[i] -= x;
        }

        for (int i=0; i<5; ++i){
            System.out.print(num[i] + " ");
        }
    }
}