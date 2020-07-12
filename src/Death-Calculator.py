#!/bin/env python3

import datetime
import tkinter as tk

def error1():
	popup1 = tk.Tk()
	popup1.title("Error")
	popup1.iconbitmap("lib/icon.ico")
	error_msg = tk.Label(popup1, text="Error: Invalid Input", font=("Courier, 12"))
	error_msg.pack(padx=35, pady=10)
	exit_button = tk.Button(popup1, text="Ok", padx=20, pady=1, font=("Courier 12 bold"), command=lambda: popup1.withdraw())
	exit_button.pack(pady=15)
	popup1.mainloop()

def inputPopup():
	inputWindow = tk.Tk()
	inputWindow.title("Date of Birth")
	inputWindow.geometry("260x150")
	inputWindow.iconbitmap("lib/icon.ico")

	def enterButton():
		global birthDate_raw
		birthDate_raw = entryBox.get()
		check = birthDate_raw.split("-")
		try:
			int(check[0])
			int(check[1])
			int(check[2])
		except:
			error1()
		try:
			int(check[3])
			error1()
		except IndexError:
			pass
		inputWindow.withdraw()
		visualizer()

	title = tk.Label(inputWindow, text="Enter your date of birth:", font='Helvetica 12', borderwidth=1)
	title.pack(padx=10, pady=10)

	entryBox = tk.Entry(inputWindow)
	entryBox.pack(pady=10)
	entryBox.insert(0, "YYYY-MM-DD")

	enterButton = tk.Button(inputWindow, text="Enter", font='Helvetica 12 bold', command=enterButton)
	enterButton.pack(pady=10)

	inputWindow.mainloop()


def visualizer():
	root = tk.Tk()
	root.title("Time left to live (Visualized)")
	root.iconbitmap("lib/icon.ico")

	global birthDay, birthMonth, birthYear
	birthYear, birthMonth, birthDay = birthDate_raw.split("-")

	date_raw = str(datetime.datetime.now()).split(" ")
	global currentDay, currentMonth, currentYear
	currentYear, currentMonth, currentDay = date_raw[0].split("-")
	threashhold = ((int(currentYear) - int(birthYear)) * 12) + (int(currentMonth) - int(birthMonth))

	if (int(currentDay) + int(birthDay)) > 30:
		threashhold += 1

	for i in range(1, 961):
		if i <= threashhold:
			command = "tile{} = tk.Label(root, borderwidth=1, relief='groove', padx=5, bg='firebrick1')".format(i)
		else:
			command = "tile{} = tk.Label(root, borderwidth=1, relief='groove', padx=5, bg='azure2')".format(i)
		exec(command)

	count = 1
	for x in range(1, 31):
		for y in range(1, 33):
			command = "tile{}.grid(row={}, column={})".format(count, x, y)
			exec(command)
			count += 1

	bottomText = tk.Label(root, text="Lifespan visualized (assuming you die at 80) - Created by Treebug842")
	bottomText.grid(row=31, column=1, columnspan=32, sticky=tk.W)

	root.mainloop()

inputPopup()

