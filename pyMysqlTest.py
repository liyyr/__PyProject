import pymysql

ServerList = []
with open('D:\\account.txt','w') as f:
		f.write('Id\tOrderDate\tOrderPrice\tCustomer\n')

#连接到本地数据库，获取所有网络mysql服务器信息，并将对应信息写入列表ServerList[]，供后续使用
try:
	db = pymysql.connect('localhost','root','root','serverlist')
	cursor = db.cursor()
	cursor.execute('select * from server')
	results = cursor.fetchall()
	for row in results:
		host = row[1]
		username = row[2]
		pwd = row[3]
		prefixed = row[4]
		#print('host= %s, username= %s, pwd= %s' % (host, username, pwd))
		ServerList.append([host, username, pwd, prefixed])
	db.close()
except:
	print("serverlist is error")

#获取mysql参数，并逐个连接查询
try:
	n = 0

	#通过获取最大队列，做循环查询
	while n < len(ServerList):
		host, username, pwd, prefixed = ServerList[n]
		db2 = pymysql.connect(host, username, pwd, prefixed+'_ww_account')
		cursor2 = db2.cursor()
		cursor2.execute('select * from orders')
		results2 = cursor2.fetchall()
		for row2 in results2:
			Id = row2[0]
			OrderDate = row2[1]
			OrderPrice = row2[2]
			Customer = row2[3]
			#print('Id= %d, OrderDate= %s, OrderPrice= %d, Customer= %s' % (Id, OrderDate, OrderPrice, Customer))
			
			#将查询得到结果，写入文本记录
			with open('D:\\account.txt','a') as f:

				#写入文本必须str格式，如存在int类型，请强制转换类型
				f.write('\n'+str(Id)+'\t'+OrderDate+'\t'+str(OrderPrice)+'\t'+Customer)
		n += 1
	db2.close
except:
	print("DBSelect is error")


