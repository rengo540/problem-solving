import java.util.Scanner;


public class Magnets {


    public static void main(String[] args) {
        Scanner input =new Scanner(System.in);


        int nOfMagnets ;
        nOfMagnets=input.nextInt();

        int count =0;


        int[] arr=new int[nOfMagnets];

        for(int i=0;i<nOfMagnets;i++){
            arr[i]=input.nextInt();

        }

        for(int i=0;i<nOfMagnets;i++)
        {
            if(i==nOfMagnets-1){break;}

            while(arr[i]!=arr[i+1])
            {
                count++;
                break;
            }
            
        }

        System.out.println(count+1);


    }
    
}
