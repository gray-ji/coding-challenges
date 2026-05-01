class Solution {
    public int[] solution(int n, int m) {
        int a = n, b = m, t = b;
        
        while (a % b > 0) {
            b = a % b;
            a = t;
            t = b;
        }
        
        return new int[] {b, n * m / b};
    }
}