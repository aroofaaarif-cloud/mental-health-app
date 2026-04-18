from flask import Flask, render_template, request, redirect

app = Flask(__name__)

entries = []

@app.route('/')
def home():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    mood = request.form.get('mood')
    note = request.form.get('note')

    # Simple message
    if mood == "sad":
        message = "It's okay to feel sad. Take a deep breath—you'll get through this 🌙"
    elif mood == "happy":
        message = "That's amazing! Keep enjoying this moment 😊"
    elif mood == "angry":
        message = "Pause. Breathe. You are in control 🧘"
    else:
        message = "Stay balanced and take care 💙"

    entries.append({
        "mood": mood,
        "note": note,
        "message": message
    })

    return redirect('/')

if __name__ == '__main__':
    app.run()