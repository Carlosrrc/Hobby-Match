from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personality-test', methods=['GET', 'POST'])
def personality_test():
    if request.method == 'POST':
        # Process personality test data
        preferences = request.form.get('preferences')
        return f"You selected: {preferences}"
    return render_template('personality_test.html')

@app.route('/interests', methods=['GET', 'POST'])
def interests():
    if request.method == 'POST':
        # Save interests to the database
        interests = request.form.getlist('interests')
        return f"Interests saved: {', '.join(interests)}"
    return render_template('interests.html')

if __name__ == '__main__':
    app.run(debug=True)
