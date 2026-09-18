# Name: FANG ZILAI
# Assignment One
# ddl is 22/9/2026 23:59pm

import turtle
import colorsys

# ==========================================
# Task 1: Simple Calculator
# ==========================================
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")
if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operation")

print("\n-----------------------------------\n")

# ==========================================
# Task 2: QA Bot
# ==========================================
print("Question Answering Bot")
question = input("Ask me something: ")
if question == "hello":
    print("Bot: Hello! Nice to meet you.")
elif question == "python":
    print("Bot: Python is a language.")
elif question == "jetson":
    print("Bot: Jetson Nano is an AI computer.")
elif question == "ai":
    print("Bot: AI means Artificial Intelligence.")
elif question == "name":
    print("Bot: My name is Python Bot.")
else:
    print("Bot: Sorry, I don't understand.")

print("\n-----------------------------------\n")

# ==========================================
# Task 3: Turtle Drawing
# ==========================================
print("Turtle Drawing - Starting...")
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for i in range(100):
    color = colorsys.hsv_to_rgb(i / 100, 1.0, 1.0)
    t.pencolor(color)
    t.forward(i * 3)
    t.right(144)

turtle.done()
