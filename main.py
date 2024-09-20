import os
from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route('/', methods=["GET", 'POST'])
def index():
    if request.method == "POST":
        user_input = request.form.get("text_input", "")
        embedded_html = f"""
            <div>Your Input</div>
            <h2>{user_input}</h2>
        """
        return render_template("index.html", embedded_html=Markup(embedded_html))
    return render_template('index.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
