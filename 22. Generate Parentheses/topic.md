## 22. Gernerate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

>Link：https://leetcode-cn.com/problems/generate-parentheses

## Train of Thought
方法一
穷举法，使用堆栈判断每个穷举的结果是否满足要求
方法二
回溯法，拼完的字符串长度小于n则+"("，"("的长度少于")"的长度，则+")"
方法三
动态规划
