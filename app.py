from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Replace 'your_api_key_here' with your actual OpenAI API key
openai.api_key = os.environ['api_key']

@app.route('/')
def home():
    # Renders the home page
    return render_template('index.html')


@app.route('/api/review', methods=['POST'])
def review_website():
    # Receives the website URL from the AJAX request
    data = request.json
    url = data['url']

    # Placeholder: Replace this with actual website analysis
    # The following scores are placeholders.
    scores = {'Design': 5, 'User Experience': 5, 'Functionality': 5}

    # Generate a review summary using OpenAI's chat model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # This model supports the chat endpoint
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Review the website at {url}."},
        ]
    )

    review_summary = response['choices'][0]['message']['content']

    # Returns the review summary as JSON
    return jsonify({'reviewSummary': review_summary})


if __name__ == '__main__':
    app.run(debug=True)

