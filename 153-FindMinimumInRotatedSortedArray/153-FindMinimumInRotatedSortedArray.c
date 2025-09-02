// Last updated: 9/2/2025, 1:42:54 PM
int min_value(int a,int b)
{
    return (a<b?a:b);
}
int findMin(int* arr, int n) {
    int min_val=arr[0];
    int low=0;
    int high=n-1;
    int mid;
    while(low<=high)
    { 
            mid=low+(high-low)/2;
        if(arr[low]<=arr[mid])
        {
            min_val=min_value(min_val,arr[low]);
            low=mid+1;
        }
        else
        {
            min_val=min_value(min_val,arr[mid+1]);
            high=mid;
        }
    }
    return min_val;
    
}
