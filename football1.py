N = int(input())
goals = 20
fouls = 10
temp = 0
players=[]
fouls = []

for k in range(0,N):
    n = int(input())
    for i in range(0,n):
        ele = int(input())
        players.append(ele)
    for j in range(0,n):
        ele2 = int(input())
        fouls.append(ele2)

my_new_players = [a * 20 for a in players]
my_new_fouls = [b * 10 for b in fouls]

zip_lists = zip(my_new_players, my_new_fouls)

diff = []
for list1, list2 in zip_lists:
    diff.append(list1 - list2)
    
if(max(diff)>=0):
    print(max(diff))
else:
    print(0)