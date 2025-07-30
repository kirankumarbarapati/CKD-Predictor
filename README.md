Chronic Kidney Disease (CKD) Predictor
A web application built with Django and Scikit-learn to predict the likelihood of a patient having Chronic Kidney Disease (CKD) based on various health metrics.
---------------------------------------------------------------------------------------+
Author: [Kiran Kumar]
---------------------------------------------------------------------------------------+

#Features :
Web-Based Interface: A clean and simple form to input patient data.
Machine Learning Integration: Uses a pre-trained model to provide real-time predictions.
Data Preprocessing: Demonstrates a full pipeline from a raw, messy CSV to a clean, model-ready dataset.
---------------------------------------------------------------------------------------+
#Tech Stack :
Backend: Django, Python
Machine Learning: Scikit-learn, Pandas, NumPy
Model Saving: Joblib
Frontend: HTML, CSS ,Js
---------------------------------------------------------------------------------------+

# Setup and Installation :

Follow these steps to get the project running on your local machine.

#Prerequisites
Python (version 3.8 or higher recommended)
pip (Python package installer)
git (for cloning the repository)

1. Clone the Repository
Open your terminal or command prompt and clone this repository:
Generated bash
git clone https://github.com/
cd your-repository-name
Use code with caution.
Bash

2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.
On Windows:
Generated bash
#--------------------------------------------------------#
python -m venv venv

.\venv\Scripts\activate
#--------------------------------------------------------#
Use code with caution.
Bash
On macOS / Linux:
Generated bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash

3. Install Required Packages
Install all the necessary Python packages using the requirements.txt file.
Generated bash
#--------------------------------------------------------#
pip install -r requirements.txt
#--------------------------------------------------------#
Use code with caution.
Bash

4. Run Django Migrations
This command sets up the initial database schema required by Django.
Generated bash
#--------------------------------------------------------#
python manage.py migrate
#--------------------------------------------------------#
Use code with caution.
Bash

5. Start the Development Server
You are now ready to run the application!
Generated bash
#--------------------------------------------------------#
python manage.py runserver
#---------------------------------------------------------#
Use code with caution.
Bash

The server will start, and you can access the application in your web browser.
---------------------------------------------------------------------------------------+
How to Use 
---------------------------------------------------------------------------------------+
Once the server is running, open your web browser and navigate to:

http://127.0.0.1:8000/
You will see a form with fields for various patient health metrics.
Fill in all the fields with numerical data. Use the dropdowns for categorical features.
Click the "Get Prediction" button.
The page will reload, and the prediction result will be displayed at the bottom.
Project Notes
Dataset: The model was trained on the Chronic Kidney Disease dataset, which contains 400 instances and 25 features. Data cleaning and imputation (filling missing values with the mean/mode) were performed before training.
Model: A RandomForestClassifier from Scikit-learn was used. It was saved to the file prediction/saved_models/ckd_model.joblib.
Disclaimer: This is an educational project and is not intended for real-world medical diagnosis. The predictions are based on a model and should not be used as a substitute for professional medical advice.

