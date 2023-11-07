    

def isPalindrome(grid1,grid2):
    rows, cols = len(grid1), len(grid1[0])
    visited = set()
    def dfs(i,j):
        if i not in range(rows) or j not in range(cols) or grid2[i][j] == 0 or (i,j) in visited:
            return True
        if grid2[i][j] != grid1[i][j]:
            return False
        visited.add((i,j))
        return dfs(i+1, j) and dfs(i-1,j) and dfs(i,j+1) and dfs(i,j-1)
    num = 0
    for i in range(rows):
        for j in range(cols):
            if (i,j) in visited or grid2[i][j] == 0:
                continue
            if dfs(i,j):
                num += 1
    return num
# print(isPalindrome([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],[[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]))
connections = [[1,0],[1,2],[3,2],[3,4]]
for i, j in connections:
    print(i, j)

