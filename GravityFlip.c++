
#include <cstdlib>
#include<iostream>
using namespace std;


int main() {
    
    int n ,temp=0; 
    cin >> n ;
    int* arr=new int[n] ;

    for(int i=0 ;i<n ;i++)
    {
        cin>>arr[i];
    }

    for(int i=0;i<n ;i++)
      {for(int j=i+1;j<n;j++)
        {   if(arr[i]>arr[j]){
                temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        cout<<arr[i]<<" ";
      }

    
    return 0;
}