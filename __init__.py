# moduleplus.py
# 🧰 MODULEPLUS - Personal Python Toolbox
def get_web_text(url):
    response = requests.get(url)

    print("Status:", response.status_code)

    if response.status_code != 200:
        return "Couldn't access this webpage."

    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(" ", strip=True)
from bs4 import BeautifulSoup

def get_web_text(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(" ", strip=True)
# ==============================
# 🧮 BUILT-IN MATH MODULES
# ==============================

import math
import cmath
import statistics
import fractions
import decimal
import random
import numbers
def random_number(start, end):
    return random.randint(start, end)

# ==============================
# 📅 DATE & TIME
# ==============================

import datetime
import time
import calendar

# ==============================
# 📁 FILES & FOLDERS
# ==============================

import os
import pathlib
import shutil
import tempfile

# ==============================
# 🔤 TEXT & DATA
# ==============================

import string
import re
import json
import csv

# ==============================
# 📦 DATA TOOLS
# ==============================

import collections
import itertools
import functools
import heapq

# ==============================
# 💻 SYSTEM
# ==============================

import sys
import platform
import os
import pathlib

# ==============================
# 🌐 NETWORKING
# ==============================

import urllib
import socket

# ==============================
# 🔐 SECURITY & ENCODING
# ==============================

import hashlib
import base64
def sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()
def encode64(text):
    return base64.b64encode(text.encode()).decode()

def decode64(text):
    return base64.b64decode(text).decode()
# ==============================
# 🐢 BUILT-IN GRAPHICS
# ==============================

import turtle
import tkinter
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.simpledialog
import tkinter

def make_button(window, text, function):
    return tkinter.Button(
        window,
        text=text,
        command=function
    )

# ==============================
# 🔬 EXTERNAL PACKAGES
# ==============================

import numpy as np
import matplotlib.pyplot as plt
import requests


# ==============================
# 🥧 CONSTANTS
# ==============================

PI = math.pi
E = math.e
TAU = math.tau


# ==============================
# ➕ SIMPLEMATH
# ==============================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# ==============================
# 🚀 ADVANCEDMATH
# ==============================

def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def power(x, n):
    return x ** n


def square_root(x):
    return math.sqrt(x)


def factorial(x):
    return math.factorial(x)


def absolute(x):
    return abs(x)


def maximum(a, b):
    return max(a, b)


def minimum(a, b):
    return min(a, b)


# ==============================
# 📐 TRIGONOMETRY
# ==============================

def sine(x):
    return math.sin(x)


def cosine(x):
    return math.cos(x)


def tangent(x):
    return math.tan(x)


def degrees(x):
    return math.degrees(x)


def radians(x):
    return math.radians(x)


# ==============================
# 🔢 LOGARITHMS
# ==============================

def logarithm(x, base=10):
    return math.log(x, base)


def natural_log(x):
    return math.log(x)


def exponential(x):
    return math.exp(x)


# ==============================
# 🔄 ROUNDING
# ==============================

def floor(x):
    return math.floor(x)


def ceiling(x):
    return math.ceil(x)


def round_number(x, digits=0):
    return round(x, digits)


# ==============================
# 📐 GEOMETRY
# ==============================

def circle_area(radius):
    return PI * radius ** 2


def circle_circumference(radius):
    return 2 * PI * radius


def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(length, width):
    return 2 * (length + width)


def triangle_area(base, height):
    return 0.5 * base * height


# ==============================
# 💯 PERCENTAGES
# ==============================

def percentage(value, percent):
    return value * percent / 100


def percent_change(old, new):
    return ((new - old) / old) * 100


# ==============================
# 🌀 COMPLEX MATH
# ==============================

def complex_square_root(x):
    return cmath.sqrt(x)


def complex_phase(x):
    return cmath.phase(x)


# ==============================
# 🎲 RANDOM
# ==============================

def random_number(start, end):
    return random.randint(start, end)


# ==============================
# 🔬 NUMPY HELPERS
# ==============================

def array(values):
    return np.array(values)


def array_average(values):
    return np.mean(values)


def array_sum(values):
    return np.sum(values)


def array_max(values):
    return np.max(values)


def array_min(values):
    return np.min(values)


# ==============================
# 📊 MATPLOTLIB HELPERS
# ==============================

def plot_line(x, y):
    plt.plot(x, y)
    plt.show()


def plot_scatter(x, y):
    plt.scatter(x, y)
    plt.show()


def plot_bar(labels, values):
    plt.bar(labels, values)
    plt.show()


def plot_pie(labels, values):
    plt.pie(values, labels=labels)
    plt.show()


def plot_title(title):
    plt.title(title)


def plot_grid():
    plt.grid(True)


def save_plot(filename):
    plt.savefig(filename)


# ==============================
# 🌐 REQUESTS HELPERS
# ==============================

def get(url):
    return requests.get(url)


def get_text(url):
    return requests.get(url).text


def get_json(url):
    return requests.get(url).json()


# ==============================
# 🐢 TURTLE HELPERS
# ==============================

def new_turtle():
    return turtle.Turtle()


def turtle_square(t, size=100):
    for i in range(4):
        t.forward(size)
        t.right(90)


# ==============================
# 🎉 MODULEPLUS LOADED
# ==============================

print("ModulePlus loaded! 🧰🐍")
