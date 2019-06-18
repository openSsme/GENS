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

		f = open(input("\n\n                \033[1;32mEnter output file name (ENTER to go back):  \033[1;m") + ".txt" , 'w')
		if f.name == ".txt":
			os.system('del .txt' if os.name == 'nt' else 'rm .txt')
			clear()
			banner()
			main()
		else:
			p = input("\n                \033[1;32mEnter a prefix:  \033[1;m")
			n = int(input("\n                \033[1;32mEnter range minimum (exclude prefix):  \033[1;m"))
			if n >= l:
				Msg.msg3()
				time.sleep(3)
				clear()
				banner()
				main()
			else:
				l = int(input("\n                \033[1;32mEnter range maximum:  \033[1;m"))
				Msg.msg1() if l >= 1000000 else Msg.msg2()
				generator.action_generate(n, f, p, l)

	def generate2():

		f = open(input("\n\n                \033[1;32mEnter output file name (ENTER to go back):  \033[1;m") + ".txt" , 'w')
		if f.name == ".txt":
			os.system('del .txt' if os.name == 'nt' else 'rm .txt')
			clear()
			banner()
			main()
		else:
			p = input("\n                \033[1;32mEnter prefix (carrier prefix, area code, country code):  \033[1;m")
			n = 1000000
			l = 9999999

			Msg.msg4()
			generator.action_generate(n, f, p, l)

	def generate3():

		f = open(input("\n\n                \033[1;32mEnter output file name (ENTER to go back):  \033[1;m") + ".txt" , 'w')
		if f.name == ".txt":
			os.system('del .txt' if os.name == 'nt' else 'rm .txt')
			clear()
			banner()
			main()
		else:
			p = input("\n		\033[1;32mEnter area code (area code, country code+area code etc):  \033[1;m")
			n = 5000000
			l = 9999999

			Msg.msg4()
			generator.action_generate(n, f, p, l)

	def action_generate(n, f, p, l):

		# GENERATOR
		while n != l:

			n = n+1
			f.write(str(p)+str(n)+'\n')

		f.close()

		# COUNTER
		f = open(f.name, "r+")
		b = mmap.mmap(f.fileno(), 0)
		l = 0
		r = b.readline
		while r():

			l += 1

		f.close()
		clear()
		banner()
		print('''\


		\033[1;38mDone generating list of numbers prefixed with '{}'.\033[1;m '''.format(p) + '''

		\033[1;32mCounted \033[1;34m{}\033[1;m \033[1;32mlines.\033[1;m

		'''.format(l))

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


		\033[1;32mRange minimum must be smaller or equal to range maximum.\033[1;m

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

	user_input = input('''\


	\033[1;38mSelect an option:\033[1;m

	\033[1;31m[>]\033[1;m  \033[1;37m1)\033[1;m \033[1;32mGenerate custom range numbers\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m2)\033[1;m \033[1;32mGenerate cellphone numbers (israel)\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m3)\033[1;m \033[1;32mGenerate landline numbers (israel)\033[1;m
	\033[1;31m[>]\033[1;m  \033[1;37m4)\033[1;m \033[1;31mQuit properly\033[1;m

	''')

	if user_input == "1":

		clear()
		banner()
		generator.generate1()

	elif user_input == "2":

		clear()
		banner()
		generator.generate2()

	elif user_input == "3":

		clear()
		banner()
		generator.generate3()

	elif user_input == "4":

		Msg.quitProperly()

	elif user_input == "404":

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
