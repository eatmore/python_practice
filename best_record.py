f = open('game_one_user.txt')
data = f.read()
record = data.split()

record_dic = {'user_name': record[0],'times': record[1],'ave_times': record[2], 'min_time': record[3]}
print(record_dic)