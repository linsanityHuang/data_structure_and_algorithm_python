'''
时间复杂度的全称是渐进时间复杂度，表示算法的执行时间与数据规模之间的增长关系。
类比一下，空间复杂度全称就是渐进空间复杂度，表示算法的存储空间与数据规模之间的增长关系。

我还是拿具体的例子来给你说明。（这段代码有点“傻”，一般没人会这么写，我这么写只是为了方便给你解释。）

1void print(int n) {
2  int i = 0;
3  int[] a = new int[n];
4  for (i; i <n; ++i) {
5    a[i] = i * i;
6  }

7  for (i = n-1; i >= 0; --i) {
8    print out a[i]
9  }
10}

跟时间复杂度分析一样，我们可以看到，第 2 行代码中，我们申请了一个空间存储变量 i，但是它是常量阶的，跟数据规模 n 没有关系，所以我们可以忽略。

第 3 行申请了一个大小为 n 的 int 类型数组，除此之外，剩下的代码都没有占用更多的空间，所以整段代码的空间复杂度就是 O(n)。

我们常见的空间复杂度就是 O(1)、O(n)、O(n^2)，像 O(logn)、O(nlogn) 这样的对数阶复杂度平时都用不到。

而且，空间复杂度分析比时间复杂度分析要简单很多。所以，对于空间复杂度，掌握刚我说的这些内容已经足够了。
'''

