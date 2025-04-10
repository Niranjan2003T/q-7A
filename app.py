from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Niranjan"  # Replace with your full name
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n1 | head -15")

    return f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}

    Top Output:
    {top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
