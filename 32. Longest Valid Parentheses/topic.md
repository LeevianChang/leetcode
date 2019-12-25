## 32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

> Link：https://leetcode-cn.com/problems/longest-valid-parentheses


### Train of Thought
方法1：
暴力法，循环检查字符串是否有效
方法2：
动态规划
考虑两种可能性，1：“)”前是“（”的情况，2：“）”前是“）”的情况
方法3：
