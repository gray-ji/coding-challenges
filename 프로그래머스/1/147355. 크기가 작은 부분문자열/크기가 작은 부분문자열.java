class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int plen = p.length();
        
        for (int i=0; i<t.length() - plen + 1; i++)
            if (t.substring(i, i + plen).compareTo(p) <= 0)
                answer += 1;
        
        return answer;
    }
}