# Rule-based-chatbot-codesofttask1-
Build a simple chatbot that responds to user inputs based on  predefined rules. Use if-else statements or pattern matching  techniques to identify user queries and provide appropriate  responses.
🧠 Rule based Chatbot 🤖
A beginner-friendly chatbot built with Flask and  JavaScript, capable of answering common questions related to:

🕐 Time & 📅 Date

🌦️ Weather (via OpenWeatherMap API)

🧮 Simple Calculations

📌 Casual Conversations

✨ Features
✅ Conversational chatbot interface

🌍 Real-time weather info using city names

🧠 Responds to greetings, thank you, and farewells

🔢 Evaluates basic math expressions

📅 Tells current time and date

🎨 Simple and clean frontend using HTML/CSS



ma
📁 Project Structure
php
Copy code
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend page
            
├── README.md            # Project readme



⚙️ How to Run
1. Clone the Repo

2. Set up Environment 
bash
Copy code
python -m venv env
source env/bin/activate   # or env\\Scripts\\activate on Windows
3. Install Dependencies
bash
Copy code
pip install flask requests flask-cors
<br>

5. Add Your API Key 🔑
Edit app.py and replace:

python
Copy code
API_KEY = "your_actual_api_key"
with your OpenWeatherMap API key.

5. Run the App
bash
Copy code
python app.py
Then open http://localhost:5000 in your browser!

📦 Example Chat
text
Copy code
You: Hi
Bot: Hello! How can I help you?

You: What's the weather?
Bot: Please tell me the city name:

You: Mumbai
Bot: The weather in Mumbai is clear with 31°C temperature.

🙌 Author
Prasannata Wandhe












