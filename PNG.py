#!/usr/bin/python3
# coding: utf-8


import sys, time, mmap, os, webbrowser

os.system('mode con: cols=45 lines=90' if os.name == 'nt' else 'printf "\e[8;35;110t"')

def banner():

	os.system('cls' if os.name == 'nt' else 'printf "\033c"')
	print ('''\


	\033[1;37m--------------------------------------------------------------------------------------------
	============================================================================================

				    PHONE NUMBERS GENERATOR v3 BY\033[1;m

	\033[1;31m				██╗  ██╗ ██████╗ ██╗  ██╗
					██║  ██║██╔═████╗██║  ██║
					███████║██║██╔██║███████║
					╚════██║████╔╝██║╚════██║
					     ██║╚██████╔╝     ██║
					     ╚═╝ ╚═════╝      ╚═╝\033[1;m

	\033[1;37m=============================================================================================
	---------------------------------------------------------------------------------------------
	\033[1;m''')

def reset():
	banner()
	main()

class generator():

	def process(selection):
		fname = input("\n\n\t\t\033[1;32mEnter output file name (ENTER to go back):  \033[1;m")
		if fname == '':
			reset()
		else:
			while 1:
				prefix = input("\n\t\t\033[1;32mEnter a prefix:  \033[1;m")
				if (prefix.isdigit()): break
				else: Msg.msg5()
			while selection == "1":
				try:
					rmin = int(input("\n\t\t\033[1;32mEnter range minimum (exclude prefix):  \033[1;m"))
					break
				except ValueError:
					Msg.msg5()
			while selection == "1":
				try:
					rmax = int(input("\n\t\t\033[1;32mEnter range maximum:  \033[1;m"))
					if rmin >= rmax:
						Msg.msg3()
					else:
						Msg.msg1() if int(rmax) >= 1000000 else Msg.msg2()
						r = range(rmin, rmax)
						generator.action_generate(fname, prefix, r)
						break
				except ValueError:
					Msg.msg5()
			if selection == "2":
				Msg.msg4()
				r = range(1000000, 9999999)
				generator.action_generate(fname, prefix, r)
			elif selection == "3":
				Msg.msg4()
				r = range(5000000, 9999999)
				generator.action_generate(fname, prefix, r)

	def action_generate(fname, prefix, r):

		# GENERATOR
		with open(fname, 'w') as f:
			for i in r:
				i += 1
				f.write(str(prefix)+str(i)+'\n')

		# COUNTER
		with open(fname, "r+") as f:
			buffer = mmap.mmap(f.fileno(), 0)
			line = 0
			read = buffer.readline
			while read():

				line += 1

		banner()
		print("\n\n\t\t\033[1;38mDone generating list of numbers prefixed with '{}'.\033[1;m".format(prefix))
		print("\n\n\t\t\033[1;32mCounted \033[1;34m{}\033[1;m \033[1;32mlines.\033[1;m".format(line))
		main()

class Msg():

	def msg1():

		banner()
		print("\n\n\t\t\033[1;32mGenerating. this might take a while for long numbers..\033[1;m\n")

	def msg2():

		banner()
		print("\n\n\t\t\033[1;32mGenerating...\033[1;m\n")

	def msg3():

		banner()
		print("\n\n\t\t\033[1;31mRange minimum must be smaller than range maximum.\033[1;m\n")

	def msg4():

		banner()
		print("\n\n\t\t\033[1;32mGenerating. this might take a few seconds..\033[1;m\n")

	def msg5():

		banner()
		print ("\n\n\t\t\033[1;31mUse only numbers\033[1;m\n")

	def quitProperly():

		banner()
		print("\n\n\t\t\033[1;31mQuitting.\033[1;m\n")
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'printf "\033c"')
		sys.exit()

	def NST():

		banner()
		print("\n\n\t\t\033[1;31mNo such thing.\033[1;m\n")

	def fzf():

		banner()
		webbrowser.open('https://www.youtube.com/watch?v=iRq7Muf6CKg')


def main():

	user_input = input('''\


	\033[1;38mSelect an option:\033[1;m

	\033[1;31m[>]\033[1;m  \033[1;37m1)\033[1;m \033[1;32mGenerate custom range numbers\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m2)\033[1;m \033[1;32mGenerate cellphone numbers (israel)\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m3)\033[1;m \033[1;32mGenerate landline numbers (israel)\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m4)\033[1;m \033[1;31mQuit properly\033[1;m

	''')

	if user_input == "1":

		banner()
		generator.process(user_input)

	elif user_input == "2":

		banner()
		generator.process(user_input)

	elif user_input == "3":

		banner()
		generator.process(user_input)

	elif user_input == "4":

		Msg.quitProperly()

	elif user_input == "404":

		Msg.fzf()
		reset()

	else:
		Msg.NST()
		time.sleep(2)
		reset()

if __name__ == "__main__":

	reset()
