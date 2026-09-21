# --- LICENSE HEADER ---
#  MIT License.
# Copyright (C) QMX Corporation (all maintainers, authors and collaborators).
# The relaBOY is licensed and released under 
#  MIT License.
# --- LICENSE HEADER ---


# --- Libs Importeds ---
import sqlite3
import os 
import subprocess
import time 

# Connect to SQLite
conn_lite = sqlite3.connect("rela.db")

# Create a table and a cursor of SQLite
cursor = conn_lite.cursor()
sqTable = cursor.execute("""CREATE TABLE IF NOT EXISTS
                                tb_query
                                (APP TEXT) 
                        """)

# Save/Commit the changes
conn_lite.commit()

# Close the sqTable
conn_lite.close()


# The Function:
# Monitoring the Power Botton, if press
# in the Botton: The Termux executes a prgn of
# What is open app 
def getBottonPower():
  # Not using root, 
  # a 'return True' is necessary.
  return True

  
# The function:
# Executes a prgn
def prgnFall():
  # The Menu
  print("| --- MENU OF ENTRIES --- |\n")
  print("| y/Y/Youtube/youtube= Youtube |\n")
  print("| a/A/Acode/acode = Acode |\n")
  print("| --- MENU OF ENTRIES --- |\n")
  # What open App?
  prgn = input("What open app?  \n")
  # 1. Verify 
  # Is y (Youtube)?
  if prgn in ["y", "Y", "Youtube", "youtube"]:
    # Executes the Youtube
    subprocess.run(['am', 'start', 'com.google.android.youtube'])
  # Is a (Acode)?
  elif prgn in ["a", "A", "Acode", "acode"]:
    # Executes the Acode
    subprocess.run(['am', 'start', 'com.fox.acode'])
  # Not, handling
  else:
    print("Not commands found.")

    
# The main Function 
def RelaBOT():
  # 1. Entry in a loop
  while True:
    # 2. Call the function
    result = getBottonPower()
    # 3. Verify this return 
    if result == True:
      prgnFall()
      time.sleep(478)
    else:
      time.sleep(2500)
      continue

# Executes the logic
RelaBOT()