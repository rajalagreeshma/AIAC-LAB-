#Lab 20 – Security Testing: Identifying Vulnerabilities in AI- Generated Code

"""Task 1 – Input Validation Check
Task:
Analyze an AI-generated Python login script for input validation
vulnerabilities.
Instructions:
• Prompt AI to generate a simple username-password
login program.
• Review whether input sanitization and validation are
implemented.
• Suggest secure improvements (e.g., using re for input
validation).
Expected Output:
• A secure version of the login script with proper input
validation."""

# Simple AI-generated login script (insecure)
users = {"admin": "password123", "user": "mypassword"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid credentials.")




import re
import hashlib

# Store hashed passwords instead of plain text
users = {
    "admin": hashlib.sha256("password123".encode()).hexdigest(),
    "user": hashlib.sha256("mypassword".encode()).hexdigest()
}

def validate_username(username):
    # Allow only alphanumeric usernames, 3–15 chars
    return re.fullmatch(r"[A-Za-z0-9]{3,15}", username) is not None

def validate_password(password):
    # Require at least 8 chars, one digit, one letter
    return re.fullmatch(r"(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}", password) is not None

username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if not validate_username(username):
    print("Invalid username format. Use 3–15 alphanumeric characters.")
elif not validate_password(password):
    print("Invalid password format. Must be at least 8 characters with letters and numbers.")
else:
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_pw:
        print("Login successful!")
    else:
        print("Invalid credentials.")




"""Task 2 – SQL Injection Prevention
Task:
Test an AI-generated script that performs SQL queries on a
database.
Instructions:
• Ask AI to generate a Python script using SQLite/MySQL to
fetch user details.
• Identify if the code is vulnerable to SQL injection (e.g.,
using string concatenation in queries).
• Refactor using parameterized queries (prepared
statements).
Expected Output:
• A secure database query script resistant to SQL
injection."""

import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")

# ❌ Vulnerable to SQL injection
query = "SELECT * FROM users WHERE username = '" + username + "';"
cursor.execute(query)

result = cursor.fetchone()
if result:
    print("User found:", result)
else:
    print("No such user.")


import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ").strip()

# ✅ Secure: use parameterized query
query = "SELECT * FROM users WHERE username = ?;"
cursor.execute(query, (username,))

result = cursor.fetchone()
if result:
    print("User found:", result)
else:
    print("No such user.")



import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="usersdb"
)
cursor = conn.cursor()

username = input("Enter username: ").strip()

# ✅ Secure query with %s placeholder
query = "SELECT * FROM users WHERE username = %s;"
cursor.execute(query, (username,))

result = cursor.fetchone()
if result:
    print("User found:", result)
else:
    print("No such user.")







"""Task 3 – Cross-Site Scripting (XSS) Check
Task:
Evaluate an AI-generated HTML form with JavaScript for XSS
vulnerabilities.
Instructions:
• Ask AI to generate a feedback form with JavaScript-based
output.
• Test whether untrusted inputs are directly rendered
without escaping.
• Implement secure measures (e.g., escaping HTML
entities, using CSP).
Expected Output:
• A secure form that prevents XSS attacks."""
<!DOCTYPE html>
<html>
<head>
  <title>Feedback Form</title>
</head>
<body>
  <h2>Feedback</h2>
  <form id="feedbackForm">
    <label for="feedback">Enter your feedback:</label><br>
    <input type="text" id="feedback" name="feedback">
    <button type="submit">Submit</button>
  </form>

  <div id="output"></div>

  <script>
    document.getElementById("feedbackForm").addEventListener("submit", function(e) {
      e.preventDefault();
      var feedback = document.getElementById("feedback").value;
      // ❌ Vulnerable: directly injects user input into HTML
      document.getElementById("output").innerHTML = "You said: " + feedback;
    });
  </script>
</body>
</html>





<!DOCTYPE html>
<html>
<head>
  <title>Secure Feedback Form</title>
  <!-- ✅ CSP: prevents inline scripts and unsafe eval -->
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; object-src 'none';">
</head>
<body>
  <h2>Feedback</h2>
  <form id="feedbackForm">
    <label for="feedback">Enter your feedback:</label><br>
    <input type="text" id="feedback" name="feedback">
    <button type="submit">Submit</button>
  </form>

  <div id="output"></div>

  <script>
    function escapeHTML(str) {
      return str.replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;")
                .replace(/"/g, "&quot;")
                .replace(/'/g, "&#039;");
    }

    document.getElementById("feedbackForm").addEventListener("submit", function(e) {
      e.preventDefault();
      var feedback = document.getElementById("feedback").value;
      // ✅ Safe: escape before rendering
      document.getElementById("output").textContent = "You said: " + escapeHTML(feedback);
    });
  </script>
</body>
</html>







"""Task 4 – Real-Time Application: Security Audit of AI-
Generated Code
Scenario:
Students pick an AI-generated project snippet (e.g., login form,
API integration, or file upload).
Instructions:
• Perform a security audit to detect possible
vulnerabilities.
• Prompt AI to suggest secure coding practices to fix
issues.
• Compare insecure vs secure versions side by side.
Expected Output:
• A security-audited code snippet with documented
vulnerabilities and fixes."""
from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    # ❌ Directly saves file with user-provided filename
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
    return "File uploaded successfully!"



from flask import Flask, request, abort
import os
import re
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        abort(400, "No file part")
    file = request.files["file"]

    if file.filename == "":
        abort(400, "No selected file")

    if not allowed_file(file.filename):
        abort(400, "File type not allowed")

    # ✅ Sanitize filename
    filename = secure_filename(file.filename)

    # ✅ Enforce size limit
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    if size > MAX_FILE_SIZE:
        abort(400, "File too large")

    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return "File uploaded securely!"






"""Task 5 – Insecure Data Serialization Check
Task:
Evaluate AI-generated code that uses pickle for saving user
data.
Instructions:
• Ask AI to generate a script using pickle.load().
• Explain why untrusted pickle data is dangerous.
• Replace with safer formats like JSON.
Expected Output:
• Secure serialization code using JSON instead of pickle."""

import pickle

# ❌ Insecure: using pickle to load user data
with open("userdata.pkl", "rb") as f:
    user_data = pickle.load(f)

print("Loaded user data:", user_data)



import json

# ✅ Secure: using JSON for serialization
with open("userdata.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)

print("Loaded user data:", user_data)
