#! /usr/bin/python3

import webbrowser,  sys,  pyperclip

sys.argv #This accepts command line arguments

#check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() #This uses pyperclip to take from the clipboard

webbrowser.open('https://www.google.com/maps/place/' + address) #this opens the default browser to the url string, and concatenates the address string taken from arguments to take us where we need to go
