// Last updated: 9/2/2025, 1:44:19 PM
bool isPalindrome(int x)
{
long long sum=0,ld,on=x;
    while(x>0)
    {
        ld=x%10;
        sum=sum*10+ld;
        x=x/10;        
    }
    if (sum==on)
        return true;
    return false;
}
