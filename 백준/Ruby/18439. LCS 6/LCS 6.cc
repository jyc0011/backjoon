#include <bits/stdc++.h>
using namespace std;

using u64 = unsigned long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string A, B;
    if (!(cin >> A)) return 0;
    if (!(cin >> B)) return 0;
    string S = A, T = B;
    if (T.size() > S.size()) swap(S, T);
    const int n = (int)S.size();
    const int m = (int)T.size();
    const int W = (m + 63) >> 6;
    const int r = m & 63;
    const u64 LAST_MASK = (r == 0) ? ~0ULL : ((1ULL << r) - 1ULL);

    auto mask_last = [&](vector<u64>& v) {
        if (W) v.back() &= LAST_MASK;
    };

    array<vector<u64>, 26> pos;
    for (auto &vec : pos) vec.assign(W, 0ULL);
    for (int j = 0; j < m; ++j) {
        int c = T[j] - 'A';
        pos[c][j >> 6] |= (1ULL << (j & 63));
    }
    vector<u64> D(W, 0ULL);
    auto orV = [&](const vector<u64>& a, const vector<u64>& b) {
        vector<u64> res(W);
        for (int i = 0; i < W; ++i) res[i] = a[i] | b[i];
        return res;
    };
    auto andV = [&](const vector<u64>& a, const vector<u64>& b) {
        vector<u64> res(W);
        for (int i = 0; i < W; ++i) res[i] = a[i] & b[i];
        return res;
    };
    auto notV = [&](const vector<u64>& a) {
        vector<u64> res(W);
        for (int i = 0; i < W; ++i) res[i] = ~a[i];
        return res;
    };
    auto shl1 = [&](const vector<u64>& a) {
        vector<u64> res(W);
        u64 carry = 0ULL;
        for (int i = 0; i < W; ++i) {
            u64 n = a[i] >> 63;
            res[i] = (a[i] << 1) | carry;
            carry = n;
        }
        mask_last(res);
        return res;
    };
    auto sub_vec = [&](const vector<u64>& x, const vector<u64>& y) {
        vector<u64> res(W);
        unsigned __int128 borrow = 0;
        for (int i = 0; i < W; ++i) {
            unsigned __int128 xi = x[i];
            unsigned __int128 yi = y[i];
            unsigned __int128 diff = xi - yi - borrow;
            res[i] = (u64)diff;
            borrow = (xi < yi + borrow) ? 1 : 0;
        }
        return res;
    };

    for (int i = 0; i < n; ++i) {
        int c = S[i] - 'A';
        vector<u64> x = orV(pos[c], D);
        vector<u64> y = shl1(D);
        if (W) y[0] |= 1ULL;
        mask_last(y);
        vector<u64> tmp = sub_vec(x, y);
        vector<u64> ntmp = notV(tmp);
        vector<u64> newD = andV(x, ntmp);
        mask_last(newD);
        D.swap(newD);
    }
    long long ans = 0;
    for (int i = 0; i < W; ++i) ans += __builtin_popcountll(D[i]);
    cout << ans << '\n';
    return 0;
}