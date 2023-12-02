# main
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request, url_for, redirect
import openai

load_dotenv()
app = Flask(__name__)
openai.api_key = os.getenv("API_TOKEN")


@app.route("/")
def index():
    """Returns the index page"""
    return render_template("index.html")


def get_completion(prompt, model="gpt-3.5-turbo"):
    prompt_answer = f"""
    Perform the following actions: 
    1 - Look up the text and summary requirements below
    2 - Provide two foods based on the requirements from text
    3 - Answer questions in the formation part
    4 - For the `Food` part, we want the formation to be: 


    Return only the following format as the final response:
    Nutrition name: <nutrition name>
    Food: <foods separated by comma>

    ```{prompt}```
    """

    messages = [{"role": "user", "content": prompt_answer}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


@app.route("/result")
def result():
    # Get the result from the URL parameter
    result = request.args.get("result", "")
    print(result)
    return render_template("result.html", result=result)


@app.route("/predict", methods=["POST"])
def predict():
    """Handles the prediction request"""
    print(request.form)
    prompt = request.form.get("prompt")
    print(prompt)
    result = get_completion(prompt)

    # Redirect to the result page with the result as a parameter
    return redirect(url_for("result", result=result))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
