import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] cmds) {
        int length = cmds.length;
        int[] answer = new int[length];
        
        for (int i=0; i<length; i++) {
            int[] temp = Arrays.copyOfRange(arr, cmds[i][0] - 1, cmds[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[cmds[i][2] - 1];
        }
        
        return answer;
    }
}