import java.util.PriorityQueue;

class Solution {
    public int[] solution(int k, int[] scores) {
        int length = scores.length;
        int[] answer = new int[length];
        PriorityQueue<Integer> top = new PriorityQueue<>();
        
        for (int i=0; i<length; i++) {
            top.add(scores[i]);
            if (top.size() > k) top.poll();
            answer[i] = top.peek();
        }
        
        return answer;
    }
}