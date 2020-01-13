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
		r1 = range(1000000, 10000000)
		r2 = range(5000000, 10000000)
		if fname == '':
			reset()

		else:
			while selection == "1":
				while 1:
					prefix = input("\n\t\t\033[1;32mEnter a prefix number:  \033[1;m")
					if (prefix.isdigit()): break

					else: Msg.msg5()

				while 1:
					try:
						rmin = int(input("\n\t\t\033[1;32mEnter range minimum (exclude prefix):  \033[1;m"))
						break

					except ValueError:
						Msg.msg5()

				while 1:
					try:
						rmax = int(input("\n\t\t\033[1;32mEnter range maximum:  \033[1;m"))
						if rmin >= rmax:
							Msg.msg3()

						else:
							Msg.msg1() if int(rmax) >= 1000000 else Msg.msg2()
							r = range(rmin, rmax)
							generator.generate(fname, prefix,r)
							break

					except ValueError:
						Msg.msg5()

			while selection != "1":
				prefix = input("\n\t\t\033[1;32mEnter a prefix number ('all' for all possible combinations):  \033[1;m")
				if (prefix.isdigit()):
					if selection == "2":
						Msg.msg4()
						generate(fname, prefix, r1)
						break

					else:
						Msg.msg4()
						generate(fname, prefix, r2)
						break

				elif prefix == "all":
					if selection == "2":
						Msg.msg4()
						enerate(fname, "mpfx", r1)
						break

					else:
						Msg.msg4()
						generate(fname, "lpfx", r2)
						break

				else:
					Msg.msg6()

	def generate(fname, prefix, r):
		if (prefix.isdigit()):
			with open(fname, 'w') as f:
				for i in r:
					f.write(str(prefix)+str(i)+'\n')
					i += 1

		else:
			mpfx = ['050','052','053','054','055','057','058']
			lpfx = ['02','03','04','08','09','071','072','073','074','075','076','077','078']
			if prefix == "mpfx":
				with open(fname, 'w') as f:
					for i in mpfx:
						for j in r:
							f.write(str(i)+str(j)+'\n')
							j += 1

			else:
				with open(fname, 'w') as f:
					for i in lpfx:
						for j in r:
							f.write(str(i)+str(j)+'\n')
							j += 1

		# COUNTER
		with open(fname, "r+") as f:
			buffer = mmap.mmap(f.fileno(), 0)
			line = 0
			read = buffer.readline
			while read():
				line += 1

		if prefix == "mpfx": prefix = "all mobile prefixes"
		elif prefix == "lpfx": prefix = "all landline prefixes"
		banner()
		print("\n\n\t\t\033[1;38mSuccessfully generated a list of numbers prefixed with {}.\033[1;m".format(prefix))
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
		print("\n\n\t\t\033[1;32mGenerating. this might take a while..\033[1;m\n")

	def msg5():
		banner()
		print ("\n\n\t\t\033[1;31mUse only numbers\033[1;m\n")

	def msg6():
		banner()
		print ("\n\n\t\t\033[1;31mUse only numbers or 'all'\033[1;m\n")

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
	if sys.version[0] is not "3":
		print("\n\t\tThis program runs in Python3 only.\n")
		sys.exit()

	else:
		user_input = input('''\


		\033[1;38mSelect an option:\033[1;m

		\033[1;31m[>]\033[1;m  \033[1;37m1)\033[1;m \033[1;32mGenerate a custom range of numbers\033[1;m
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
