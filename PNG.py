#!/usr/bin/python3
# coding: utf-8
###
###  Phone Numbers Generator v1.33
###
###  Copyright 2012 - 2019 404 <openSsme@gmail.com>
###
###  This program is free software; you can redistribute it and/or modify
###  it under the terms of the GNU General Public License as published by
###  the Free Software Foundation; either version 2 of the License, or
###  (at your option) any later version.
###
###  This program is distributed in the hope that it will be useful,
###  but WITHOUT ANY WARRANTY; without even the implied warranty of
###  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
###  GNU General Public License for more details.
###
###  You should have received a copy of the GNU General Public License
###  along with this program; if not, write to the Free Software
###  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
###  MA 02110-1301, USA.
###

import sys, time, mmap, os, webbrowser

os.system('mode con: cols=45 lines=90' if os.name == 'nt' else 'printf "\e[8;35;110t"')

def banner():

	print ('''\


	\033[1;37m--------------------------------------------------------------------------------------------
	============================================================================================

				    PHONE NUMBERS GENERATOR v1.33 BY\033[1;m

	\033[1;31m				██╗  ██╗ ██████╗ ██╗  ██╗
					██║  ██║██╔═████╗██║  ██║
					███████║██║██╔██║███████║
					╚════██║████╔╝██║╚════██║
					     ██║╚██████╔╝     ██║
					     ╚═╝ ╚═════╝      ╚═╝\033[1;m

	\033[1;37m=============================================================================================
	---------------------------------------------------------------------------------------------
	\033[1;m''')

def clear():

	os.system('cls' if os.name == 'nt' else 'printf "\033c"')
	return ''

class generator():

	def generate1():

		f = open(input("\n\n                \033[1;32mEnter output filename:  \033[1;m") + ".txt" , 'w')
		prefix = input("\n                \033[1;32mEnter a prefix:  \033[1;m")
		number = int(input ("\n                \033[1;32mEnter range minimum (exclude prefix):  \033[1;m") )
		limit = int(input ("\n                \033[1;32mEnter range maximum:  \033[1;m") )

		if number >= limit:
			Msg.msg3()
			time.sleep(3)
			clear()
			banner()
			main()

		Msg.msg1() if limit >= 1000000 else Msg.msg2()
		generator.action_generate(number, f, prefix, limit)

	def generate2():

		f = open(input("\n\n                \033[1;32mEnter output filename:  \033[1;m") + ".txt" , 'w')
		prefix = input("\n                \033[1;32mEnter carrier prefix number (050, 052, 053, 054, 057, 059):  \033[1;m")
		number = 1000000
		limit = 9999999

		Msg.msg4()

		generator.action_generate(number, f, prefix, limit)

	def generate3():

		f = open(input("\n\n                \033[1;32mEnter output filename:  \033[1;m") + ".txt" , 'w')
		prefix = input('\n' + "\033[1;32mEnter area code (02, 03, 04,072, 077, 08, 09):  \033[1;m")
		number = 5000000
		limit = 9999999

		Msg.msg4()

		generator.action_generate(number, f, prefix, limit)

	def action_generate(number, f, prefix, limit):

		# GENERATOR
		while number != limit:

			number = number+1
			f.write(str(prefix)+str(number)+'\n')
		f.close()

		# COUNTER
		f = open(f.name, "r+")
		buf = mmap.mmap(f.fileno(), 0)
		lines = 0
		readline = buf.readline
		while readline():
			lines += 1

		clear()
		banner()
		print('''\




		\033[1;38mDone generating list of numbers prefixed with '{}'.\033[1;m '''.format(prefix) + '''

		\033[1;32mCounted \033[1;34m{}\033[1;m \033[1;32mlines.\033[1;m

		'''.format(lines))

		main()

class Msg():

	def msg1():

		clear()
		banner()
		print('''\


		\033[1;32mGenerating. this might take a few seconds for a 7+ digits numbers..\033[1;m

		''')

	def msg2():

		clear()
		banner()
		print('''\


		\033[1;32mGenerating...\033[1;m

		''')

	def msg3():

		clear()
		banner()
		print('''\


		\033[1;32mFirst number must be smaller or equal to last number.\033[1;m

		''')

	def msg4():

		clear()
		banner()
		print('''\


		\033[1;32mGenerating. this might take a few seconds..\033[1;m

		''')

	def quitProperly():

		clear()
		banner()
		print('''\


		\033[1;31mQuitting.\033[1;m

		''')
		time.sleep(1)
		clear()
		sys.exit()

	def NST():

		clear()
		banner()
		print('''\


		\033[1;31mNo such thing.\033[1;m

		''')

	def fzf():

		clear()
		banner()
		webbrowser.open('https://www.youtube.com/watch?v=iRq7Muf6CKg')


def main():

	usrInput = input('''\


	\033[1;38mSelect an option:\033[1;m

	\033[1;31m[>]\033[1;m  \033[1;37m1)\033[1;m \033[1;32mGenerate custom range numbers\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m2)\033[1;m \033[1;32mGenerate cellphone numbers (israel)\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m3)\033[1;m \033[1;32mGenerate landline numbers (israel)\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m4)\033[1;m \033[1;31mQuit properly\033[1;m

	''')

	if usrInput == "1":

		clear()
		banner()
		generator.generate1()

	elif usrInput == "2":

		clear()
		banner()
		generator.generate2()

	elif usrInput == "3":

		clear()
		banner()
		generator.generate3()

	elif usrInput == "4":

		Msg.quitProperly()

	elif usrInput == "404":

		Msg.fzf()
		clear()
		banner()
		main()

	else:
		Msg.NST()
		time.sleep(2)
		clear()
		banner()
		main()

if __name__ == "__main__":

	clear()
	banner()
	main()
