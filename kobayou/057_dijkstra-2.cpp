#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
ll MOD = 1000000007;

#define vec              vector<int>
#define vecll            vector<ll>
#define vecd             vector<double>
#define vecst            vector<string>
#define vecb             vector<bool>
#define v2(v,n,m,init)   vector<vector<int>>  v(n, vector<int>(m, init))
#define vb2(v,n,m,init)  vector<vector<bool>> v(n, vector<bool>(m, init))
#define vll2(v,n,m,init) vector<vector<ll>>   v(n, vector<ll>(m, init))

#define rep(i,n)         for(ll i=(ll)0; i<(ll)n; i++)
#define REP(i,m,n)       for(ll i=(ll)m; i<(ll)n; i++)
#define arr(var, n)      vec var(n); rep(i,n){cin >> var[i];}
#define arrll(var, n)    vecll var(n); rep(i,n){cin >> var[i];}
#define arrst(var, n)    vecst var(n); rep(i,n){cin >> var[i];}
#define all(var)         (var).begin(), (var).end()
#define sortall(var)     sort(all(var))
#define uniqueall(v)     v.erase(unique(v.begin(), v.end()), v.end());
#define pb(var)          push_back(var)
#define prt(var)         cout << (var) << "\n"
#define prtd(n, var)     cout << fixed << setprecision(n) << (var) << "\n"
#define prtfill(n, var)  cout << setw(n) << setfill('0') << (var);
#define prt2(v1, v2)     cout << (v1) << " " << (v2) << "\n"
#define prt3(v1, v2, v3) cout << (v1) << " " << (v2) << " " << (v3) << "\n"
#define prtall(v)        rep(i,v.size()){cout<<v[i]<<(i!=v.size()-1?" ":"\n");}
template <typename T>
bool chmax(T &a, const T& b){if(a<b){a=b; return true;} return false;}
template <typename T>
bool chmin(T &a, const T& b){if(a>b){a=b; return true;} return false;}
//----------------------------------------------------------------
struct Weight{
  int to;
  int weight;
  Weight(int t, int w) : to(t), weight(w) {}
};

class GraphW{

public:
  vector<vector<Weight>> graphs;
  vector<bool> check; // For DFS, Dijkstra
  vector<ll> dist;   // For BFS, Dijkstra
  int dijk_count;
  queue<int> q; // For BFS
  using P = pair<ll, int>;
  priority_queue<P, vector<P>, greater<P>> que; // For Dijkstra

  bool st_dijk;

  GraphW(int n){
    graphs.resize(n);
    init(n);
    st_dijk=true;
  }
  ~GraphW(){}

  void addedge(int a, int b, ll c){
    a--; b--;
    if(c<0){st_dijk=false;}
    graphs[a].push_back(Weight(b, c));
    graphs[b].push_back(Weight(a, c));
  }

  void addedge_cin(int m){
    rep(i,m){
      int a, b;
      ll c;
      cin >> a >> b >> c;
      addedge(a, b, c);
    }
  }

  void init(int n){
    check.resize(n, false);
    dist.resize(n, -1);
  }

  void dfs(int v){
    check[v] = true;

    for(auto next_v : graphs[v]){
      if(check[next_v.to]) continue;
      dfs(next_v.to);
    }
  }

  void dijkstra(int v)//----------------------
  {
    if(st_dijk){// start
      for(int i=0;i<dist.size(); i++){dist[i]=LONG_MAX;}
      for(int i=0;i<check.size(); i++){check[i]=false;}
      dist[v]=0;
      que.push(make_pair(0, v));
    } else {
      cout << "Dijkstra can't be applied.\n";
      return;
    }

    while(!que.empty()){
      P cur = que.top();
      que.pop();

      if(dist[cur.second]<cur.first) continue;

      for(Weight next_v : graphs[cur.second]){
        if(dist[next_v.to]>dist[cur.second]+next_v.weight){
          dist[next_v.to] = dist[cur.second]+next_v.weight;
          que.push(make_pair(dist[next_v.to], next_v.to));
        }
      }
    }
  }
};

int main(void) {
  int n, k;
  cin >> n >> k;
  GraphW g(n);
  vecll ans;
  rep(i,k){
    int type;
    cin >> type;
    if(type==1){
      g.addedge_cin(1);
    } else {
      int a, b;
      cin >> a >> b;
      g.dijkstra(a-1);
      ans.pb(g.dist[b-1]==LONG_MAX ? -1 : g.dist[b-1]);
    }
  }
  rep(i,ans.size()){
    prt(ans[i]);
  }
}
