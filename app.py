from flask import Flask, render_template, jsonify, request, session
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
Session(app)

user_data = {}

@app.route('/')
def index():
    user = session.get('user', {})
    return render_template('index.html', user=user)

@app.route('/update_clicks', methods=['POST'])
def update_clicks():
    if 'user' in session:
        user_id = session['user']['id']
        if user_id in user_data:
            user_data[user_id]['clicks'] += 1
            return jsonify({'clicks': user_data[user_id]['clicks']})
        else:
            return jsonify({'error': 'User data not found'}), 400
    return jsonify({'error': 'User not logged in'}), 400

@app.route('/login')
def login():
    user = {
        'id': '1',
        'name': 'CRYPTO DRELL',
        'avatar': 'https://example.com/avatar.jpg'
    }
    session['user'] = user
    user_data[user['id']] = {
        'name': user['name'],
        'avatar': user['avatar'],
        'clicks': 0
    }
    return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
