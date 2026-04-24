using System;
using System.Collections.Generic;
using System.Linq;


public class Solution {
    int[] dx = new int[]{0, 0, 1, -1};
    int[] dy = new int[]{1, -1, 0, 0};
    public int[] solution(string[,] places) {
        int[] answer = new int[5];
        for (int i=0; i<5; ++i) {
            string[] board = new string[5];
            for(int j=0; j<5; ++j) {
                board[j] = places[i,j];
            }
            answer[i] = check(board);
        }
        return answer;
    }
    
    public int check(string[] board){
        int nx, ny;
        for (int x=0; x<5; ++x) {
            for (int y=0; y<5; ++y) {
                // 사람 P
                if (board[x][y] == 'P'){
                    for (int d=0; d<4; ++d) {
                        nx = x+dx[d];
                        ny = y+dy[d];
                        if (nx<0 || nx>=5 || ny<0 || ny>=5) continue;
                        if (board[nx][ny] == 'P') return 0;
                    }
                }
                // 빈 테이블 O
                else if (board[x][y] == 'O'){
                    int cnt = 0;
                    for (int d=0; d<4; ++d) {
                        nx = x+dx[d];
                        ny = y+dy[d];
                        if (nx<0 || nx>=5 || ny<0 || ny>=5) continue;
                        if (board[nx][ny] == 'P') cnt++;
                    }
                    if (cnt>=2) return 0;
                }
            }
        }
    return 1;
    }
}