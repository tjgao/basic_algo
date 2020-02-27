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

def test_comb():
    print(sorted(combine_dfs(4,2)))
    print(sorted(combine_iter(4,2)))

if __name__ == '__main__':
    test_subsets()
    test_comb()
