from db import *
import os
import time
import winsound
from random import shuffle
from emoji import emojize
from main import *

shuffle(questions)

def checkAnswer():
    global checkpoint
    global checkUp
    if answer == questions[checkpoint][indexCorrectVariant]:
       print(emojize(f"Doğru cavab verdiniz! {moneys[checkpoint]}$ qazandınız :thumbs_up:"))
       checkpoint += 1 
    elif answer != questions[checkpoint][indexCorrectVariant] and checkpoint > 4 and checkpoint < 10 and answer != "x":
       print(emojize(f"Yanlış cavab verdiniz! Oyun bitdi, qazandığınız məbləğ : {moneys[4]} $ :money_with_wings:"))
       checkUp = False
    elif answer != questions[checkpoint][indexCorrectVariant] and checkpoint > 9 and answer != "x":
        print(emojize(f"Yanlış cavab verdiniz! Oyun bitdi, qazandığınız məbləğ : {moneys[9]} $ :money_with_wings:"))   
        checkUp = False
    elif answer != questions[checkpoint][indexCorrectVariant] and checkpoint < 6 and answer != "x":
        print(emojize(f"Yanlış cavab verdiniz! Oyun bitdi, qazandığınız məbləğ : 0 $ :money_with_wings:"))   
        checkUp = False
    elif answer == "x" and checkpoint > 4:
        print(f"Oyundan çəkildiniz :/ Qazandığınız məbləğ : {moneys[checkpoint - 1]} $")
        checkUp = False
        
def checkJokers():
    if answer == "1":
        time.sleep(0.5)
        os.system("cls")
        jokers.remove("1")
        for question in questions:
            if question == questions[checkpoint]:
                print()
                print(f"=== Question {checkpoint + 1} ===")
                print()
                print(f"{question[indexQuestion]}")
                print()
                if question[indexCorrectVariant] == "A":
                    print(f"A) {question[indexVariants][0]}")
                    print()
                    print(f"D) {question[indexVariants][3]}")
                    print()
                if question[indexCorrectVariant] == "B":
                    print(f"A) {question[indexVariants][1]}")
                    print()
                    print(f"D) {question[indexVariants][3]}")
                    print()
                if question[indexCorrectVariant] == "C":
                    print(f"A) {question[indexVariants][0]}")
                    print()
                    print(f"C) {question[indexVariants][2]}")
                    print()     
                if question[indexCorrectVariant] == "D":
                    print(f"B) {question[indexVariants][1]}")
                    print()
                    print(f"D) {question[indexVariants][3]}")
                    print() 
                print("Jokerləriniz : ")
                for j in jokers:
                    if j == "2":
                        print(f"{j} => Dosta zəng etmək")
                    elif j == "3":
                        print(f"{j} => Auditoriya")        
    if answer == "2":
        print(emojize("Dosta zeng edilir... :telephone_receiver:"))
        winsound.Beep(400, 2000)
        time.sleep(1)
        jokers.remove("2")
        print(f"Dostunuzun cavabı : {questions[indexCorrectVariant][2]}")
    if answer == "3":
        print("Auditoriya qerar verir...")
        time.sleep(1)
        jokers.remove("3")
        print(f"Auditoriyanın cavabı : {questions[indexCorrectVariant][2]}")        

while checkUp:
    if checkpoint == 0:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint==0:
            if answer in variants:
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 1:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 1:
            if answer in variants:
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 2:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 2:
            if answer in variants:
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 3:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 3:
            if answer in variants:
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 4:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 4:
            if answer in variants:
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 5:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 5:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 6:
        answer =ask_question(checkpoint)
        while checkUp and checkpoint == 6:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 7:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 7:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 8:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 8:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 9:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 9:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 10:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 10:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 11:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 11:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 12:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 12:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 13:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 13:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 14:
        answer = ask_question(checkpoint)
        while checkUp and checkpoint == 14:
            if answer in variants or answer == "x":
                checkAnswer()
            elif answer in jokers:
                checkJokers()
                answer = input("Seçim edin:")
            else:
                print("Yanlış daxil etdiniz!")
                answer = input("Seçim edin:")
    elif checkpoint == 15:
        print("Qalib oldunuzz!!")
        time.sleep(0.5)
        print("1 Milyon qazandın!")
        break


        
