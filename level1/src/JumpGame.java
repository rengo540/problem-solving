public class JumpGame {


    public boolean jumpGame1(int [] nums){
        int maxJumps = nums[0];
        int index = 0 ;
        int n = nums.length;
        while (index<n){
            if(index==n-1){
                return true;
            }
            int maxvalue = 0 ;
            int maxI = 0;
            if(maxJumps==0){
                return false;
            }
            for(int j=maxJumps+index;j>index;j--){
                if(nums[j]>=maxvalue){
                    maxvalue=nums[j];
                    maxI = j ;
                }
            }

            index = maxI;
            maxJumps=nums[maxI];
        }
        return false;
    }
}
