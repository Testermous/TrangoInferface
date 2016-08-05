#Author: Dan Evert Testerman
#Email bugs to dantesterman@rocketmail.com
#This code is liscened under Copyleft.

import getpass, sys, telnetlib, time

def command_telnet(num, totalTries):
	if num == 0: #1st time run
		print("Commands:    \"testlink AP-IP SU-ID\"")
		print("or           \"rssi IP\"")
	else:
		print("Improper syntax.  Reiterating commands:")
		print("\"testlink AP-IP SU-ID\"")
		print("\"rssi IP\"")
	print("Special Command: \"c\" to close")
	command = input("Enter command:  ") #input() use to be raw_input()
	parserCommand = command.split(" ") #Splits the command string w/ spaces being the delimeter
	#Check and see if sent syntax is correct
	if parserCommand[0].lower() == "testlink":
		print("Works, telneting in...")
		testlink()
	elif parserCommand[0].lower() == "rssi":
		print("Works, telneting in...")
		rssi()
	elif parserCommand[0].lower() == "c":
		print("Closing the program.")
		sys.exit()
	else:
		totalTries += 1
		if totalTries >= 4:
			print("Too many tries.  Closing program.")
			sys.exit()
		else:
			command_telnet(1, totalTries)
		
def rssi():
	ipAddress = "10.128.41.93"
	password = b"Password"
	tn = telnetlib.Telnet(ipAddress)

	tn.read_until(b"Password: ")
	tn.write(password + b"\n")

	tn.read_until(b"#>")
	tn.write(b"rssi" + b"\n")
	tn.write(b"exit" + b"\n")

	print(tn.read_all())
	
def testlink():
	ipAddress = "10.128.41.6"
	password = b"WisperISP123"
	tn = telnetlib.Telnet(ipAddress)

	tn.read_until(b"Password: ")
	tn.write(password + b"\n")
	
	print("1")
	tn.read_until(b"#>", 2)
	print("2")
	tn.write(b"su testrflink 47" + b"\n")
	print("3")
	tn.write(b"exit" + b"\n")
	print("4")

	print(tn.read_all())
		
command_telnet(0, 0)


