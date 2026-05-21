import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        
        Map<String, Integer> map = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            String key = Character.toString(s.charAt(i));
            
            if (map.containsKey(key)) answer[i] = i - map.get(key);
            else answer[i] = -1;
            
            map.put(key, i);
        }
        
        return answer;
    }
}