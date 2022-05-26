"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space."""

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        s = s.split()
        for i in range(len(s)):
            result += s[i][::-1]
            if i != len(s)-1:
                result += ' '
        return result

"""Runtime: 51 ms, faster than 61.70% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.6 MB, less than 84.06% of Python3 online submissions for Reverse Words in a String III."""