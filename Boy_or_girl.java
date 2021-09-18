import java.util.Scanner;

public class Boy_or_girl {



    public static void main(String[] args) {
    

        Scanner input =new Scanner(System.in);
        String username ; 
        int n=0;
        username=input.next();

        String temp ="";
      for(int i=0;i<username.length();i++){  
      
        if(!temp.contains(String.valueOf(username.charAt(i)))){
           
            temp=temp+username.charAt(i);

        }
        
    }
      

       if((temp.length())%2==0)
       {
           System.out.println("CHAT WITH HER!");
       }        else
       {
           System.out.println("IGNORE HIM!");
       }

}
}
