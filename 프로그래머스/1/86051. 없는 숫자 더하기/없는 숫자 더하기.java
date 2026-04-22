class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        int[] noNumbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        
        for (int number : numbers)
            noNumbers[number] = 0;
        
        for (int number : noNumbers)
            answer += number;
        
        return answer;
    }
}