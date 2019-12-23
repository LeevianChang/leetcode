## 30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

>Link：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words

### Train of Thought

方法1：
暴力法，容易超时
方法2：
使用滑动窗口解法，由一个变量记录一次循环各个单词出现的个数，如果比入参中的words多，则表明单词有误，需调整窗口的开始索引，移动，直到当前的单词数与入参中的words相符