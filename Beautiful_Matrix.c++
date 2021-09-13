
#include <cstdlib>
#include<iostream>
using namespace std;


int main() {
    
    int arr [5][5] , n=0  ,indexI=0 , indexJ=0 ;

    for(int i=0 ;i<5 ;i++){
        for(int x =0 ;x<5 ;x++)
           { cin>>arr[i][x];

            if( arr[i][x] ==1){
                indexI=i;   
                indexJ=x;
                }
           }  
    }

   n=abs(2-indexI)+abs(indexJ-2);
    
    cout << n <<endl ;
    


       string s ;
       string x ;
       x.compare(s);
    
    return 0;
}