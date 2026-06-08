import java.util.Arrays;

class Solution {
    public int solution(int k, int m, int[] score) {    
        int len = score.length;
        
        Arrays.sort(score);
        
        for (int i=0; i<len/2; i++) {
            int temp = score[i];
            score[i] = score[len - 1 - i];
            score[len - 1 - i] = temp;
        }
        
        int answer = 0;
        
        for (int i=m-1; i<len; i+=m)
            answer += score[i] * m;
        
        return answer;
    }
}