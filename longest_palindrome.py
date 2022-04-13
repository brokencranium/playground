# find the longest palindrome in a string by comparing the center of the string
# with the center of the substring

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        max_len = 1
        start = 0
        for i in range(len(s)):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                start = i - max_len
                max_len += 1

        return s[start:start + max_len]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome(""))
    print(s.longestPalindrome("bb"))
    print(s.longestPalindrome("babadada"))
    print(s.longestPalindrome("babadadaa"))
