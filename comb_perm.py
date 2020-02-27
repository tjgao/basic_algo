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
    res, wip = [[]], [[]]
    for i in range(0, len(lst)):
        tmp = []
        for s in wip:
            l = list(s)
            l.append(lst[i])
            tmp.append(l)
        res.extend(tmp)
        wip.extend(tmp)
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





if __name__ == '__main__':
    lst0 = [1,2,3,4]
    lst1 = [1,2,3]
    lst2 = []
    print(sorted(subset_dfs(lst0)))
    print(sorted(subset_dfs(lst1)))
    print(sorted(subset_dfs(lst2)))
#    print('--------------')
#    print(subset_iter(lst0))
#    print(subset_iter(lst1))
#    print(subset_iter(lst2))
    lst0 = [1,2,2,3,3,3,4]
    lst1 = [1,2,2,3]
    lst2 = []
    print(sorted(subset_dfs_dedup(lst0)))
    print(sorted(subset_dfs_dedup(lst1)))
    print(sorted(subset_dfs_dedup(lst2)))
    print('--------------')

