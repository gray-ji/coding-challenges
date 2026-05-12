class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder(s);
        
        for (int i=0; i<sb.length(); i++) {
            char c = sb.charAt(i);
            if (c != ' ') {
                int ia = Character.isUpperCase(c) ? (int) 'A' : (int) 'a';
                c = (char) (((int) c + n - ia) % 26 + ia);
            }
            
            sb.setCharAt(i, c);
        }
        
        return sb.toString();
    }
}