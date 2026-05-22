import java.util.*;

class Solution {
    public static int n, m, r, c, k;
    public static char[] dir = {'d', 'l', 'r', 'u'};
    public static int[] dx = {1, 0, 0, -1}; // d, u
    public static int[] dy = {0, -1, 1, 0}; // l, r


    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        this.n = n; this.m = m; this.r = r; this.c = c; this.k = k;
        
        StringBuilder sb = new StringBuilder();
        
        if(backTrack(x, y, sb))
            return sb.toString();
        else
            return "impossible";
    }
    
    public static boolean backTrack(int x, int y, StringBuilder sb) {
        if(sb.length() == k)
            return x == r && y == c;
        
        int remain = k - sb.length();
        int dist = Math.abs(x - r) + Math.abs(y - c);
        
        // 가지치기 1: 남은 칸수보다 목적지가 더 멀 때
        if(remain < dist)
            return false;
        
        // 가지치기 2: 남은 칸수의 거리의 홀짝이 다를 때 (도달x)
        // 목적지까지 최단 거리 dist에 도달한 뒤 남은 칸수를 소진하려면 왔다갔다(+2씩)를 
        // 반복해야 하므로 (remain - dist)가 반드시 짝수여야 한다
        if((remain - dist) % 2 != 0)
            return false;
        
        for(int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx >= 1 && ny >= 1 && nx <= n && ny <= m) {
                sb.append(dir[i]);
                
                if(backTrack(nx, ny, sb))
                    return true;
                
                sb.deleteCharAt(sb.length() - 1); // 마지막 문자 삭제로 백트래킹
            }
        }
        
        return false;
    }
}