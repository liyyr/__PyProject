#!coding = utf-8

import random


def CheckNum():
	listA = [1,2,3,4,5,6,7,8,9]
	listB = random.sample(listA,6)
	startNum = ''
	cycleNum = 1

	#从列表中获取随机数，并进行字符串衔接合并
	for x in listB:
		tempNum = x
		startNum = startNum + str(tempNum)

	#进行数值的验证，如验证通过，则执行指定操作
	while cycleNum:
		print("您本次操作的验证码为 %s" % startNum)
		inputNum = input("请输入对应的验证码：")

		if inputNum == startNum:
			print("您的输入正确")
		else:
			print("您的输入有误")

		cycleNum = int(input("按任意键再次操作，如需退出请按“0”"))

if __name__ == "__main__":
	CheckNum()

