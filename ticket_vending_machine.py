import pandas as pd
import datetime
import os
from pathlib import Path

# Get current date and time
now = datetime.datetime.now()

# Station dictionaries
Stations = {
    "Station": ["Krishnanagar", "Badkulla", "Ranaghat", "Chakdaha", "Kalyani", "Naihati", "Belgharia", "Dum Dum", "Sealdah"]
}
Stations2 = {
    0: "Krishnanagar",
    1: "Badkulla",
    2: "Ranaghat",
    3: "Chakdaha",
    4: "Kalyani",
    5: "Naihati",
    6: "Belgharia",
    7: "Dum Dum",
    8: "Sealdah"
}

# Display station list
view_station = pd.DataFrame(Stations)

# Input user data
name = input("name in short form:").upper().strip()
print(view_station)

# Collect station details and passenger info
while True:
    try:
        From = int(input("station from: "))
        if From in Stations2:
            list1 = Stations2[From]
            to = int(input("station to: "))
            if to in Stations2:
                list2 = Stations2[to]
                passen = int(input("enter passengers: "))
                amount = int(input("enter amount: "))
                break
            else:
                print("Station not found...")    
        else:
            print("Station not found...")    
    except ValueError:
        print("Error.. please enter an integer value.")

# Calculate total amount and generate ticket ID
total_amount = passen * amount
ticket_id = f"INR-{now.strftime('%Y%m%d%H%M%S')}"

# Create ticket content
ticket_contant = (
    "===============================================\n"
    "                       TRAIN TICKET                    \n"
    "===============================================\n"
    f" Ticket ID:        {ticket_id}\n"
    f" Date:               {now.strftime('%D')}\n"
    f" Time:               {now.strftime('%H:%M:%S')}\n"
    "------------------------------------------\n"
    f" From:             {list1}\n"
    f" To:                  {list2}\n"
    "------------------------------------------\n"
    f" Passengers:       {passen}\n"
    f" Total Amount:     {total_amount} ₹\n"
    "------------------------------------------\n"
    "          Thank you for traveling with us!  \n"
    "===============================================\n"
)

# Print ticket content
print(ticket_contant)
print()
print("Ticket saved....")

# Define path to save the ticket
doc_path = "/Users/LENOVO/OneDrive/Documents"
new_file = os.path.join(doc_path, f"TT-{name}-{ticket_id}.txt")

# Save ticket to file 
with open(new_file, 'w', encoding='utf-8') as f:
    f.write(ticket_contant)

# Open the file (on Windows)
os.startfile(new_file)
