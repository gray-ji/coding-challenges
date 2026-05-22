class Solution {
    public String solution(int[] food) {
        StringBuilder sb = new StringBuilder("0");
        
        for (int i=food.length - 1; i>0; i--) {
            int share = food[i] / 2;
            for (int j=0; j<share; j++) {
                sb.insert(0, Integer.toString(i));
                sb.append(Integer.toString(i));
            }
        }
        
        return sb.toString();
    }
}