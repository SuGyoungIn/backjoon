import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
class Solution {
    public int solution(int[][] maps) {
        int answer = bfs(maps);
        return answer;
    }
    public int bfs(int[][] maps){
        int n = maps.length;
        int m = maps[0].length;
        Deque<int[]> deq = new ArrayDeque<>();
        deq.offer(new int[]{0,0,1});
        int[][] d = {{1,0},{0,1},{-1,0},{0,-1}};
        while (!deq.isEmpty()){
            int[] now = deq.poll();
            if(now[0] == n-1 && now[1] == m-1){
                return now[2];
            }
            for (int i = 0; i < 4;i++){
                int[] dd = d[i];
                int ni = now[0]+dd[0];
                int nj = now[1]+dd[1];
                if (ni >= 0 && ni < n && nj>= 0 && nj < m && maps[ni][nj] == 1){
                    maps[ni][nj] = 0;
                    deq.offer(new int[]{ni,nj,now[2]+1});
                }
            }
            
        }
        return -1; 
    }
}