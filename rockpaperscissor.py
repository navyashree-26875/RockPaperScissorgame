from flask import Flask, render_template_string, request, session
import random

app = Flask(__name__)
app.secret_key = "rockpaperscissors"

choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Rock Paper Scissors</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            font-family:Arial, sans-serif;
            background:linear-gradient(135deg,#4facfe,#00f2fe);
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            padding:20px;
        }

        .container{
            width:100%;
            max-width:650px;
            background:rgba(255,255,255,0.15);
            backdrop-filter:blur(15px);
            border-radius:20px;
            padding:30px;
            text-align:center;
            color:white;
            box-shadow:0 10px 30px rgba(0,0,0,0.3);
        }

        h1{
            margin-bottom:25px;
            font-size:36px;
        }

        .buttons{
            display:flex;
            justify-content:center;
            flex-wrap:wrap;
            gap:15px;
        }

        button{
            padding:15px 25px;
            border:none;
            border-radius:12px;
            font-size:18px;
            cursor:pointer;
            transition:0.3s;
        }

        .play-btn{
            background:#ff9800;
            color:white;
        }

        .play-btn:hover{
            transform:translateY(-5px);
            background:#ff6f00;
        }

        .reset-btn{
            background:#e53935;
            color:white;
            margin-top:15px;
        }

        .reset-btn:hover{
            background:#c62828;
        }

        .choice{
            font-size:80px;
            margin:10px;
            animation:pop 0.4s ease;
        }

        @keyframes pop{
            from{
                transform:scale(0);
            }
            to{
                transform:scale(1);
            }
        }

        .result{
            margin-top:15px;
            font-size:28px;
            font-weight:bold;
        }

        .win{
            color:#00ff99;
        }

        .lose{
            color:#ff5252;
        }

        .tie{
            color:#ffe082;
        }

        .score{
            margin-top:20px;
            background:rgba(255,255,255,0.2);
            padding:15px;
            border-radius:10px;
            font-size:20px;
        }

        .history{
            margin-top:20px;
            text-align:left;
            background:rgba(255,255,255,0.15);
            padding:15px;
            border-radius:10px;
            max-height:150px;
            overflow-y:auto;
        }

        .history h3{
            margin-bottom:10px;
        }

        .history li{
            margin:5px 0;
        }

    </style>
</head>

<body>

<div class="container">

    <h1>🎮 Rock Paper Scissors 🎮</h1>

    <form method="POST">

        <div class="buttons">

            <button class="play-btn" name="choice" value="rock">
                🪨 Rock
            </button>

            <button class="play-btn" name="choice" value="paper">
                📄 Paper
            </button>

            <button class="play-btn" name="choice" value="scissors">
                ✂️ Scissors
            </button>

        </div>

    </form>

    <form method="POST">
        <button class="reset-btn" name="reset">
            🔄 Reset Score
        </button>
    </form>

    {% if user %}

        <hr style="margin:20px 0;">

        <h2>Your Choice</h2>
        <div class="choice">{{ user_emoji }}</div>

        <h2>Computer Choice</h2>
        <div class="choice">{{ computer_emoji }}</div>

        <div class="result {{ result_class }}">
            {{ result }}
        </div>

    {% endif %}

    <div class="score">

        🏆 Player : {{ player }} <br><br>

        💻 Computer : {{ computer }} <br><br>

        🤝 Tie : {{ tie }}

    </div>

    <div class="history">

        <h3>📜 Game History</h3>

        <ul>
            {% for item in history %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>

    </div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():

    if "player" not in session:
        session["player"] = 0
        session["computer"] = 0
        session["tie"] = 0
        session["history"] = []

    user = None
    user_emoji = ""
    computer_emoji = ""
    result = ""
    result_class = ""

    if request.method == "POST":

        if "reset" in request.form:
            session["player"] = 0
            session["computer"] = 0
            session["tie"] = 0
            session["history"] = []

        elif "choice" in request.form:

            user = request.form["choice"]
            computer = random.choice(list(choices.keys()))

            user_emoji = choices[user]
            computer_emoji = choices[computer]

            if user == computer:
                result = "🤝 It's a Tie!"
                result_class = "tie"
                session["tie"] += 1

            elif (
                (user == "rock" and computer == "scissors") or
                (user == "paper" and computer == "rock") or
                (user == "scissors" and computer == "paper")
            ):
                result = "🎉 You Win!"
                result_class = "win"
                session["player"] += 1

            else:
                result = "💻 Computer Wins!"
                result_class = "lose"
                session["computer"] += 1

            history = session["history"]
            history.insert(
                0,
                f"You: {choices[user]} | Computer: {choices[computer]} → {result}"
            )
            session["history"] = history[:10]

    return render_template_string(
        html,
        user=user,
        user_emoji=user_emoji,
        computer_emoji=computer_emoji,
        result=result,
        result_class=result_class,
        player=session["player"],
        computer=session["computer"],
        tie=session["tie"],
        history=session["history"]
    )

if __name__ == "__main__":
    app.run(debug=True)
