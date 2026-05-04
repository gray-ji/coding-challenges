import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList<Integer> nList = new ArrayList<>();
        
        while (n > 0) {
            nList.add(n % 3);
            n /= 3;
        }
        
        int idx = nList.size() - 1;
        for (int i=0; i<=idx; i++) {
            answer += nList.get(idx - i) * Math.pow(3, i);
        }
        
        return answer;
    }
}