#!/usr/bin/python

"""
# Web Path Fuzzer 
# 2017 \ LyJoker
""" 

import sys
import os
import socket
import httplib
import httplib2
import ssl
import requests
os.system("clear")
print "\t################################################################"
print "\t#                                                              #"
print "\t#                   WEB HOST PATH FUZZER.v4                    #"
print "\t#            Checking Certain Files for Existence              #"
print "\t#                      In Multi Targets                        #"
print "\t#                                          By LyJoker \ 2017   #"
print "\t################################################################\n"

targetlistt = str(raw_input(" #~ Enter Targets List Path Formatted as (IP:0.0.0.0 or site:www.site.com) : "))
targetlist = targetlistt.replace('"', '')
linkslistt = str(raw_input(" #~ Enter Links List Path Formatted as ( /path/file.php ) : "))
linkslist = linkslistt.replace('"', '')

def fuzz(targetlist,linkslist):
	try:
		global var1
		global var2
		var1=0 #Targets
		var2=0 #Files
	
		targfile = open(targetlist, "r")
		targlist = targfile.read()
		targlist = targlist.split("\n")
		
		linksfile = open(linkslist, "r")
		linkss = linksfile.read()
		linkss = linkss.split("\n")
		global t
		for t in targlist :
			internetconnection()
			site_pors()
			var1 = var1 + 1
			for lin in linkss :
				try:
					global site
					try:
						try:
							_create_unverified_https_context = ssl._create_unverified_context
						except AttributeError:
							pass
						else:
							ssl._create_default_https_context = _create_unverified_https_context
						#host = site + lin
						host = t +"/"+ lin
						print ("\t [#] Checking  " + host)
						h = httplib2.Http(disable_ssl_certificate_validation=True)
						response, content = h.request(str(host), 'HEAD')
						#connection = httplib.HTTPConnection(site)
						#connection.request("HEAD",lin)
						#response = connection.getresponse()
						if response.status == 200:
							var2 = var2 + 1
							print "%s %s" % ( "\n\n---->>>  " + host, "Success File Found!\n")
							report = open('Result.txt','a')
							report.write("\nFile Found :- \n\n")
							report.write("  "+ str(host) +"\n")
							report.close()
							pass
						elif response.status == 401:
							var2 = var2 + 1
							print "%s %s" % ( "\n\n---->>>  " + host, "Possible File Found ! \n")
							report = open('Result.txt','a')
							report.write("\nPossible File Response !  :- \n\n")
							report.write("  "+ str(host) +"\n")
							report.close()
						elif response.status == 404:
							##connection.close()
							var2 = var2
							pass
						elif response.status == 302:
							#print ("\t [#] Checking With SSL  " + host)
							#connection = httplib.HTTPSConnection(site)
							#connection.request("HEAD",lin)
							#response = connection.getresponse()
							#if response.status == 200:
							#	var1 = var1 + 1
							#	print "%s %s" % ( "\n\n---->>>  " + host, "Possible File Found !\n")
							#	break
							#else:
							#connection.close()
							var2 = var2
							pass
						#	print "%s %s" % ("\n>>>" + host, "Possible File Found (302 - Redirect)")
						elif response.status == 403:
							#connection.close()
							var2 = var2
							pass
						elif response.status == 504:
							var2 = var2
							pass
						else:
							print "%s %s %s" % (host, " Interesting response:", response.status)
							report = open('Result.txt','a')
							report.write("\n Something Wrong With Host It Self ! \n\n")
							report.write("  "+ str(host) +"\n")
							report.close()
							#connection.close()
							var2 = var2
							pass
					except httplib2.ServerNotFoundError:
						print ("\n\n\t       [!] Make Sure Paths List Correctly Written [!]\
	            \n          Possible False Format at Line Number (" + str(var2) +") >--> " + str(lin) +" \n")
						exit()
					except httplib2.RelativeURIError:
						print ("\n\n\t       [!] Make Sure Paths List Correctly Written [!]\
	            \n          Possible False Format at Line Number (" + str(var2) +") >--> " + str(lin) +" \n")
						exit()
					except httplib.InvalidURL:
						print ("\n\n\t       [!] Make Sure Paths List Correctly Written [!]\
	            \n          Possible False Format at Line Number (" + str(var2) +") >--> " + str(lin) +" \n")
						exit()
					except httplib.BadStatusLine:
						pass
					except httplib.ResponseNotReady:
						print ("\n\n\t [!] Error occured, Internet too Slow ! , Maybe You Need To Use a Proxy [!] ")
						report = open('DeadTargets.txt','a')
						report.write(str(t)+"\n")
						report.close()
						final_report()
						#exit()
						break
					except httplib2.RedirectLimit:
						print ("\n\n\t [!] Error occured, Target Got So Many Redirect ! , Check The Host and Try Again Later [!] ")
						report = open('DeadTargets.txt','a')
						report.write(str(t)+"\n")
						report.close()
						final_report()
						#exit()
						break
					except socket.error:
						print ("\n\n\t [!] Error occured, Internet too Slow ! , Maybe You Need To Use a Proxy [!] ")
						report = open('DeadTargets.txt','a')
						report.write(str(t)+"\n")
						report.close()
						final_report()
						#exit()
						break
					except (KeyboardInterrupt):
						print "\n\t[!] Session Interrupted"		
						exit()
				except (KeyboardInterrupt):
					print "\n\t[!] Session Interrupted"
					exit()
			else:
				pass
		final_report()
	except KeyboardInterrupt:
		print "\n[*] Exiting program .. "
		sys.exit(1)
		
		

