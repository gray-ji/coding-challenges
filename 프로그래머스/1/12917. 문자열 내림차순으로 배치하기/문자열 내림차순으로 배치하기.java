import java.util.*;

class Solution {
    public String solution(String s) {
        String[] sarr = s.split("");
        Arrays.sort(sarr, Collections.reverseOrder());

        return String.join("", sarr);
    }
}