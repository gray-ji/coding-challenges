class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int p1 = 0, p2 = 0;
        
        for (String word : goal) {
            if (p1 < cards1.length && cards1[p1].equals(word)) p1++;
            else if (p2 < cards2.length && cards2[p2].equals(word)) p2++;
            else return "No";
        }
        return "Yes";
    }
}
