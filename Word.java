import java.util.Scanner;

public class Word {
    public static void main(String[] args) {
        Scanner input =new Scanner(System.in);

        String word="" ;
        word=input.next();

        int upperString =0;
        int lowerString =0;

        String x;

        for(int i=0;i<word.length();i++)
        {
            x=String.valueOf(word.charAt(i));

            if(x == x.toUpperCase())
            {
                upperString ++ ;
            }
            else
            {
                lowerString ++ ;
            }
            
        }


        
         if(upperString>lowerString)
        {
           word= word.toUpperCase();
        }else{
           word= word.toLowerCase();
        }

        System.out.println(word);


    }
    
}
