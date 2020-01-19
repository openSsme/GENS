#!/usr/bin/python3
# coding: utf-8


import sys, time, mmap, os, webbrowser

os.system('mode con: cols=45 lines=90' if os.name == 'nt' else 'printf "\e[8;35;110t"')

def banner():

	os.system('cls' if os.name == 'nt' else 'printf "\033c"')
	print ('''\


	\033[1;37m--------------------------------------------------------------------------------------------
	░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

				      PHONE NUMBERS GENERATOR v3 BY\033[1;m

	\033[1;31m				██╗  ██╗ ██████╗ ██╗  ██╗
					██║  ██║██╔═████╗██║  ██║
					███████║██║██╔██║███████║
					╚════██║████╔╝██║╚════██║
					     ██║╚██████╔╝     ██║
					     ╚═╝ ╚═════╝      ╚═╝\033[1;m

	\033[1;37m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	--------------------------------------------------------------------------------------------
	\033[1;m''')

def reset():
	banner()
	main()

def process(selection):
	fname = input("\n\n\t\t\033[1;32mName the output file (default: go back):  \033[1;m")
	if fname == '':
		reset()

	else:
		while selection == "1":
			while 1:
				prefix = input("\n\t\t\033[1;32mEnter a prefix number:  \033[1;m")
				if (prefix.isdigit()): break

				else: display('5')

			while 1:
				try:
					rmin = int(input("\n\t\t\033[1;32mEnter range minimum (exclude prefix):  \033[1;m"))
					break

				except ValueError:
					display('5')

			while 1:
				try:
					rmax = int(input("\n\t\t\033[1;32mEnter range top:  \033[1;m"))
					if rmin >= rmax:
						display('3')

					else:
						display('1') if int(rmax) >= 1000000 else display('2')
						custome_range = range(rmin, rmax)
						generate(fname, prefix, custome_range)
						break

				except ValueError:
					display('5')

		while selection != "1":
			mobile_range = range(1000000, 10000000)
			landline_range = range(5000000, 10000000)
			prefix = input("\n\t\t\033[1;32mEnter a prefix number ('all' for all possible combinations):  \033[1;m")
			if (prefix.isdigit()):
				if selection == "2":
					display('4')
					generate(fname, prefix, mobile_range)
					break

				else:
					display('4')
					generate(fname, prefix, landline_range)
					break

			elif prefix == "all":
				if selection == "2":
					display('4')
					generate(fname, "mpfx", mobile_range)
					break

				else:
					display('4')
					generate(fname, "lpfx", landline_range)
					break

			else:
				display('6')

def generate(fname, prefix, range):
	if (prefix.isdigit()):
		with open(fname, 'w') as f:
			for i in range:
				f.write(str(prefix)+str(i)+'\n')
				i += 1

	else:
		if prefix == "mpfx":
			mpfx = ['050','052','053','054','055','057','058']
			with open(fname, 'w') as f:
				for i in mpfx:
					for j in range:
						f.write(str(i)+str(j)+'\n')
						j += 1

		else:
			lpfx = ['02','03','04','08','09','071','072','073','074','075','076','077','078']
			with open(fname, 'w') as f:
				for i in lpfx:
					for j in range:
						f.write(str(i)+str(j)+'\n')
						j += 1

	# COUNTER
	with open(fname, "r+") as f:
		buffer = mmap.mmap(f.fileno(), 0)
		lines = 0
		read = buffer.readline
		while read():
			lines += 1

	if prefix == "mpfx": prefix = "all mobile prefixes"
	elif prefix == "lpfx": prefix = "all landline prefixes"
	banner()
	display('9', prefix)
	display('10', lines)
	main()

def display(msg, *args):

	if msg == '1': banner(); print("\n\n\t\t\033[1;32mGenerating. this might take a while for long numbers..\033[1;m\n")
	if msg == '2': banner(); print("\n\n\t\t\033[1;32mGenerating...\033[1;m\n")
	if msg == '3': banner(); print("\n\n\t\t\033[1;31mTop of the range cannot be smaller than the minimum.\033[1;m\n")
	if msg == '4': banner(); print("\n\n\t\t\033[1;32mGenerating. this might take a while..\033[1;m\n")
	if msg == '5': banner(); print ("\n\n\t\t\033[1;31mUse only numbers\033[1;m\n")
	if msg == '6': banner(); print ("\n\n\t\t\033[1;31mUse only numbers or 'all'\033[1;m\n")
	if msg == '7': banner(); print("\n\n\t\t\033[1;31mQuitting.\033[1;m\n");
	if msg == '8': banner(); print("\n\n\t\t\033[1;31mNo such thing.\033[1;m\n")
	if msg == '9': banner(); print("\n\n\t\t\033[1;38mSuccessfully generated a list of numbers starting with {}.\033[1;m".format(args[0]))
	if msg == '10': print("\n\n\t\t\033[1;32mCounted \033[1;34m{}\033[1;m \033[1;32mlines.\033[1;m".format(args[0]))
	if msg == '11': banner(); print("\n\n\t\t\033[1;31mCOMPLY, OBEY, CAUTERIZE\033[1;m\n")
	if msg == '12': banner(); print("\n\t\tThis program runs in Python3 only.\n")


def main():
	if sys.version[0] != "3":
		display('12')
		sys.exit()

	else:
		user_input = input('''\


		\033[1;38mSelect an option:\033[1;m

		\033[1;31m[>]\033[1;m  \033[1;37m1)\033[1;m \033[1;32mGenerate a list of custom numbers\033[1;m
		\033[1;31m[>]\033[1;m  \033[1;37m2)\033[1;m \033[1;32mGenerate a list of cellphone numbers (israel)\033[1;m
		\033[1;31m[>]\033[1;m  \033[1;37m3)\033[1;m \033[1;32mGenerate a list of landline numbers (israel)\033[1;m
		\033[1;31m[>]\033[1;m  \033[1;37m4)\033[1;m \033[1;31mQuit properly\033[1;m

		''')

		if user_input == "1": banner(); process(user_input)
		elif user_input == "2": banner(); process(user_input)
		elif user_input == "3": banner(); process(user_input)
		elif user_input == "4": display('7'); time.sleep(1); os.system('cls' if os.name == 'nt' else 'printf "\033c"'); sys.exit()
		elif user_input == "404": banner(); webbrowser.open('https://www.youtube.com/watch?v=iRq7Muf6CKg'); display('11')

		else: display('8'); time.sleep(2); reset()

if __name__ == "__main__":
		reset()
