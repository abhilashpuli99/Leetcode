// Last updated: 9/2/2025, 1:44:31 PM
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    int hash[256];
    fill(hash, hash + 256, -1);  // Initialize all characters as unseen

    int maxLen = 0;
    int l = 0;  // Left boundary of window

    for (int r = 0; r < s.size(); ++r) {
        if (hash[s[r]] >= l) {
            l = hash[s[r]] + 1;  // Move left boundary past the last occurrence
        }
        hash[s[r]] = r;  // Update last seen index
        maxLen = max(maxLen, r - l + 1);  // Update max length
    }

    return maxLen;
    }
};