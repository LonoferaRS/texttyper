# Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time, os, sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("clear")


typingPrint("Hello world...\n")
time.sleep(1)
typingPrint("You've entered the Matrix!\n")
time.sleep(1)

time.sleep(1)
typingPrint("Good bye!\n")
typingPrint("This screen will clear itself in 3..")
time.sleep(1)
typingPrint("2..")
time.sleep(1)
typingPrint("1..")
time.sleep(1)
clearScreen()