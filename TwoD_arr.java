import java.util.ArrayList;
import java.util.List;

public class TwoD_arr {

public static void main(String[] args) {
    

}

public static int hourglassSum(List<List<Integer>> arr) {
    
    int max =0 ; 
    
    List<List<Integer>> subArr =new ArrayList<>();

    for(int i =0 ; i<6 ; i++ )
    {
        for(int j =0 ;j<6 ;j++)
        {
            subArr.set(i, arr.get(i));

        }

        
    }
    

    


    return max ;
}
}
