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
|52|[queue-reconstruction-by-height](https://leetcode.com/problems/queue-reconstruction-by-height/)|Medium|June 22|【注意】这道题思路没想到，是先对身高从高到低排序，再在组内按照index从小到大排序，然后依次插入|
|53|[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|Medium|June 22|【注意】用哈希表。即要确定一个subarray和是否为k，转为看[0:n]和为B的话，看是否有[0:m]和为B-k，这样[m:n]就是要求的子串|
|54|[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)|Easy|June 22|找s子串的字符（不考虑顺序）等于给定字符p的index位置|
|55|[jump-game](https://leetcode.com/problems/jump-game/)|Medium|June 23|【自己想到的思路是类似于solution中方法一，不过写得更耗时；参考了一个答案是类似于solution方法四贪心法，遍历数组，剩余步数step不为零的前提下，每次向前移动一步，将当前的num[i]和step相比较取较大者，作为剩余步数step|
|56|[find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)|Medium|June 23|遍历查找|
|57|[longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence)|Medium|June 23|动态规划：包括位置i在内的最长递增子序列长度|
|58|[longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence/)|Hard|June 24|自己想到的思路是先排序，再看是否连续；另一个O(N)思路就是把这个nums处理为集合，然后挨着往上界、下界找|
|59|[merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/)|Easy|June 24|【linked list】(思路：递归）把二叉树加起来|
|60|[invert-binary-tree](https://leetcode.com/problems/invert-binary-tree/)|Easy|June 24|【linked list】（思路：递归）把二叉树左右对称翻转|
|61|[course-schedule](https://leetcode.com/problems/course-schedule/)|Medium|June 26|【注意】判断有向图是否有环（拓扑排序）|
|62|[binary-tree-inorder-traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|Medium|June 26|【linked list】二叉树的中序遍历（先左，再root，再右），自己想的思路是递归，还可以用stack来存所有左节点|
|63|[binary-tree-level-order-traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|Medium|July 1| 把二叉树的值每一层每一层输出（从左往右）|
|64|[burst-balloons](https://leetcode.com/problems/burst-balloons/)|Hard|July 1|【注意】用动态规划，需要想清楚dp定义，而且递推式也要注意|
|65|[symmetric-tree](https://leetcode.com/problems/symmetric-tree)|Easy|July 1|检查是否为对称树|
|66|[minimum-path-sum](https://leetcode.com/problems/minimum-path-sum/)|Medium|July 1|矩阵里可往右、往下移动，找最小路径和（动态规划），注意初始条件|
|67|[min-stack](https://leetcode.com/problems/min-stack/)|Easy|July 1|最小栈|
|68|[palindrome-linked-list](https://leetcode.com/problems/palindrome-linked-list/)|Easy|July 1|判断链表是否是回文|
|69|[convert-bst-to-greater-tree](https://leetcode.com/problems/convert-bst-to-greater-tree)|Easy|July 3|【注意】BST是右侧>中间>左侧|
|70|[unique-binary-search-trees](https://leetcode.com/problems/unique-binary-search-trees/)|Medium|July 3|给定1-n个数有多少独特的BST。把题看懂后，基于BST特点，想到了合适的递推式|
|71|[maximal-square](https://leetcode.com/problems/maximal-square/)|Medium|July 3|【注意】最大正方形面积 以当前点(x,y) = '1' 为右下角的最大正方形的边长，递推式f(x,y) = min( f(x-1,y), f(x,y-1), f(x-1,y-1)) + 1.|
|72|[partition-equal-subset-sum](https://leetcode.com/problems/partition-equal-subset-sum/)|Medium|July 3|判断能否把包含正整数的lst分为和相等的2部分|
|73|[search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|Medium|July 3|二分法，不过主要是判断target到底属于左/右区间会稍微注意下哪侧区间是有序的|
|74|[best-time-to-buy-and-sell-stock-with-cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)|Medium|July 7|【注意】递推公式没想到，[参考](https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html)令sell[i] 表示第i天未持股时，获得的最大利润，buy[i]表示第i天持有股票时，获得的最大利润。|
|75|[linked-list-cycle](https://leetcode.com/problems/linked-list-cycle/)|Easy|July 7|判断链表是否有环，其中memory O(1)的方法是使用【快慢指针】|
|76|[path-sum-iii](https://leetcode.com/problems/path-sum-iii/)|Easy|July 7|二叉树从上到下共有多少条路的和等于指定数值|
|77|[intersection-of-two-linked-lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)|Easy|July 7|两个链表是否有交叉点。memory O(1)思路是分别遍历两个链表，得到分别对应的长度。然后求长度的差值，把较长的那个链表向后移动这个差值的个数，然后一一比较|
|78|[add-two-numbers](https://leetcode.com/problems/add-two-numbers/)|Medium|July 8|两个链表代表数字，求和|
|79|[diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/)|Easy|July 8|二叉树中最长路径，可不过root|
|80|[longest-palindromic-substring](https://leetcode.com/problems/longest-palindromic-substring/)|Medium|July 8|【注意】中心扩散法，还有[马拉车算法](https://segmentfault.com/a/1190000002991199)|
|81|[lru-cache](https://leetcode.com/problems/lru-cache/)|Medium|July 9|双向链表+dict来实现可以把least recently used对应node删去|
|82|[flatten-binary-tree-to-linked-list](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|Medium|July 22|把节点都移到右侧（思路是先直接得到右侧节点顺序list，再挨着赋值）|

