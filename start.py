from bs4 import BeautifulSoup
import requests
import os
import urllib.request
import urllib3
import re
import csv
import subprocess

class ParserCore:
       def __init__(self, file):
           self.file = file
           self.__test_file()


       def __test_file(self):
           if os.path.isfile(self.file):
              with open(self.file, "r") as f_obj:
                     
           else:
              raise ValueError("Должен быть файл")

       def 


a  = ParserCore('OptOnline.csv')

# Tools.by
# Строительный Инструмент
# Fermer 
# Eco 
# Startul 
# Toptul 
# Wortex 
# Solaris 
# Oleo-Mac 
# Fiskars 
# Gepard 
# Юпитер 
# Starfix 
# ВОЛАТ 
# Sola 
# Wilo 
# Telwin 
# Slowik 
# Molot 


# http://th-tool.by/
# Авто Инструмент
# BaumAuto
# Big Red
# BRAUMAUTO
# D&D
# FORCEKRAFT
# Forsage
# Forsage electro
# FORSAGE kids
# HCB
# JTC
# KINGTUL
# KingTul kraft
# KINGTUL profi
# KINGTUL(SK)
# M7
# MARSHAL
# Partner
# Prowin
# Rotake


# http://h-d.by/
# CYNEL
# FLO
# GAV
# GEKO
# GERLACH
# H-D
# JUCO
# LUND
# LUXI
# NORMA
# POWER UP
# POWERUP
# PROWIN
# STHOR
# TOYA
# VOREL
# YATO
# Zeta
# ZMM MAXPOL
# Сибиар
