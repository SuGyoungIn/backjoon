class Solution {
    public String solution(String my_string) {
        String answer = "";
        String[] str = my_string.split("");
        for (int i = 0; i < str.length; i++){
            String s = str[i];
            String tmp = (s == s.toUpperCase()) ? s.toLowerCase() : s.toUpperCase();
            answer += tmp;
        }
        return answer;
    }
}