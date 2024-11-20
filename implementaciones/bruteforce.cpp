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
string a,b;
// se prueban todos los casos posibles
vector<int> calc(int i, int j){
    // no hay ningún prefijo que igualar
    if (i == 0 && j == 0) return {0};
    if (i == 0){
        // prefijo vacío, solo hay que insertar
        vector<int> res = calc(i,j-1);
        int k = res.size();
        for (int l = 0; l < k; l++)
            res[l] = res[l]+costo_ins(b[j-1]);
        return res;
    }
    if (j == 0){
        // prefijo vacío, solo hay que eliminar letras
        vector<int> res = calc(i-1,j);
        int k = res.size();
        for (int l = 0; l < k; l++)
            res[l] = res[l]+costo_del(a[i-1]);
        return res;
    }
    vector<int> res;
    // eliminar para igualar
    vector<int> r1 = calc(i-1,j);
    for (int c1 : r1) res.push_back(c1+costo_del(a[i-1]));
    // añadir para igualar
    vector<int> r2 = calc(i,j-1);
    for (int c2 : r2) res.push_back(c2+costo_ins(b[j-1]));
    // substitución para igualar
    vector<int> r3 = calc(i-1,j-1);
    for (int c3 : r3) res.push_back(c3+costo_sub(a[i-1],b[j-1]));
    if (i > 1 && j > 1 && (a[i-1] == b[j-2] && a[i-2] == b[j-1])){
        // transposición si es posible
        vector<int> r4 = calc(i-2,j-2);
        for (int c4 : r4) res.push_back(c4+costo_trans(a[i-1],a[i-2]));
    }
    return res;
}
void solve(){
    int n,m;
    cin >> n;
    if (n != 0) cin >> a;
    cin >> m;
    if (m != 0) cin >> b;
    vector<int> res = calc(n,m);
    // se obtiene el mínimo
    cout << *min_element(res.begin(),res.end()) << endl;
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