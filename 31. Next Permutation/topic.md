## 31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

>Link：https://leetcode-cn.com/problems/next-permutation

### Train of Thought

本题考查字典序算法，给定其中一种排列，求基于字典序的下一种排列。要求下一种排列既要比原排列大，又不能有第三种排列位于他俩之间。即下一种排列为大于原排列的最小排列。

查了一下字典序排序的算法：
以输入为 358764 为例，字典序算法的步骤：
1、从原排列中，从右至左，找到第一个左邻小于右邻的字符，记左邻位置为 a。
示例中 a=1，list[a] = 5。
2、重新从右至左，找到第一个比 list[a] 大的字符，记为位置为 b。
示例中 b=4，list[b] = 6。
3、交换 a 和 b 两个位置的值。
示例变为了 368754。
4、将 a 后面的数，由小到大排列。
示例变为了 364578。

算法结束，输出 364578。
————————————————
版权声明：本文为CSDN博主「HappyRocking」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/happyrocking/article/details/83619392