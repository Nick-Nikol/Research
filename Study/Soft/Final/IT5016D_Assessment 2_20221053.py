#Initialize counter variable for ticket numbers
counter = 1
1

#Dictionary to store ticket information
tickets = {}

import random
import string

#Function to generate a new password
def generate_password(staffID, creator_name):
  password_length = 5
  password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
  return password

#Function to submit a new ticket
def submit_ticket(staffID, creator_name, email, description):
  global counter
  ticket_num = counter + 2001
  if "Password Change" in description:
    password = generate_password(staffID, creator_name)
  else:
    password = "N/A"
  tickets[ticket_num] = {"Staff ID": staffID, "Creator Name": creator_name, "Email": email, "Description": description, "Password": password, "Status": "Open", "Response": "Not Yet Provided"}
  counter += 1
  print("Ticket successfully submitted with ticket number", ticket_num)

#Function to Respond to ticket
def respond_to_ticket(ticket_num, response):
  if ticket_num not in tickets:
    print("Invalid ticket number.")
  else:
    ticket = tickets[ticket_num]
    if ticket["Status"] == "Open":
      ticket["Response"] = response
      ticket["Status"] = "Resolved"
      print("Response added to ticket", ticket_num)
    else:
      print("Ticket", ticket_num, "is not open.")

#Function to display all tickets
def display_tickets():
  for ticket_num in tickets:
    ticket = tickets[ticket_num]
    print("Ticket Number: {:<5} Staff ID: {:<15} Creator Name: {:<20} Email: {:<30}".format(ticket_num, ticket["Staff ID"], ticket["Creator Name"], ticket["Email"]))
    print("Description: {:<40} Password: {:<10} Status: {:<10} Response: {:<20}".format(ticket["Description"], ticket["Password"], ticket["Status"], ticket["Response"]))
    print()

#Function to re-open a resolved ticket
def reopen_ticket(ticket_num):
  if ticket_num not in tickets:
    print("Invalid ticket number.")
  else:
    ticket = tickets[ticket_num]
    if ticket["Status"] == "Resolved":
      ticket["Status"] = "Open"
      print("Ticket", ticket_num, "re-opened.")
    else:
      print("Ticket", ticket_num, "is not resolved.")

def ticket_status():
  open_count = 0
  resolved_count = 0
  closed_count = 0
  for ticket_num in tickets:
    ticket = tickets[ticket_num]
    if ticket["Status"] == "Open":
      open_count += 1
    elif ticket["Status"] == "Resolved":
      resolved_count += 1
    elif ticket["Status"] == "Closed":
      closed_count += 1
  print("Number of open tickets:", open_count)
  print("Number of resolved tickets:", resolved_count)
  print("Number of closed tickets:", closed_count)


# Display menu
while True:
  print("Welcome to the Help Desk Ticket System")
  print("1. Submit a new ticket")
  print("2. Display all tickets")
  print("3. Respond to a ticket")
  print("4. Re-open a resolved ticket")
  print("5. See ticket status")
  print("6. Quit")
  choice = int(input("Enter your choice: "))

  if choice == 1:
    staffID = input("Enter Staff ID: ")
    creator_name = input("Enter Creator Name: ")
    email = input("Enter Contact Email: ")
    print("If you need to change password type Password change in desc")
    description = input("Enter Description of Issue: ")
    submit_ticket(staffID, creator_name, email, description)
  elif choice == 2:
    display_tickets()
  elif choice == 3:
    ticket_num = int(input("Enter Ticket Number: "))
    response = input("Enter Response: ")
    respond_to_ticket(ticket_num, response)
  elif choice == 4:
    ticket_num = int(input("Enter Ticket Number: "))
    reopen_ticket(ticket_num)
  elif choice == 5:
    ticket_status()
  elif choice == 6:
    break
  else:
    print("Invalid choice.")