import pymysql

ServerList = []
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
except:
	print("serverlist is error")

try:
	n = 0
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
			print('Id= %d, OrderDate= %s, OrderPrice= %d, Customer= %s' % (Id, OrderDate, OrderPrice, Customer))
		n += 1
except:
	print("DBSelect is error")

db.close()
