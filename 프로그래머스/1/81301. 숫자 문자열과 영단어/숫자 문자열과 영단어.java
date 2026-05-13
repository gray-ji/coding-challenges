class Solution {
    public int solution(String s) {
        StringBuilder sb = new StringBuilder(s);
        String[] words = new String[] {
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
        };
        
        for (int i=0; i<words.length; i++) {
            int idx = sb.indexOf(words[i]);
            
            while (idx != -1) {
                sb.replace(idx, idx + words[i].length(), Integer.toString(i));
                idx = sb.indexOf(words[i], idx+1);
            }
        }
        
        return Integer.parseInt(sb.toString());
    }
}