# Sliding window

class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        start_index = 0
        max_length = 0
        for index in range(len(s)):
            right_index = s[:index].rfind(s[index]) + 1
            if right_index > start_index:
                start_index = right_index

            max_length = max(max_length, index - start_index + 1)

        return max_length


if __name__ == "__main__":
    s = Solution()
    print(s.length_of_longest_substring("jbpnbwwd"))
    print(s.length_of_longest_substring("abcabcbb"))
    print(s.length_of_longest_substring("bbbbb"))
    print(s.length_of_longest_substring("pwwkew"))
    print(s.length_of_longest_substring("aab"))
    print(s.length_of_longest_substring("dvdf"))
