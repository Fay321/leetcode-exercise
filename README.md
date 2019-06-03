# leetcode-exercise
leetcode exercises with python

| 序号 | 题目名 | 难度 | 日期 | 备注 |
| ------| ------ | ------ | ------ | ------ |
| 1|[two sum](https://leetcode.com/problems/two-sum/)| Easy | March 15| 无|
|2| [longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)| Medium| March 15|用动态规划做的，但想的是从右往左做的，而且写复杂了|
|3| [longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring/)|Medium|March 17|最长回文子序列，尝试的动态规划也超时了，需要再检查|
|4|[palindrome-number](https://leetcode.com/problems/palindrome-number/submissions/)|Easy|April 8| 数字回文|
|5|[single number](https://leetcode.com/problems/single-number/solution/)|Easy|April 9|找唯一出现一次的数字|
|6|[Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)|Easy|April 10| 找s中出现在J中字符的个数|
|7|[Majority Element](https://leetcode.com/problems/majority-element/)|Easy|April 11|找数组中出现次数大于数组长度一半的一个数|
|8|[reverse linked list](https://leetcode.com/problems/reverse-linked-list)|Easy|April 14|逆转链表，对链表这个结构不熟，这道easy题还做了一阵子|
|9|[find-all-numbers-disappeared-in-an-array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array)|Easy|April 15|直接用了两个集合做差集|
|10|[kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/)|Medium|April 15|找数组中第k大的数|
|11|[house-robber](https://leetcode.com/problems/house-robber/submissions/)|Easy|April 20|找数组中不相邻元素最大和（动态规划）|
|12|[integer-to-roman](https://leetcode.com/problems/integer-to-roman/submissions/)|Medium（Easy)|May 28| 整数转为罗马数字|
|13|[string-to-integer](https://leetcode.com/problems/string-to-integer-atoi/)|Medium(Hard)|May 29|字符串中把前面的数字找出来并转为为int（难度在于未想到一些case）|
|14|[max-increase-to-keep-city-skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)| Easy|May 29|从上方、右侧看楼高保持一致的情况下，增加楼层高度|
|15|[hamming-distance](https://leetcode.com/problems/hamming-distance/submissions/)|Easy|May 29|把数字转为二进制，看哪些位置不同|
|16|[3sum](https://leetcode.com/problems/3sum/submissions/)|Medium|May 29|【注意】之前自己想到的是n^3的复杂度遍历，参考[思路](https://blog.csdn.net/haolexiao/article/details/70768526)知道先排序，再对每个数，求剩下的数字之后为target的list|
|17|[maximum-product-subarray](https://leetcode.com/problems/maximum-product-subarray/submissions/)|Medium|May 30|思路：维护两个数组，到这个数为止的最大值、最小值|
|18|[shortest-unsorted-continuous-subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)|Easy|June 1|一开始想到个O(NlogN)复杂度的，觉得可能过不了，就尝试想了O(N)的，但是反而边界条件很难想，最后用一开始想到的简单解法过了|
|19|[merge-intervals](https://leetcode.com/problems/merge-intervals/)|Medium|June 1|用了类似于暴力搜索的思路解决（时间复杂度高）如果先按照interval的start排序，这样复杂度低些|
|20|[maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|Easy|June 1|【注意】用递归求二叉树的深度|
|21|[move-zeroes](https://leetcode.com/problems/move-zeroes/)|Easy|June 2|把0都移到数组右侧（想的时候想绕了，想的是非零元从右边往左移动，其实应该是把零往右侧非零处交换|
|22|[daily-temperatures](https://leetcode.com/problems/daily-temperatures)|Medium|June 2|【注意】自己的思路是从右边往左记录比这个位置大的数，这样如果b比a小的话，只需要查看比b更大的数和a比较即可。看了效率更高的思路是从左往右，大的数值可以消掉栈中的元素|
|23|[counting-bits](https://leetcode.com/problems/counting-bits/)|Medium|June 3|自己思路复杂度是O(N\*size)，然后找到一个找到规律后的O(N)解答|
