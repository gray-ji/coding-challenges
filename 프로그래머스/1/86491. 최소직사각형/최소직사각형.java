class Solution {
    public int solution(int[][] sizes) {
        int w = 1, h = 1;
        
        for (int[] size : sizes) {
            int x = Math.max(size[0], size[1]);
            int y = Math.min(size[0], size[1]);
            
            w = (x > w) ? x : w;
            h = (y > h) ? y : h;
        }
        
        return w * h;
    }
}