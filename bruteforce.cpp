#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
// mapa para guardar las distancias
map<int,int> dist;
// mapa para indexar las cadenas
map<string,int> tr;
// mapa para recuperar la cadena, dado el índice
map<int,string> v1;
// marcar aquellas cadenas que ya han sido visitadas
map<int,bool> vis;
// abecedario
string v2 = "abcdefghijklmnopqrstuvwxyz";
// contador para el índice
int cnt = 0;
// número grande para representar el infinito
const int inf = INT_MAX;
// función que asigna un índice a una cadena,
// o recupera su índice
int get_id(string & s){
    if (tr.find(s) == tr.end()){
        v1[cnt] = s;
        dist[cnt] = inf;
        tr[s] = cnt++;    
    }
    return tr[s];
}
// funciones de costo
int costo_trans(char a, char b){
    return 1;
}
int costo_sub(char a, char b){
    if (a == b) return 0;
    return 2;
}
int costo_del(char a){
    return 1;
}
int costo_ins(char b){
    return 1;
}
void solve(){
    string a,b;
    cin >> a >> b;
    // iniciando dijkstra, uso set en lugar de priority_queue, debido a la constante
    int c1 = get_id(a), c2 = get_id(b);
    dist[c1] = 0;
    set<pair<int,int>> q;
    q.insert({0,c1});
    while (!q.empty()){
        int p = q.begin()->second;
        q.erase(q.begin());
        if (p == c2){
            cout << dist[c2] << endl;
            break;
        }
        if (vis[p]) continue;
        vis[p] = 1;
        string cur = v1[p];
        int sz = cur.size();
        // relizar operación de transpocision
        for (int i = 1; i < sz; i++){
            swap(cur[i-1],cur[i]);
            int c4 = get_id(cur);
            if (dist[c4] > dist[p]+costo_trans(cur[i-1],cur[i])){
                dist[c4] = dist[p]+costo_trans(cur[i-1],cur[i]);   
                q.insert({dist[c4],c4});
            }
            swap(cur[i-1],cur[i]);
        }
        // relizar operación de substitucion
        for (int i = 0; i < sz; i++)
            for (int j = 'a'; j <= 'z'; j++){
                char rb = cur[i];
                cur[i] = j;
                int c4 = get_id(cur);
                if (dist[c4] > dist[p]+costo_sub(rb,j)){
                    dist[c4] = dist[p]+costo_sub(rb,j);   
                    q.insert({dist[c4],c4});
                }
                cur[i] = rb;
            }
        // relizar operación de eliminación
        for (int i = 0; i < sz; i++){
            string rb = cur.substr(i,1);
            cur.erase(i,1);
            int c4 = get_id(cur);
            if (dist[c4] > dist[p]+costo_del(rb[0])){
                dist[c4] = dist[p]+costo_del(rb[0]);   
                q.insert({dist[c4],c4});
            }
            cur.insert(i,rb);
        }
        // relizar operación de inserción
        for (int i = 0; i <= sz; i++){
            for (int j = 0; j < 26; j++){
                string rb = v2.substr(j,1);
                cur.insert(i,rb);
                int c4 = get_id(cur);
                if (dist[c4] > dist[p]+costo_ins(rb[0])){
                    dist[c4] = dist[p]+costo_ins(rb[0]);   
                    q.insert({dist[c4],c4});
                }
                cur.erase(i,1);
            }
        }
    }
}
signed main(){
    // optimización para la lectura del input
    ios_base::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
    int t = 1;
    // cin >> t;
    while (t--)
        solve();
    return 0;
}