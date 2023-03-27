import os
from emoji import emojize
import time
from functions import *
from db import *

def ask_question(checkpoint):
    for question in questions:
        time.sleep(1)
        os.system("cls")
        if question == questions[checkpoint]:
            print()
            print(f"=== Question {checkpoint + 1} ===")
            print()
            print(f"{question[indexQuestion]}")
            print()
            print(f"A) {question[indexVariants][0]}")
            print(f"B) {question[indexVariants][1]}")
            print(f"C) {question[indexVariants][2]}")
            print(f"D) {question[indexVariants][3]}")
            print()
            print("Jokerləriniz : ")
            for j in jokers:
                if j == "1":
                    print(f"{j} => 50/50")
                elif j == "2":   
                    print(f"{j} => Dosta zəng etmək")
                elif j == "3":   
                    print(f"{j} => Auditoriya")    
            print()    
            print(emojize(f"Sualın dəyəri : {moneys[checkpoint]}$ :money_with_wings:"))  
            print()  
            if checkpoint > 4:
                print("x => Pulu götürüb çəkilmək")
            answer = input("Seçim edin:")
            time.sleep(0.5)
            return answer

