from flask import current_app as app
model_id = app.config["model_id"]
def predict(x):
    if model_id == "1":
        return "1"
    else:
        return "2"
