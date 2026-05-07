class Solution {
    public int solution(int[] number) {
        int answer = 0;
        int length = number.length;
        
        for (int a=0; a<length-2; a++)
            for (int b=a+1; b<length-1; b++)
                for (int c=b+1; c<length; c++)
                    if (number[a] + number[b] + number[c] == 0)
                        answer += 1;
        
        return answer;
    }
}