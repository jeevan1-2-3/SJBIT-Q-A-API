🎓 SJBIT Q&A API
An AI-powered Question & Answer API for S.J.B Institute of Technology, Bengaluru
Ask anything about SJBIT — get instant, accurate answers!

📌 What is This Project?
This is a REST API built using Flask and Groq AI that acts like a smart chatbot for SJBIT college.

You ask a question → API sends it to Groq AI → AI answers → You get the response
Think of it like a 24/7 college helpdesk that never sleeps! 🌙

🛠️ Tech Stack
Tool	Purpose
🐍 Python	Programming language
🌐 Flask	Web framework to create the API
🧠 Groq AI (LLaMA 3.3 70B)	AI brain that generates answers
🔐 python-dotenv	Loads secret API key from .env file
📦 Virtual Environment	Keeps project dependencies isolated
📁 Project Structure
sjbit-qa-api/
│
├── app.py              ← Main Flask server (routes & logic)
├── prompt.py           ← SJBIT knowledge + prompt builder
├── .env                ← Secret API key (never push to GitHub!)
├── .env.example        ← Template showing what keys are needed
├── .gitignore          ← Files to ignore in Git
├── requirements.txt    ← List of packages to install
└── README.md           ← You are here! 📍
⚙️ How It Works
┌─────────────┐     POST /ask      ┌─────────────┐     API Call     ┌─────────────┐
│             │ ─────────────────► │             │ ───────────────► │             │
│    User     │                    │  Flask API  │                  │   Groq AI   │
│             │ ◄───────────────── │  (app.py)   │ ◄─────────────── │  (LLaMA 3)  │
└─────────────┘     JSON Answer    └─────────────┘     AI Answer    └─────────────┘
User sends a question via POST request
Flask receives and validates the question
prompt.py builds a complete prompt with SJBIT knowledge
Groq AI reads the prompt and generates an answer
Flask sends the answer back as JSON
🚀 Getting Started
Prerequisites
Python 3.8 or above
Groq API Key (free at console.groq.com)
Git installed
Step 1 — Clone the Repository
git clone https://github.com/YOUR_USERNAME/sjbit-qa-api.git
cd sjbit-qa-api
Step 2 — Create Virtual Environment
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
You should see (venv) in your terminal ✅

Step 3 — Install Dependencies
pip install -r requirements.txt
Step 4 — Set Up API Key
Create a .env file in the project root:

# .env
GROQ_API_KEY=your_groq_api_key_here
🔑 Get your free API key at console.groq.com
⚠️ Never share this key or push it to GitHub!

Step 5 — Run the Server
python app.py
You should see:

✅ Groq API Key loaded successfully
🚀 Starting SJBIT Q&A API...
📍 Visit http://127.0.0.1:5000 to see if it's running
📮 Send POST requests to http://127.0.0.1:5000/ask
📮 API Endpoints
1. Home — GET /
Check if the API is running.

Request:

GET http://localhost:5000/
Response:

{
  "message": "🎓 Welcome to the SJBIT Q&A API!",
  "status": "running",
  "how_to_use": {
    "method": "POST",
    "endpoint": "/ask",
    "body_format": {
      "question": "Type your SJBIT-related question here"
    }
  }
}
2. Ask Question — POST /ask
Send a question and get an AI-generated answer.

Request:

POST http://localhost:5000/ask
Content-Type: application/json
{
  "question": "What courses does SJBIT offer?"
}
Success Response:

{
  "question": "What courses does SJBIT offer?",
  "answer": "SJBIT offers undergraduate programs in CSE, ISE, ECE, EEE, Mechanical, and Civil Engineering...",
  "status": "success"
}
Error Response:

{
  "error": "Question cannot be empty.",
  "status": "error"
}
💬 Example Questions to Try
✅ "What branches does SJBIT offer?"
✅ "How do I get admission to SJBIT?"
✅ "Does SJBIT have a hostel facility?"
✅ "What companies recruit from SJBIT?"
✅ "What is the attendance requirement at SJBIT?"
✅ "Is SJBIT affiliated to VTU?"
✅ "What is the location of SJBIT?"
🔐 Security Best Practices
Practice	How We Did It
API Key hidden	Stored in .env file
.env not uploaded	Added to .gitignore
Template provided	.env.example shows required keys
Virtual environment	Isolated dependencies
🧠 How the AI Knows About SJBIT
The AI gets SJBIT information through a System Prompt in prompt.py.

system_context = """
You are a helpful assistant for SJBIT.
You know about branches, admission, fees,
hostel, placements, and campus facilities...
"""
The system prompt acts like a job description given to the AI before it answers any question.

🌐 Testing with Postman
Open Postman
Select POST method
Enter URL: http://localhost:5000/ask
Go to Body → select raw → select JSON
Type:
{
  "question": "What is SJBIT?"
}
Click Send
See the answer! ✅
❗ Common Errors & Fixes
Error	Reason	Fix
GROQ_API_KEY not found	.env file missing	Create .env and add your key
400 Bad Request	Empty or missing question	Send proper JSON with question field
500 Internal Server Error	Groq API issue	Check your API key is valid
ModuleNotFoundError	Packages not installed	Run pip install -r requirements.txt
👩‍💻 Author
*Jeevan M
Task 3.1 — OpenAI-Based Q&A API
SJBIT Internship Project

📞 SJBIT Contact
🌐 Website: www.sjbit.edu.in
📞 Phone: 080-28432945
📍 Location: BGS Health & Education City, Uttarahalli-Kengeri Main Road, Bangalore - 560060
💡 Note: This project uses Groq AI (LLaMA model) instead of OpenAI — same concept, faster responses, and free tier available!
