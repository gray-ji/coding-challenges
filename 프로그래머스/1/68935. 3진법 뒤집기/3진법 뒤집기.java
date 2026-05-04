import java.util.*;

class Solution {
    public int solution(int n) {
        String sn = "";
        
        while (n > 0) {
            sn += n % 3;
            n /= 3;
        }
        
        return Integer.parseInt(sn, 3);
    }
}