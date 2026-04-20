class Solution {
    public int solution(int num) {
        long lnum = (long) num;
        for (int i=0; i<=500; i++) {
            if (lnum == 1) return i;
            
            if (lnum % 2 == 0) {
                lnum = lnum / 2;
            } else {
                lnum = lnum * 3 + 1;
            }
        }
        
        return -1;
    }
}