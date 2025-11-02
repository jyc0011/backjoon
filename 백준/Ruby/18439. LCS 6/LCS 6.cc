#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <algorithm>
#include <numeric>
#include <cstdint> 
#include <stdexcept>

using std::cin;
using std::cout;
using std::string;
using std::vector;
using std::array;
using std::swap;

using u64 = uint64_t;

inline int popcount64(u64 x) {
    int count = 0;
    while (x != 0) {
        x &= (x - 1);
        count++;
    }
    return count;
}

struct BigBitset {
    vector<u64> blocks;
    u64 lastMask;
    int numWords;
    BigBitset() : lastMask(0), numWords(0) {}
    BigBitset(int bits, u64 mask) 
        : numWords((bits + 63) / 64), lastMask(mask) {
        blocks.assign(numWords, 0ULL);
    }
    
    BigBitset(vector<u64>&& b, u64 mask) 
        : blocks(std::move(b)), lastMask(mask), numWords(blocks.size()) {}
    void maskLast() {
        if (numWords > 0) {
            blocks.back() &= lastMask;
        }
    }
    BigBitset operator|(const BigBitset& other) const {
        vector<u64> res(numWords);
        for (int i = 0; i < numWords; ++i) {
            res[i] = blocks[i] | other.blocks[i];
        }
        return BigBitset(std::move(res), lastMask);
    }
    BigBitset operator&(const BigBitset& other) const {
        vector<u64> res(numWords);
        for (int i = 0; i < numWords; ++i) {
            res[i] = blocks[i] & other.blocks[i];
        }
        return BigBitset(std::move(res), lastMask);
    }
    BigBitset operator~() const {
        vector<u64> res(numWords);
        for (int i = 0; i < numWords; ++i) {
            res[i] = ~blocks[i];
        }
        BigBitset result(std::move(res), lastMask);
        result.maskLast();
        return result;
    }

    BigBitset operator<<(int shift) const {
        if (shift != 1) {
            throw std::runtime_error("Only shift-by-1 is implemented");
        }
        vector<u64> res(numWords, 0ULL);
        u64 carry = 0ULL;
        for (int i = 0; i < numWords; ++i) {
            u64 nextCarry = blocks[i] >> 63;
            res[i] = (blocks[i] << 1) | carry;
            carry = nextCarry;
        }
        BigBitset result(std::move(res), lastMask);
        result.maskLast();
        return result;
    }

    BigBitset operator-(const BigBitset& other) const {
        vector<u64> res(numWords);
        bool borrow = false;
        for (int i = 0; i < numWords; ++i) {
            u64 x = blocks[i];
            u64 y = other.blocks[i];
            u64 diff_no_borrow = x - y;
            res[i] = diff_no_borrow - borrow;
            bool next_borrow = (x < y) || (borrow && (x == y));
            borrow = next_borrow;
        }
        return BigBitset(std::move(res), lastMask);
    }
    
    void setBit(int i) {
        int wordIndex = i / 64;
        int bitIndex = i % 64;
        if (wordIndex < numWords) {
            blocks[wordIndex] |= (1ULL << bitIndex);
        }
    }
    
    int popcount() const {
        int count = 0;
        for (u64 block : blocks) {
            count += popcount64(block);
        }
        return count;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string A, B;
    if (!(cin >> A)) return 0;
    if (!(cin >> B)) return 0;
    string S = A, T = B;
    if (T.size() > S.size()) {
        swap(S, T);
    }
    const int n = (int)S.size();
    const int m = (int)T.size();
    if (m == 0) {
        cout << "0\n";
        return 0;
    }
    const int numWords = (m + 63) / 64;
    const int lastBlockBits = m % 64;
    const u64 LAST_MASK = (lastBlockBits == 0) ? ~0ULL : ((1ULL << lastBlockBits) - 1ULL);
    array<BigBitset, 26> charPosMasks;
    for (int i = 0; i < 26; ++i) {
        charPosMasks[i] = BigBitset(m, LAST_MASK);
    }
    for (int j = 0; j < m; ++j) {
        int c = T[j] - 'A';
        charPosMasks[c].blocks[j / 64] |= (1ULL << (j % 64));
    }
    BigBitset dpMask(m, LAST_MASK);
    for (int i = 0; i < n; ++i) {
        int c = S[i] - 'A';
        BigBitset x = charPosMasks[c] | dpMask;
        BigBitset y = dpMask << 1;
        y.setBit(0);
        BigBitset tmp_diff = x - y;
        BigBitset newDpMask = x & (~tmp_diff);
        dpMask = newDpMask;
    }
    cout << dpMask.popcount() << '\n';
    return 0;
}