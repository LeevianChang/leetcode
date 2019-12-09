## 5. Longest Palindromic Substring

> Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

>Example 1:
>Input: "babad"
>Output: "bab"
>Note: "aba" is also a valid answer.

>Example 2:
>Input: "cbbd"
>Output: "bb"

>Link：https://leetcode-cn.com/problems/longest-palindromic-substring

## Train of Thought

首先，暴力法可能是第一个会想到的方法，这里不做思考。

题目中，需要在两个字符串中找到最长回文，找到回文的方法是把字符串倒过来看，和原始字符串相同的部分，比如
字符串 `babad` ，倒过来是`dabab` 其中发现 `aba` 相同，所以最长回文是 `aba`
如果只是这么判断，可以发现反例 `abcdfcba` ，倒过来看是 `abcfdcba`，可以看到`abc`和`cba`，均是相同的
问题出在哪里呢？
翻转过来的字符串与原来字符串相同的部分，不是原来位置上的部分，所以在做判断的时候，需要处理这种可能性，并且排除

