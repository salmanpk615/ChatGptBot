from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)


class ChatGPTBot:
    def __init__(self):
        openai.api_key = "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"  # your actual OpenAI API key

    def create_prompt(self):
        prompt = request.form['prompt']
        response = self.get_response(prompt)
        return jsonify({'response': response})

    def get_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,  # passing the user input
            max_tokens=1024,  # generated output can have 1024 number of tokens
            n=1,  # number of outputs generated in one call
            stop=None,
            temperature=0.5,  # The range of the sampling temperature is 0 to 2.
        )
        response = response.choices[0].text
        return response


chat_bot = ChatGPTBot()


@app.route("/", methods=['POST', 'GET'])
def create_prompt_and_get_response():
    if request.method == 'POST':
        chat_bot.create_prompt()
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
