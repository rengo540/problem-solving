import java.util.Scanner;
import java.util.Stack;

public class Police_Recruits {

    public static void main(String[] args) {
        

        Scanner input =new Scanner(System.in);

        int n,hired=0,count=0;  
        n=input.nextInt();

        

        for(int i=0 ;i<n;i++)
        {
            int x ;
            x=input.nextInt();
            if(x>0)
            {
                hired+=x;
                continue;
            }else if(x<0 && hired>0)
            {
                hired--;
                continue;
            }
            else if(x<0)
            {
                count++;
                continue;
            }

           
        }


        System.out.println(count);




       
        

    }
    
}
