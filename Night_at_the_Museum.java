import java.util.Scanner;


public class Night_at_the_Museum {

    public static void main(String[] args) {
        
        Scanner input =new Scanner(System.in); 
    
        String movie="" ;
        int sum=0, c=0;
        movie=input.next();

if(movie.length()==1)
{
        c = movie.charAt(0)-'a';
                if(c>13)
           {
               c=26-c;
           }
                sum+=c;

}else{

        for(int i =0;i<movie.length()-1;i++)
        {
            if(i==0)
            {
                 c = movie.charAt(i)-'a';
                  if(c>13)
                    {
                        c=26-c;
                    }
                sum+=c;
                

            }


           int c1 =movie.charAt(i+1)-movie.charAt(i);

           if(c1>13)
           {
               c1=26-c1;
           }else if (c1<-13)
           {
               c1=26+c1;

           }
          c1= Math.abs(c1);

          sum=sum+c1;
        }
    }

        System.out.println(sum);



    
    }

}
