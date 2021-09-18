import java.util.Scanner;

public class Stones_on_the_Table {
    public static void main(String[] args) {
        
Scanner input =new Scanner(System.in);

        int n ,count=0;
        n=input.nextInt();

        String word ;
        word=input.next();


        for(int i=0;i<n-1 ;i++)
        {
            

            if(word.charAt(i)==word.charAt(i+1)){
                count++;
            }
        }

        System.out.println(count);




    }
    
}
