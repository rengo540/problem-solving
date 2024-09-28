import java.util.HashMap;

public class DuplicateInteger {
    private HashMap<Integer,Integer> dic;
    public DuplicateInteger(){
        dic = new HashMap<>();
    }
    public boolean isDuplicate(int [] arr){
        for(int num :arr){
            if (dic.containsKey(num)){
                return true;
            }else {
                dic.put(num,1);
            }
        }
        return false;
        
    }
}
