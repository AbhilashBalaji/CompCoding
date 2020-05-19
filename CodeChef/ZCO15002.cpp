#include <bits/stdc++.h>
typedef long long ll;
int main()
{
    ll n, k;
    std::cin >> n >> k;
    ll a[n];
    for (ll i = 0; i < n; i++)
        std::cin >> a[i];
    std::sort(a, a + n);
    ll ans = 0;
    ll j = 1;
    for (ll i = 0; i < n - 1; i++)
    {
        for (; j < n; j++)
        {
            if (a[j] - a[i] >= k)
            {
                ans += (n - j);
                break;
            }
            else
                j++;
        }
    }
    std::cout << ans;
}