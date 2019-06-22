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
|24|[palindromic-substrings](https://leetcode.com/problems/palindromic-substrings/submissions/)|Medium|June 3|【思路】回文子串（核心思路：就是回文往左右扩一个位置看是否还是回文)|
|25|[merge-two-sorted-lists](https://leetcode.com/problems/merge-two-sorted-lists/)|Easy|June 3|合并排序的链表。主要是注意怎么生成链表head,prev,next|
|26|[climbing-stairs](https://leetcode.com/problems/climbing-stairs/)|Easy|June 5|【思路】自己是用组合数(scipy.special.comb)来挨着计算，更好的思路是用动态规划|
|27|[best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|Easy|June 5|找最大子序列和|
|28|[subsets](https://leetcode.com/problems/subsets/)|Medium|June 5|用了itertools.product笛卡儿积|
|29|[top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements/)|Medium(Easy)|June 5|出现次数top K的数字|
|30|[unique-paths](https://leetcode.com/problems/unique-paths/)|Medium|June 5|从左上角到右下角的不同路径（本质上就是计算组合数）|
|31|[find-the-duplicate-number](https://leetcode.com/problems/find-the-duplicate-number)|Medium(Easy)|June 5|找重复数字|
|32|[trapping-rain-water](https://leetcode.com/problems/trapping-rain-water/)|Medium|June 5|蓄水问题，在于观察到这个格子蓄水量为 max(min(左侧最大值，右侧最大值)-高度,0)|
|33|[sort-colors](https://leetcode.com/problems/sort-colors/)|Medium|June 7|只包含0，1，2的数字排序，直接计算各个数字出现的次数，挨着修改|
|34|[permutations](https://leetcode.com/problems/permutations/)|Medium|June 7|递归来求permutation|
|35|[product-of-array-except-self](https://leetcode.com/problems/product-of-array-except-self/)|Medium|June 7|用了两个字典分别存除了i左侧的积、右侧的积，然后再分别乘起来。这思路空间开销大|
|36|[rotate-image](https://leetcode.com/problems/rotate-image/)|Medium|June 8|【注意】图像旋转90度，就是先上下翻转，再沿对角线翻转|
|37|[maximum-subarray](https://leetcode.com/problems/maximum-subarray)|Easy|June 8|记录包括第i个位置的最大值|
|38|[group-anagrams](https://leetcode.com/problems/group-anagrams/)|Medium|June 8|判断两个词语字符组成完全相同|
|39|[combination-sum](https://leetcode.com/problems/combination-sum/)|Medium|June 10|自己的递归思路+去重运行慢，看了一个解答后，先对candidates排序后，就不必再考虑去重，速度快很多|
|40|[container-with-most-water](https://leetcode.com/problems/container-with-most-water/)|Medium|June 10|最开始想的是挨着算两两柱子形成的容器容量。但这个会超时。用最左、最右两个柱子作为开端；而两个柱子中最低的那个限制了容量，所以要想宽度减少而容量增加只可能是高度变高，所以把两个柱子中较低的那个指针往中间移动|
|41|[word-break](https://leetcode.com/problems/word-break/)|Medium|June 10|【注意】自己想的递归暴力搜索超时，后面改用动态规划|
|42|[letter-combinations-of-a-phone-number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|Medium|June 10|就是用递归得到permutation|
|43|[search-a-2d-matrix-ii](https://leetcode.com/problems/search-a-2d-matrix-ii/)|Medium|June 10|自己想的从左上角查找，观察题目得到规律应该从右上角查更快些|
|44|[valid-parentheses](https://leetcode.com/problems/valid-parentheses/)|Medium|June 10|括号匹配（注意栈为空了，才说明都匹配完了）|
|45|[decode-string](https://leetcode.com/problems/decode-string/)|Medium|June 12|类似于括号匹配，用栈|
|46|[coin-change](https://leetcode.com/problems/coin-change/)|Medium|June 12|【注意】用动态规划来解决换零钱问题|
|47|[sliding-window-maximum](https://leetcode.com/problems/sliding-window-maximum/)|Hard|June 12|如果用最简单的kN复杂度的思路也可以直接解决|
|48|[number-of-islands](https://leetcode.com/problems/number-of-islands/)|Medium|June 12|【注意】用了DFS，找到所有相邻岛屿|
|49|[perfect-squares](https://leetcode.com/problems/perfect-squares/)|Medium|June 12|【注意】一个数可以拆成的最小平方和数目，想到了用类似于change coin动态规划。还有一个求解方法是用DFS|
|50|[generate-parentheses](https://leetcode.com/problems/generate-parentheses/)|Medium|June 12|【注意】想的递归思路超时，看了solution后是用DFS思路|
|51|[target-sum](https://leetcode.com/problems/target-sum/)|Medium|June 20|给不同符号，求和等于给定值（用一个字典记录到nums第i个位置为止，等于j的不同搭配数有多少，有点像之前做遍历搜索|
|52|[]()|Medium|June 22|【待定】这道题有bug|
|53|[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|Medium|June 22|【注意】用哈希表。即要确定一个subarray和是否为k，转为看[0:n]和为B的话，看是否有[0:m]和为B-k，这样[m:n]就是要求的子串|
