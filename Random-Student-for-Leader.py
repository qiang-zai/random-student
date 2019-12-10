__author__ = 'LQ'

import time
import threading
import tkinter as tk
import random


class RandomNameGame(object):
	'''随机小组内学生姓名'''

	def __init__(self):
		'''初始化信息'''
		self.window = tk.Tk()  # 初始化Tk() 建立二个窗口
		self.window.title('小组点名小程序')  # 设置标题
		self.window.minsize(1000, 700)
		self.student_info_list = [["郭飘", "李行", "柯康", "赵骏然", "严瑞哲", "方小静", "华豪", "彭文杰"],
		                          ["万华", "魏垚", "张一波", "刘洋华", "马勋", "吴文涛", "杨义龙", "范丽文"],
		                          ["林欢", "杨尚儒", "邓彭川", "周志勇", "柯鸿成", "吕浩亮", "张晶晶", "叶冲"],
		                          ["汪梦龙", "李论", "徐佳伟", '程明', '黄辉', "方小静", "华豪", "彭文杰"],
		                          ["1", "2", "3", '4', '5', "6", "7", "8"]]
		self.label_list = []  # label列表
		self.start = 0  # 随机起始数字
		self.status = True  # 随机状态控制

	def round(self):
		t = threading.Thread(target=self.startup)  # 启动start
		t.setDaemon(True)
		t.start()

	def startup(self):
		'''开始按钮事件'''
		while True:
			# 检测停止按钮是否被按下
			if self.status == False:
				self.status = True
				break
			# 遍历所有的label修改label背景色为天蓝色
			for i in self.label_list:
				i['bg'] = 'lightSkyBlue'
			self.label_list[self.start]['bg'] = 'red'  # 修改起始数字对应的滚动框背景色为 红色
			# 程序延时(跳动时间间隔)
			time.sleep(0.05)
			self.start += 1
			# 如果start数字大于所有的leael数,就将start重置为0
			if self.start > (len(self.label_list) - 1):
				self.start = 0

	def stops(self):
		'''停止按钮事件'''
		self.status = False  # 停止标志位

	def change_name_by_leader_num(self, leader_num):
		'''根据小组button按钮,生成对应小组的学员姓名'''
		name_list = self.student_info_list[leader_num]
		random.shuffle(name_list)
		for i, thing in enumerate(self.label_list):
			thing.config(text=name_list[i])

	def generate_button(self, text, command, x=750, y=640, width=100, height=100, font=('Arial', 25)):
		'''生成button工具函数'''
		return tk.Button(self.window, text=text, font=font, command=command).place(x=x, y=y, width=width,
		                                                                           height=height)

	def generate_label(self, text, x, y, bg='yellow', font=('Arial', 40), width=200, height=200):
		'''生成label工具函数'''
		label = tk.Label(self.window, text=text, bg=bg, font=font)
		label.place(x=x, y=y, width=width, height=height)
		return label

	def init_label(self):
		label_background = self.generate_label('', 0, 0, bg='black', width=620, height=620)
		label1 = self.generate_label('张三', 5, 5)
		label2 = self.generate_label('李四', 210, 5)
		label3 = self.generate_label('王五', 415, 5)
		label4 = self.generate_label('周六', 415, 210)
		label5 = self.generate_label('周润发', 415, 415)
		label6 = self.generate_label('Python', 210, 415)
		label7 = self.generate_label('强仔', 5, 415)
		label8 = self.generate_label('Java', 5, 210)
		self.label_list.extend([label1, label2, label3, label4, label5, label6, label7, label8])

	def init_button(self):
		leader_1_button = self.generate_button('第一组', lambda: self.change_name_by_leader_num(0), y=50)
		leader_2_button = self.generate_button('第二组', lambda: self.change_name_by_leader_num(1), y=150)
		leader_3_button = self.generate_button('第三组', lambda: self.change_name_by_leader_num(2), y=250)
		leader_4_button = self.generate_button('第四组', lambda: self.change_name_by_leader_num(3), y=350)
		leader_5_button = self.generate_button('第五组', lambda: self.change_name_by_leader_num(4), y=450)
		start_button = self.generate_button('开始', self.round, x=130, width=180, height=60, font=('Arial', 50))
		stop_button = self.generate_button('结束', self.stops, x=330, width=180, height=60, font=('Arial', 50))

	def run(self):
		'''运行Game'''
		self.init_label()
		self.init_button()
		self.window.mainloop()


def main():
	'''入口函数'''
	random_name_game = RandomNameGame()
	random_name_game.run()


if __name__ == '__main__':
	main()
