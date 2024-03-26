from flask import Flask, render_template, request
import threading
import alice
import bob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/alice', methods=['POST'])
def alice_route():
    threading.Thread(target=alice.alice).start()
    return "Alice started!"

@app.route('/bob', methods=['POST'])
def bob_route():
    threading.Thread(target=bob.bob).start()
    return "Bob started!"

if __name__ == '__main__':
    app.run(debug=True)
