n_number = int(input())
data = list(map(int, input().split()))
cal_data = list(map(int, input().split()))
cal_dic = {'+': cal_data[0], '-':cal_data[1], '*':cal_data[2], '//':cal_data[3] }
maxi = -1e9
mini = 1e9

nums = []

def dfs(depth, setting):
    global maxi, mini, n_number
    
    if depth == n_number:
        maxi = max(maxi, setting)
        mini = min(mini, setting)
    
    else:
        if cal_dic['+']>0:
            cal_dic['+'] -= 1
            dfs(depth+1, setting + data[depth])
            cal_dic['+'] += 1
            
        if cal_dic['-']>0:
            cal_dic['-'] -= 1
            dfs(depth+1, setting - data[depth])
            cal_dic['-'] += 1
        
        if cal_dic['*']>0:
            cal_dic['*'] -= 1
            dfs(depth+1, setting * data[depth])
            cal_dic['*'] += 1        
            
        if cal_dic['//']>0:
            cal_dic['//'] -= 1
            if setting >=0:
                dfs(depth+1, setting // data[depth])
                cal_dic['//'] += 1
            else:
                dfs(depth+1, -(-setting // data[depth]))
                cal_dic['//'] += 1
dfs(1, data[0])
print(maxi)
print(mini)