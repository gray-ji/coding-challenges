import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        
        int length = numbers.length;
        for (int i=0; i<length-1; i++)
            for (int j=i+1; j<length; j++)
                set.add(numbers[i] + numbers[j]);
        
        int idx = 0;
        int[] answer = new int[set.size()];
        for (int num : set) answer[idx++] = num;
        
        Arrays.sort(answer);
        
        return answer;
    }
}