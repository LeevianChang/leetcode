## 10. Regular Expression Matching
>Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.'.' Matches any single character.'*' Matches zero or more of the preceding element.The matching should cover the entire input string (not partial).
Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

> Link：https://leetcode-cn.com/problems/regular-expression-matching


本题的关键在于，需要解决*的问题
*的匹配从大方向上看有两种情况,假设 patten的第二个是星号
1. string的首字符与patten的首字符相同，string是 `ab`，patten为`a*b` 
2. string的首字符与patten的首字符不同，有两种情况，
   2.1 string是`a`，patten为`b*a`，这种情况下由于*可以使前面的字符出现0次，所以也匹配
   2.2 string是`aa`,patten为`a*a`，这种情况下需要注意*只匹配了一次a，第二次出现的a是下一个字符匹配的，在代码中需要考虑到