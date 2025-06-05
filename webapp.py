import json
from flask import Flask, request, jsonify, render_template_string
import robin_stocks.robinhood as r

app = Flask(__name__)

FORM_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Robinhood Options Exporter</title>
  <style>
    body {
      margin: 0;
      font-family: Helvetica, Arial, sans-serif;
      background-color: #f5f5f5;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
    .card {
      background: #fff;
      padding: 40px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      width: 320px;
    }
    h1 {
      font-size: 24px;
      font-weight: 600;
      margin-top: 0;
      margin-bottom: 20px;
      color: #222;
    }
    label {
      font-size: 14px;
      color: #555;
    }
    input {
      width: 100%;
      padding: 8px;
      margin-top: 4px;
      margin-bottom: 12px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
    button {
      width: 100%;
      background: #00c806;
      color: white;
      border: none;
      padding: 10px 0;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background: #009b05;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Sign in</h1>
    <form method="post" action="/fetch">
      <label>Username</label>
      <input type="text" name="username" required>
      <label>Password</label>
      <input type="password" name="password" required>
      <label>2FA code (if enabled)</label>
      <input type="text" name="mfa" placeholder="123456">
      <button type="submit">Fetch Orders</button>
    </form>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(FORM_HTML)

@app.route("/fetch", methods=["POST"])
def fetch():
    username = request.form.get("username")
    password = request.form.get("password")
    mfa = request.form.get("mfa")
    if not username or not password:
        return "Missing credentials", 400
    r.login(username=username, password=password, mfa_code=mfa or None)
    orders = r.orders.get_all_option_orders()
    r.logout()
    return app.response_class(
        response=json.dumps(orders, indent=2),
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run(debug=True)
