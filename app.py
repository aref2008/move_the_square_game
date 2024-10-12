from flask import Flask, render_template, request, jsonify
import random
import spacy

app = Flask(__name__)

# Initialize NLP
nlp = spacy.load("en_core_web_sm")

# Character state
state = {
    "x": 250,
    "y": 250,
    "color": "rgba(128, 0, 128, 0.3)",
    "shape": "circle", 
}

# Box boundaries
BOUNDARY = {"width": 500, "height": 500, "border": 10, "velocity": 20}

# Available colors
COLORS = [
    "rgba(255, 0, 0, 0.3)",    # Red with 30% opacity
    "rgba(0, 255, 0, 0.3)",    # Green with 30% opacity
    "rgba(0, 0, 255, 0.3)",    # Blue with 30% opacity
    "rgba(255, 255, 0, 0.3)",  # Yellow with 30% opacity
    "rgba(128, 0, 128, 0.3)"   # Purple with 30% opacity
]

# Available shapes
SHAPES = ["circle", "square", "pentagon", "hexagon"]

# Commands processing
def process_command(text):
    doc = nlp(text.lower())
    global state

    # Move commands
    if "move" in text:
        if "left" in text:
            new_x = max(state["x"] - BOUNDARY["velocity"], BOUNDARY["border"])
            state["x"] = new_x
        elif "right" in text:
            new_x = min(state["x"] + BOUNDARY["velocity"], BOUNDARY["width"] - BOUNDARY["border"] - 50)  # Adjusted boundary
            state["x"] = new_x
        elif "up" in text:
            new_y = max(state["y"] - BOUNDARY["velocity"], BOUNDARY["border"])
            state["y"] = new_y
        elif "down" in text:
            new_y = min(state["y"] + BOUNDARY["velocity"], BOUNDARY["height"] - BOUNDARY["border"] - 50)  # Adjusted boundary
            state["y"] = new_y

    # Change color command
    elif "change" in text and "color" in text:
        state["color"] = random.choice(COLORS)

    # Change shape command
    elif "change" in text and "shape" in text:
        state["shape"] = random.choice(SHAPES)

    # Jump command (move to a random position within the box)
    elif "jump" in text:
        state["x"] = random.randint(BOUNDARY["border"], BOUNDARY["width"] - BOUNDARY["border"] - 50)
        state["y"] = random.randint(BOUNDARY["border"], BOUNDARY["height"] - BOUNDARY["border"] - 50)


# Flask routes
@app.route("/")
def index():
    return render_template("index.html", state=state, colors=COLORS)

@app.route("/command", methods=["POST"])
def command():
    command = request.form.get("command")
    process_command(command)
    return jsonify(state)

if __name__ == "__main__":
    app.run(debug=True)