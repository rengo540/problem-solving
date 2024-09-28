import java.util.ArrayList;
import java.util.List;

public class CombinationSum {
    List<List<Integer>> finalRes;


    public List<List<Integer>> combinationSum1(int[] arr, int target) {
        List<Integer> res =new ArrayList<>();
        finalRes = new ArrayList<>();
        combSum1(0,target,res,arr);
        return finalRes;
    }

    public void combSum1 (int i, int target, List<Integer> res, int []arr){
        if(target==0){
            finalRes.add(new ArrayList < > (res));
            return;
        }
        if(i>=arr.length){
            return ;
        }
        if(target>=arr[i]) {
            res.add(arr[i]);
            combSum1(i, target - arr[i], res, arr);
            res.remove(res.size() - 1);
        }
        combSum1(i+1,target,res,arr);

    }

    public List<List<Integer>> combinationSum2(int[] arr, int target) {
        List<Integer> res =new ArrayList<>();
        finalRes = new ArrayList<>();
        combSum2(0,target,res,arr);
        return finalRes;
    }
    public void combSum2 (int i, int target, List<Integer> res, int []arr){
        if(target==0){
            finalRes.add(new ArrayList < > (res));
            return;
        }

        for(int j=i;j<arr.length;j++) {
            if (j > i && arr[j] == arr[j - 1]) continue;
            if (target >= arr[i]) {
                res.add(arr[j]);
                combSum2(j + 1, target - arr[j], res, arr);
                res.remove(res.size() - 1);
            } else {
                break;
            }
        }
    }
}
