#include <bits/stdc++.h>
using namespace std;
 
struct T{
    int S, E, idx;
    char ans;
}arr[1000];
 
bool cmp1(T a, T b){return a.S <= b.S;}
bool cmp2(T a, T b){return a.idx <= b.idx;}
 
int main(){
    for(int i = 0; i < 1000; ++i)arr[i].idx = i;
    int t;
    cin >> t;
    for(int c = 1; c <= t; ++c){
        int n;
        cin >> n;
        for(int i = 0; i < n; ++i)cin >> arr[i].S >> arr[i].E;
        sort(arr, arr+n, cmp1);
        int L1 = 0, L2 = 0;
        bool can = 1;
        for(int i = 0; i < n; ++i){
            if(L1 <= arr[i].S){
                arr[i].ans = 'C';
                L1 = arr[i].E;
            }else if(L2 <= arr[i].S){
                arr[i].ans = 'J';
                L2 = arr[i].E;
            }else{
                can = 0;
                break;
            }
        }
        sort(arr, arr+n, cmp2);
        cout << "Case #" << c << ": ";
        if(can == 0)cout <<"IMPOSSIBLE\n";
        else{
            for(int i = 0; i < n; ++i)cout << arr[i].ans;
            cout << endl;
        }
    }
    return 0;
}