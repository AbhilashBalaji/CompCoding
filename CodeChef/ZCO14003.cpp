#include <bits/stdc++.h>
typedef long long ll;
int main()
{
    ll n;
    std::cin>>n;
    ll a[n];
    for(ll i =0;i<n;i++)
        std::cin>>a[i];
    std::sort(a,a+n);
    ll max =0;
    for (ll i = 0; i < n; i++)
    {
        ll temp = a[i] *(n-i);
        if (max <temp)
            max = temp;
    }
    std::cout<<max;
    

}