class Solution {
    public String solution(String s) {
        char[] carr = s.toCharArray();
        int idx = 0;
        
        for (int i=0; i<carr.length; i++) {
            char c = carr[i];
            
            if (c == ' ') {
                idx = 0;
                continue;
            }
            
            carr[i] = (idx++ % 2 == 0)
                ? Character.toUpperCase(c) : Character.toLowerCase(c);
        }
        
        return new String(carr);
    }
}