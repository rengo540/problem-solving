import java.util.Scanner;

public class BlackSquare {

    public static void main(String[] args) {
        

        Scanner input =new Scanner(System.in);

        int [] arr =new int[4];
        String word="";
int sum=0,multi=0;;

for(int i=0;i<4 ;i++)
{
    arr[i]=input.nextInt();
}

word=input.next();

        for(int i=0;i<4 ;i++)
        {int count=0;
            for(int j=0;j<word.length();j++){
                   if( i+1 ==Integer.valueOf(String.valueOf(word.charAt(j))))
                   {
                       count++;
                   }
            }
            multi=count*arr[i];
            sum+=multi;

        }

        System.out.println(sum);




    }
    
}
