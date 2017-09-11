import pymysql

db = pymysql.connect('localhost','root','root','serverlist')

cursor = db.cursor()

sql = 'select * from server'
ServerList = []
try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		host = row[1]
		username = row[2]
		pwd = row[3]
		#print('host= %s, username= %s, pwd= %s' % (host, username, pwd))
		ServerList.append([host, username, pwd])
except:
	print("serverlist is error")

try:
	n = 0
	while n < len(ServerList):
		host, username, pwd = ServerList[0]
		db2 = pymysql.connect(host, username, pwd,'serverlist')
		cursor2 = db2.cursor()
		cursor2.execute('select * from server')
		results2 = cursor2.fetchall()
		for row2 in results2:
			host2 = row2[1]
			username2 = row2[2]
			pwd2 = row2[3]
			print('host= %s, username= %s, pwd= %s' % (host2, username2, pwd2))
		n += 1
except Exception as e:
	raise e

db.close()
