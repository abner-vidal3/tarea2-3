#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define pii pair<int,int>
#define vvi vector<vector<int>>
const int inf = 1e9;
// implementación de las funciones de costo
int costo_sub(char a, char b){
    if (a == b) return 0;
    return 2;
}
int costo_ins(char b){
    return 1;
}
int costo_del(char a){
    return 1;
}
int costo_trans(char a, char b){
    return 1;
}
void solve(){
    string a,b;
    int n,m;
    cin >> n;
    if (n != 0) cin >> a;
    cin >> m;
    if (m != 0) cin >> b;
    vector<vector<int>> dp(n+1,vector<int>(m+1,inf));
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= m; j++){
            // caso base
            if (i == 0 && j == 0){
                dp[i][j] = 0;
                continue;
            }
            // prefijos vacíos
            if (i == 0) {
                dp[i][j] = min(dp[i][j],dp[i][j-1]+costo_ins(b[j-1]));
                continue;
            }
            if (j == 0) {
                dp[i][j] = min(dp[i][j],dp[i-1][j]+costo_del(a[i-1]));
                continue;
            }
            dp[i][j] = inf;
            // eliminar
            dp[i][j] = min(dp[i][j],dp[i-1][j]+costo_del(a[i-1]));
            // insertar
            dp[i][j] = min(dp[i][j],dp[i][j-1]+costo_ins(b[j-1]));
            // modificar
            dp[i][j] = min(dp[i][j],dp[i-1][j-1]+costo_sub(a[i-1],b[j-1]));
            // swap
            if (i > 1 && j > 1 && (a[i-1] == b[j-2] && a[i-2] == b[j-1]))
                dp[i][j] = min(dp[i][j],dp[i-2][j-2]+costo_trans(a[i-1],a[i-2])); 
        }
    cout << dp[n][m] << endl;
}
signed main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    int t = 1;
    // cin >> t;
    while (t--)
        solve();
    return 0;
}