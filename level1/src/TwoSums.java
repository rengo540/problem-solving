import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class TwoSums {

    public ArrayList<Integer> twoSum (int [] arr,int target){
        HashMap<Integer,Integer> dic = new HashMap<>();
        for(int i = 0; i <arr.length ; i++) {
            if(dic.containsKey(arr[i])) {
                ArrayList<Integer> returnedList = new ArrayList<>();
                returnedList.add(i);
                returnedList.add(dic.get(arr[i]));
                return returnedList;
            }else {
                int sub = target - arr[i];
                dic.put(sub,i);
            }
        }
        return null;

    }
}



