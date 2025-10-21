from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
import traceback
from src.mowingEstimator.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET'])
def home_page():
    """Route to display the home page."""
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def training():
    """Route to trigger model training."""
    try:
        os.system("python main.py")
        return "✅ Training Successful!"
    except Exception as e:
        return f"❌ Training failed: {e}"


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            area = request.form.get('area')
            if not area:
                return render_template('index.html', error="Please enter an area value.")
            
            area = float(area)

            # ✅ match feature name exactly as used during model training
            data = pd.DataFrame({'Area': [area]})

            predictor = PredictionPipeline()
            prediction = predictor.predict(data)

            return render_template('results.html', prediction=str(prediction))

        except Exception as e:
            print("Exception occurred:\n", traceback.format_exc())
            return render_template('index.html', error=f"Something went wrong: {e}")
    
  



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
