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
  powerIsPressed = False  # A boolean of 
  # Botton Power
  # 1. Verify in real time captures what running or 
  # if Botton Power interacted with System State
  smnaState = subprocess.check_output(['termux-battery-status'])
  # 1.1. Decodify the smnaState for a normal text 
  smna_text = smnaState.decode('utf-8')
  # 2. Is rmnaka?
  chara_key = "present: true"
  if chara_key in smna_text:
    return True
  else:
    return False
  
# The function:
# Executes a prgn
def prgnFall():
  prgn = input("What is app open [Youtube=y, Acode=a]?  ")

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