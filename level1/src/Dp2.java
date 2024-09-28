import java.lang.reflect.Array;
import java.util.Arrays;

public class Dp2 {


    public int lcs(String text1,String text2){
        int n = text1.length();
        int m = text2.length();
        int [][] mem = new int[n][m];
        for(int i=0;i<n;i++) {
            Arrays.fill(mem[i], -1);
        }
        return topDownSovle(n-1,m-1,mem,text1,text2);
    }

    private int topDownSovle(int i,int j,int[][] mem,String text1,String text2){
        if(i <0 || j<0){
            return 0;
        }
        if(mem[i][j] !=-1){
            return mem[i][j];
        }
        if(text1.charAt(i) == text2.charAt(j)){
            return mem[i][j]=1+topDownSovle(i-1,j-1,mem,text1,text2);
        }else{
            return mem[i][j]=Math.max(topDownSovle(i-1,j,mem,text1,text2),topDownSovle(i,j-1,mem,text1,text2));
        }
    }

    private int bottomUpSovle(String text1,String text2){
        int n = text1.length();
        int m = text2.length();
        int [][] mem = new int[n+1][m+1];

        for(int i=0;i<n+1;i++){
            for(int j=0 ;j<m+1;j++) {
                if (i == 0 || j == 0) {
                    mem[i][j] = 0;
                } else {
                    if (text1.charAt(i) == text2.charAt(j)) {
                        mem[i][j] = mem[i - 1][j - 1] + 1;
                    } else {
                        mem[i][j] = Math.max(mem[i - 1][j], mem[i][j - 1]);
                    }
                }

            }
        }
        return mem[n][m];

    }




}
