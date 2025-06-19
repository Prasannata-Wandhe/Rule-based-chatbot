from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import datetime
import requests
import re

app = Flask(__name__)
CORS(app)
name = None


def clean_city_name(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).strip()

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    def get_weather(city):
        API_KEY = "enter your api"  # Replace with your actual API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        
        city = clean_city_name(city)
        full_url = f"{base_url}?q={city}&appid={API_KEY}&units=metric"

        try:
            print(f"[DEBUG] Fetching: {full_url}")  
            response = requests.get(full_url)
            data = response.json()
            print(f"[DEBUG] Response JSON: {data}") 

            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                return f"The weather in {city.title()} is {desc} with {temp}°C temperature."
            else:
                return f"Sorry, I couldn't find that city. (Code: {data.get('cod')}, Message: {data.get('message')})"
        except Exception as e:
            return f"Sorry, there was an error getting weather info: {str(e)}"

    def basic_calculator():
        return "I can do math! Try asking me something like '2 + 2' or 'what is 5 * 3'?"

    if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
        return "Hello! How can I help you?"

    elif "my name is" in user_input:
        global name
        name = user_input.split("is")[-1].strip()
        return f"Nice to meet you, {name}!"

    elif any(word in user_input for word in ['how are you', 'how do you do', 'what\'s up']):
        return "I'm doing great, thank you for asking! How are you?"
    
    elif any(word in user_input for word in ['what is your name', 'your name', 'who are you']):
        return "I'm a simple chatbot created to help answer your questions!"

    elif any(word in user_input for word in ['weather', 'climate', 'temperature']):
        return "Please tell me the city name:"

    elif any(word in user_input for word in ['time', 'what time', 'clock']):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    
    elif any(word in user_input for word in ['date', 'what date', 'day']):
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."

    elif any(word in user_input for word in ['help', 'assist', 'support']):
        return "I can chat with you about basic topics like weather, date, time, your age and calculator. What would you like to know?"

    elif any(word in user_input for word in ['calculator', 'calc', 'calculate']):
        return basic_calculator()

    elif any(op in user_input for op in ['+', '-', '*', '/']):
        try:
            result = eval(user_input.replace('what is', '').replace('=', '').strip())
            return f"Result: {result}"
        except:
            return "Please enter a valid math expression like '2+2' or '5*3'."

    elif any(word in user_input for word in ['bye', 'goodbye', 'see you', 'farewell']):
        return "Goodbye! It was nice chatting with you. Have a great day!"
    
    elif any(word in user_input for word in ['thank you', 'thanks', 'appreciate']):
        return "You're welcome! I'm happy to help."

    # Handle single-word input as potential city name
    elif len(user_input.split()) <= 3 and user_input.isalpha():
        return get_weather(user_input)
    
    else:
        return "That's interesting! I'm still learning, so I might not understand everything. Can you tell me more or ask something else?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Please provide a message'}), 400
        
        bot_response = chatbot_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
