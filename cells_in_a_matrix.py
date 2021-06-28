tot=0
def cells_sol (N, K, task):
    rows = set([i+1 for i in range(N)])
    columns = set([i+1 for i in range(N)])
    result = []
 
    for t in task:
        rows.discard(t[0])
        columns.discard(t[1])
        result.append(len(rows)*len(columns))
 
    return result
    

N, K = map(int, input().split())
task = []
for _ in range(K):
    i, j = map(int, input().split())
    X = i, j
    task.append(X)


out_ = cells_sol(N, K, task)
for elements in out_:
    print(elements, end=' ')
print()
