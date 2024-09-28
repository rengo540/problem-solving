import java.util.HashMap;

public class SlidingWindow {

    public int longestRepeatingCharReplacement(String s,int k){
        int left=0,right = 0, longestSub = 0 ;
        HashMap<Character,Integer> dic = new HashMap<>();

        while(right<s.length()){
            if(dic.containsKey(s.charAt(right))){
                int value =dic.get(s.charAt(right));
                dic.replace(s.charAt(right),++value);
            }else {
                dic.put(s.charAt(right),1);
            }

            int mostFreqChar = dic.values().stream().max(Integer::compare).get();
            int windowSize = ((right-left)+1);
            if( windowSize- mostFreqChar >k){
                int firstChar = dic.get(s.charAt(left));
                dic.put(s.charAt(left),--firstChar);
                left++;
            }else {
                longestSub =windowSize;
            }
            right++;
        }
        return longestSub;
    }


    public int longestSubstringNoRepeapting(String s){
        HashMap<Character,Integer> dic = new HashMap<>();
        int left=0 ,right = 0,max = 0 ;
        while(left<s.length() ){
           if(right<s.length()) {
               if (dic.containsKey(s.charAt(right))) {
                   left += 1;
                   right = left;
                   dic.clear();
               } else {
                   dic.put(s.charAt(right), 1);
                   max = Math.max(max, dic.size());
                   right += 1;
               }
           }else {
               left += 1;
               right = left;
               dic.clear();
           }
        }
        return max;
    }
}
