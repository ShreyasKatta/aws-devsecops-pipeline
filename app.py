from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head><title>Target App</title></head>
    <body>
        <h1>Target Application for DevSecOps Scan</h1>
        <form action='/search'>
            <input type='text' name='query' required>
            <input type='submit' value='Search'>
        </form>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/search')
def search():
    user_query = request.args.get('query', '')
    response_content = f"<h1>Search Results</h1><p>You searched for: {user_query}</p>"
    return render_template_string(response_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)