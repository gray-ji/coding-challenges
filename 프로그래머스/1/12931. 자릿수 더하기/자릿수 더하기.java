import java.util.*;

public class Solution {
    public int solution(int n) {
        String nStr = Integer.toString(n);
        int answer = 0;
                   
        for (int i=0; i<nStr.length(); i++)
            answer += Character.getNumericValue(nStr.charAt(i));

        return answer;
    }
}