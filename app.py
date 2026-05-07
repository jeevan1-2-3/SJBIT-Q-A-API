# app.py
from flask import Flask, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
from prompt import build_sjbit_prompt


# Load .env file
load_dotenv()

# Initialize Flask
app = Flask(__name__)

# Load Groq API key
api_key = os.getenv("sjbit-key")

if not api_key:
    print("❌ ERROR: sjbit-key not found in .env file!")
else:
    print("✅ Groq API Key loaded successfully")

# Initialize Groq client
client = Groq(api_key=api_key)


# ── ROUTE 1: Home ─────────────────────────────────────────────────────────────
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "🎓 Welcome to the SJBIT Q&A API!",
        "status": "running",
        "how_to_use": {
            "method": "POST",
            "endpoint": "/ask",
            "body_format": {
                "question": "Type your SJBIT-related question here"
            }
        },
        "example_questions": [
            "What courses does SJBIT offer?",
            "How do I get admission to SJBIT?",
            "Does SJBIT have a hostel?",
            "What companies recruit from SJBIT?"
        ]
    })


# ── ROUTE 2: Ask Question ─────────────────────────────────────────────────────
@app.route("/ask", methods=["POST"])
def ask_question():

    # Get JSON data from request
    data = request.get_json()

    # Check if data was sent
    if not data:
        return jsonify({
            "error": "No data received. Please send a JSON body.",
            "example": {"question": "What courses does SJBIT offer?"},
            "status": "error"
        }), 400

    # Check if question field exists
    if "question" not in data:
        return jsonify({
            "error": "Missing 'question' field.",
            "example": {"question": "What courses does SJBIT offer?"},
            "status": "error"
        }), 400

    # Get and clean the question
    user_question = data["question"].strip()

    # Check question is not empty
    if not user_question:
        return jsonify({
            "error": "Question cannot be empty.",
            "status": "error"
        }), 400

    # Build the SJBIT prompt
    full_prompt = build_sjbit_prompt(user_question)

    # Send to Groq AI and get response
    try:
        print(f"\n📩 Question received: {user_question}")

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # Free model on Groq
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )

        # Extract the answer
        answer = response.choices[0].message.content

        print(f"✅ Answer generated successfully")

        return jsonify({
            "question": user_question,
            "answer": answer,
            "status": "success"
        }), 200

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({
            "error": f"Something went wrong: {str(e)}",
            "status": "error"
        }), 500


# ── ROUTE 3: Help for GET on /ask ─────────────────────────────────────────────
@app.route("/ask", methods=["GET"])
def ask_help():
    return jsonify({
        "message": "This endpoint only accepts POST requests.",
        "correct_usage": {
            "method": "POST",
            "content_type": "application/json",
            "body": {"question": "Your question about SJBIT"}
        }
    })


# ── Run Server ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 Starting SJBIT Q&A API...")
    print("📍 Visit http://127.0.0.1:5000 to see if it's running")
    print("📮 Send POST requests to http://127.0.0.1:5000/ask")
    print("⏹️  Press CTRL+C to stop the server\n")
    app.run(debug=True, port=5000)