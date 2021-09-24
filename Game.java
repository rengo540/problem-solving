import java.util.Scanner;

public class Game {


    public static void main(String[] args) {
        
        Scanner input =new Scanner(System.in);

        int teams,count=0 ;
        teams=input.nextInt();


        int [] arr=new int [teams*2];

        for(int i=0;i<teams*2;i++)
        {
            arr[i]=input.nextInt();
        }

        for(int i=0;i<teams*2;i++)
        {
            for(int j=0;j<teams*2;j++)
            {
                if(arr[i]==arr[j] && i%2 != j%2 )
                   { count++;
                   }
                }
            }
        

System.out.println(count-(count/2));



    }


}