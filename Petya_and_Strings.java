import java.util.Scanner;


public class Petya_and_Strings {

    
    public static void main(String[] args) {
        String s , x ; 
        Scanner input =new Scanner(System.in);

        s=input.nextLine();
        x=input.nextLine();

       s= s.toLowerCase();
        x=x.toLowerCase();

        int n = s.compareTo(x);

        if(n==0)
        {
            System.out.println(0);
            
        }else if(n>0)
        {
            System.out.println(1);

        }else{
            System.out.println(-1);

        }


        
    }


}