def final_report():
	global var1
	global var2
	global targets
	global linkss
	print("\n\n   [$]====== Fuzzing Completed ======[$]\n")
	print("       ----> " + str(var2) + " Total Files Found")
	print("       ----> " + str(var1) + " Total Targets Scanned")
	print("       Expected Scans is " + str(len(targets)*len(linkss)))
	print("          Scans Made is  " + str(var1*var2))
	print("\n   \!/ Details Will Be Find in >> Result.txt ;) \!/ ")

def internetconnection():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('8.8.8.8',53))
	if result == 0:
		pass
	else:
		print ("\n\n Make Sure Internet is Connected .. and Try Again !! ")
		sys.exit(1)


def check_ssl(url):
	try:
		c = httplib2.Http(disable_ssl_certificate_validation=True)
		response, content = c.request(str(url), 'GET')
		#response = c.getresponse()
		#print(response.status)
		if response.status == 200:
			f = content
			ff = f.find("SSL-enabled")
			if ff == 0:
				return False
			else :
				return True
			return True
		else:
			return False
	except socket.error:
		pass
	except ssl.SSLError:
		pass
	except httplib2.SSLHandshakeError:
		pass
	except httplib.ResponseNotReady:
		return True
		

def site_pors():

		global t
		checkit = t.find("http://")
		checkit2 = t.find("https://")
		if checkit == 0:
			pass
		elif checkit2 == 0:
			pass
		else:
			print("\n                       Determining Protocol Type <HTTP\HTTPS> \n")
			if check_ssl(('https://'+t)) == True:
				t = ('https://'+t)
			else:
				t = ('http://'+t)

def check():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('8.8.8.8',53))
	if result == 0:
		try:
			global targets
			global linkss
			list = open(targetlist, "r")
			targets = list.readlines()
			k = 0
			while k < len(targets):
				targets[k] = targets[k].strip()
				k += 1
		except IOError:
			print "\n [*] Error: check your Targets list path \n"
			sys.exit(1)
		except KeyboardInterrupt:
			print "\n [*] Exiting program ..\n"
			sys.exit(1)
		try:
			list = open(linkslist, "r")
			linkss = list.readlines()
			k = 0
			while k < len(linkss):
				linkss[k] = linkss[k].strip()
				k += 1
		except IOError:
			print "\n [*] Error: check your Links list path \n"
			sys.exit(1)
		except KeyboardInterrupt:
			print "\n [*] Exiting program ..\n"
			sys.exit(1)
		try:
			print "\n  [*] Loaded :" , len(targets)   , "Targets .."
			print "  [*] Loaded :"  , len(linkss) , " Path's To Fuzz With " 
			print "\n  [*] Fuzzing, please wait ... \n"
		except KeyboardInterrupt:
			print "\n [*] Exiting program ..\n"
			sys.exit(1)
		try:
			fuzz(targetlist,linkslist)
		except KeyboardInterrupt:
			print "\n [*] Exiting program ..\n"
			sys.exit(1)
	else:
		print ("\n\n Make Sure Internet is Connected .. and Try Again !! ")
		sys.exit(1)
if __name__ == '__main__':
	check()
