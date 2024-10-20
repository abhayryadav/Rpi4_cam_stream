from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video/<path:filename>')
def video(filename):
    # Serve files from /home/a
    return send_from_directory('/home/a', filename)

if __name__ == '__main__':
    app.run(port=3000)
