# give a list of integer, no dup
# return all possible subsets of it

# dfs solution
def subset_dfs(lst):
    res, wip = [], []
    def dfs(idx):
        res.append(list(wip))
        for i in range(idx, len(lst)):
            wip.append(lst[i])
            dfs(i+1)
            wip.pop()
        return res
    return dfs(0)

def subset_iter(lst):
    res = [[]]
    for i in lst:
        sz = len(res)
        for j in range(sz):
            l = list(res[j])
            l.append(i)
            res.append(l)
    return res

# the main idea is from the combination iterative 2
def subset_iter2(lst):
    res = [[]]
    for l in range(1, len(lst) + 1):
        wip = [0] * l
        i = 0
        while i >= 0:
            wip[i] += 1
            if wip[i] > len(lst):
                i -= 1
            elif i == l - 1:
                res.append([lst[ii-1] for ii in wip])
            else:
                i += 1
                wip[i] = wip[i-1]
    return res


# give a list of integer, return all possible subsets of it.
# need to exclude duplicates
def subset_dfs_dedup(lst):
    lst.sort()
    res, wip = [], []
    def dfs(idx):
        res.append(list(wip))
        prev = None
        for i in range(idx, len(lst)):
            if prev == lst[i]: continue
            wip.append(lst[i])
            dfs(i+1)
            wip.pop()
            prev = lst[i]
        return res
    return dfs(0)


def subset_iter_dedup(lst):
    lst.sort()
    res, wip, cnt = [[]], [[]], 1
    for i in range(len(lst)):
        if i + 1 < len(lst) and lst[i] == lst[i+1]:
            cnt += 1
            continue
        sz = len(res)
        for j in range(sz):
            l = list(res[j])
            for k in range(cnt):
                l.append(lst[i])
                res.append(list(l))
        cnt = 1
    return res

def test_subsets():
    lst0 = [1,2,3,4]
    lst1 = [1,2,3]
    lst2 = []
    assert sorted(subset_dfs(lst0)) == sorted(subset_iter(lst0))
    assert sorted(subset_dfs(lst1)) == sorted(subset_iter(lst1))
    assert sorted(subset_dfs(lst2)) == sorted(subset_iter(lst2))

    assert sorted(subset_dfs(lst0)) == sorted(subset_iter2(lst0))
    assert sorted(subset_dfs(lst1)) == sorted(subset_iter2(lst1))
    assert sorted(subset_dfs(lst2)) == sorted(subset_iter2(lst2))
    lst0 = [1,2,2,3,3,3,4]
    lst1 = [1,2,2,3]
    lst2 = []
    assert sorted(subset_dfs_dedup(lst0)) == sorted(subset_iter_dedup(lst0))
    assert sorted(subset_dfs_dedup(lst1)) == sorted(subset_iter_dedup(lst1))
    assert sorted(subset_dfs_dedup(lst2)) == sorted(subset_iter_dedup(lst2))

    print('subsets pass')

#---------------------
# Given two integers n and k, return all possible combinations of k numbers out of a list of integers.
# there is no dup in the list
# recursive dfs
def combine_dfs(n, k):
    res, wip = [], []
    def dfs(idx, m):
        if m <= 0: return
        for i in range(idx, n+1):
            wip.append(i) 
            if m == 1:
                res.append(list(wip))
            else:
                dfs(i+1, m-1)
            wip.pop()
    dfs(1, k)
    return res

# this is a way, but there are many copies of list
# and memory usage is high
def combine_iter(n, k):
    res, wip = [], [[]]
    for i in range(1, n+1):
        sz = len(wip)
        for j in range(sz):
            o = wip.pop(0)
            wip.append(o)
            lst = list(o)
            lst.append(i)
            if len(lst) == k:
                res.append(lst)
            elif len(lst) < k:
                wip.append(lst)
    return res

# this one is very efficient
# main idea, manipulate the numbers in each position, increment them in a certain order
# thus we have less copies and lower memory usage
# it is also much faster

def combine_iter2(n, k):
    res, wip, i = [], [0] * k, 0
    while i >= 0:
        wip[i] += 1
        if wip[i] > n:
            i -= 1
        elif i == k - 1:
            res.append(list(wip))
        else:
            i += 1
            wip[i] = wip[i-1]
    return res


def test_comb():
    assert sorted(combine_dfs(4, 2)) == sorted(combine_iter(4, 2))
    assert sorted(combine_dfs(4, 2)) == sorted(combine_iter2(4, 2))
    assert sorted(combine_dfs(5, 1)) == sorted(combine_iter2(5, 1))
    print('combination pass')

# permutations with distinct numbers
# recursive dfs
def perm_dfs(lst):
    result = []
    def dfs(idx):
        if idx >= len(lst):
            result.append(list(lst))
        else:
            for i in range(idx, len(lst)):
                lst[idx], lst[i] = lst[i], lst[idx]
                dfs(idx+1)
                lst[idx], lst[i] = lst[i], lst[idx]
        return result
    return dfs(0)

# permutations with distinct objects
# iterative way
# the key is to figure out next permutation
# the provided list may contain objects not comparable
# then we can permute the index and thus permute the objects
def perm_iter(lst):
    result = []
    def next_perm(nums):
        i, j = -1, -1
        for x in range(len(nums)-2, -1, -1):
            if nums[x] < nums[x+1]:
                i = x
                break
        if i < 0:
            return None
        for x in range(len(nums)-1, -1, -1):
            if nums[x] > nums[i]:
                j = x
                break
        nums[i], nums[j] = nums[j], nums[i]
        return nums[:i+1] + sorted(nums[i+1:])

    idx = [i for i in range(0, len(lst))]
    while idx is not None:
        result.append([lst[i] for i in idx])
        idx = next_perm(idx)
    return result


# permutations with numbers with duplicates
# a set is used to track used numbers
def perm_dfs_dedup(lst):
    result = []
    lst.sort()
    def dfs(idx):
        if idx >= len(lst):
            result.append(list(lst))
        else:
            used = set()
            for i in range(idx, len(lst)):
                if lst[i] in used: continue
                used.add(lst[i])
                lst[idx], lst[i] = lst[i], lst[idx]
                dfs(idx+1)
                lst[idx], lst[i] = lst[i], lst[idx]
        return result
    return dfs(0)

def test_perm():
    assert sorted(perm_dfs([1,2,3,4])) == sorted(perm_iter([1,2,3,4]))
    print(sorted(perm_dfs_dedup([1,1,2,3,3])))
    print('permutation pass')

if __name__ == '__main__':
    test_subsets()
    test_comb()
    test_perm()
