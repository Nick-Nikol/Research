Help Desk Ticket System
This is a simple command-line based ticket system for a help desk. It allows users to submit new tickets, display all tickets, respond to tickets, re-open resolved tickets, and see the status of tickets.

Features
Submit a new ticket: Allows users to submit a new ticket by entering their staff ID, creator name, contact email, and a description of the issue. If the description includes the phrase "Password Change", a password will be generated for the user.
Display all tickets: Shows all the tickets that have been submitted, including the ticket number, staff ID, creator name, email, description, password (if applicable), status, and response (if provided).
Respond to a ticket: Allows users to provide a response to an open ticket by entering the ticket number and the response. The ticket's status will be updated to "Resolved".
Re-open a resolved ticket: Allows users to re-open a resolved ticket by entering the ticket number. The ticket's status will be updated to "Open".
See ticket status: Shows the number of open tickets, resolved tickets, and closed tickets.

Running the ticket system
Download the script Helpdesk.py.
Open a terminal and navigate to the directory where the script is saved.
Run the script using the Python interpreter: 'python helpdesk.py'
Follow the prompts to use the ticket system.

Exiting the ticket system
To exit the ticket system, select the option to quit when prompted.

Notes
The ticket system is designed to be used in a command-line interface.
The ticket numbers are automatically generated and start at 2001.
The passwords generated for users are randomly generated and contain 5 characters, consisting of letters and digits.