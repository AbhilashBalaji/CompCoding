#include <iostream>
#include <cstdio>
#include <iomanip>
#include <iterator>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <climits>

using namespace std;

#define fastio std::ios_base::sync_with_stdio(false)
#define PAUSE_EXE assert(false)
#define inchar getchar_unlocked
#define LL long long
#define MAX 1000002
#define MOD 1000000007
#define REP(i, n) for (__typeof(n) i = 0; i < n; ++i)
#define REP1(i, n) for (__typeof(n) i = 1; i <= n; ++i)
#define REP2(i, n) for (__typeof(n) i = 1; i < n; ++i)
#define CREP(i, n) for (__typeof(n) i = n - 1; i >= 0; --i)
#define CREP1(i, n) for (__typeof(n) i = n; i >= 1; --i)
#define CREP2(i, n) for (__typeof(n) i = n - 1; i >= 1; --i)
#define MYREP(i, a, b) for (__typeof(a) i = a; i <= b; ++i)
#define MYCREP(i, a, b) for (__typeof(a) i = b; i >= a; --i)
#define SET(a, b) memset(a, b, sizeof(a))
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define fi first
#define sec second
#define all(c) (c).begin(), (c).end()
#define allr(c) (c).rbegin(), (c).rend()
#define reset(c) (c).clear()
#define loop(c, i) for (typeof(c.begin()) i = c.begin(); i != c.end(); i++)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())

const double EPS = 1e-10;

template <typename T>
void inPos(T &x)
{
    register T c = inchar();
    while (((c < 48) || (c > 57)) && (c != '-'))
        c = inchar();
    x = 0;
    for (; c < 48 || c > 57; c = inchar())
        ;
    for (; c > 47 && c < 58; c = inchar())
        x = (x << 3) + (x << 1) + (c - 48);
}

template <typename T>
T max(T &a, T &b) { return (!(a < b) ? a : b); }
template <typename T>
T min(T &a, T &b) { return (a < b ? a : b); }
template <typename T>
T mod(T a, T b) { return (a < b ? a : a % b); }
LL mulmod(LL a, LL b, LL m)
{
    LL q = (LL)(((long double)a * (long double)b) / (long double)m);
    LL r = a * b - q * m;
    if (r > m)
        r %= m;
    if (r < 0)
        r += m;
    return r;
}
template <typename T>
T power(T e, T n, T m)
{
    T x = 1, p = e;
    while (n)
    {
        if (n & 1)
            x = mod(x * p, m);
        p = mod(p * p, m);
        n >>= 1;
    }
    return x;
}
template <typename T>
T InverseEuler(T a, T m) { return (a == 1 ? 1 : power(a, m - 2, m)); }
template <typename T>
T gcd(T a, T b) { return (!b) ? a : gcd(b, a % b); }
template <typename T>
T lcm(T a, T b) { return (a * (b / gcd(a, b))); }

map<LL, bool> visited;
map<LL, vector<LL>> adjacenyList;

void solve()
{
    LL n, m;
    cin >> n >> m;

    vector<LL> shortestPath;

    LL t1, t2;
    for (LL i = 0; i < m; i++)
    {
        cin >> t1 >> t2;
        adjacenyList[t1].push_back(t2);
    }
    // for (auto &&i : adjacenyList)
    // {
    //     for (auto &&j : i.second)
    //     {
    //         cout << i.first << "->" << j << endl;
    //     }
    //     // break;
    // }
    
}

int main()
{
    cin.tie(NULL);
    LL t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}