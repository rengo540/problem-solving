import java.sql.Array;
import java.util.Arrays;
import java.util.HashMap;

public class Anagram {

    public boolean isAnagram(String s,String t){
        s= s.concat(t);
        HashMap<Character,Integer> dic = new HashMap<>();
        for(char i:s.toCharArray()){
            if(dic.containsKey(i)){
               dic.put(i,dic.get(i)+1);
            }else{
                dic.put(i,1);
            }
        }

        for(int i:dic.values()){
           if (i % 2!=0){
               return false;
           }
        }
        return true;

    }

    public boolean isAnagram2 (String s,String t){
        char [] ss = s.toCharArray();
        Arrays.sort(ss);
        s = new String(ss);

        char [] tt = t.toCharArray();
        Arrays.sort(tt);
        t = new String(tt);

        if(s.equals(t)) {
            return true;
        }else {
            return false;
        }
    }
}
