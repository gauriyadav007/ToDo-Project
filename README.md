📝 ToDo Management System — Django Project

A complete ToDo Management Web Application built using Django, featuring secure user authentication, full task CRUD operations, a trash/restore system, and a clean UI built with HTML, CSS, JavaScript.
This project demonstrates proper Django architecture, user sessions, and ORM-based database management.

📌 Features Overview

🔐 User Authentication:
✅ User Registration
✅ User Login (username + password)
✅ Forgot Password option
✅ User Profile page after login
Displays username, full name, email
& Edit profile option
✅ Logout functionality

🏠 Dashboard:
Displays all tasks created by the logged-in user.
Clean UI with buttons for editing, deleting, and managing tasks.

🗂️ Task Operations (CRUD):
✨ Create:-
Add Task form &
Buttons: Add, Cancel.
📝 Read:-
View all tasks on the homepage.
Tasks displayed in clean card/list layout.
✏️ Update:-
Update Task form &
Buttons: Update, Cancel.
🗑 Delete:-
Delete Task moves the task to Trash.
Edit Task with Save & Cancel options.

🗑️ Trash / Recycle Bin Functionality:
For Individual Tasks:-
♻️ Restore Task &
❌ Delete Permanently.
Bulk Trash Management:-
🔄 Restore All Tasks &
🧹 Delete All Tasks Permanently.

💬 Popup Notifications:
Every action gives instant feedback to the user:-
Login success,
Logout,
Task Added,
Task Updated,
Task Deleted,
Task Restored.

🧠 Django ORM Usage:
This project does not use raw SQL.
All operations use Django’s ORM.

🛠 Tech Stack:
Component	Technology:-
Frontend:	HTML, CSS, JavaScript
Backend:	Python, Django
Database:	SQLite (default Django DB)
Authentication:	Django Auth System
ORM:	Django ORM
Message Alerts:	Django Messages Framework
