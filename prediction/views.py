# prediction/views.py

from django.shortcuts import render
import joblib
import numpy as np
import pandas as pd

# Load the trained model
try:
    model = joblib.load('prediction/saved_models/ckd_model.joblib')
    print("Model loaded successfully.")
except FileNotFoundError:
    print("Model file not found. Ensure 'ckd_model.joblib' is in 'prediction/saved_models/'.")
    model = None

# These are the feature names your model was trained on
TRAINING_COLUMNS = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']

def predict_page(request):
    context = {}  # Context to pass to the template

    if request.method == 'POST':
        # Pass submitted form values back to the template to repopulate fields
        context['form_values'] = request.POST

        try:
            # Collect input data in the correct order
            input_data = [float(request.POST[col]) for col in TRAINING_COLUMNS]
            input_df = pd.DataFrame([input_data], columns=TRAINING_COLUMNS)
            
            if model:
                prediction = model.predict(input_df)
                
                # Check the prediction and build the detailed context
                # NOTE: Based on your code, prediction '0' means High Probability.
                if prediction[0] == 0:
                    context['result'] = "High Probability of CKD"
                    context['recommendations_title'] = "Important Next Steps and Recommendations"
                    context['recommendations'] = [
                        ("user-md", "<strong>Consult a Doctor Immediately:</strong> Schedule an appointment with a nephrologist (kidney specialist) for a comprehensive evaluation."),
                        ("pills", "<strong>Medication Management:</strong> A doctor may prescribe medications to control blood pressure and manage other related conditions."),
                        ("apple-alt", "<strong>Specialized Diet:</strong> You will likely need to follow a kidney-friendly diet, which may involve limiting protein, phosphorus, and potassium. A registered dietitian can help."),
                        ("tint", "<strong>Fluid Management:</strong> Your doctor will advise if you need to limit or increase your fluid intake based on your condition."),
                        ("heartbeat", "<strong>Control Blood Pressure & Diabetes:</strong> Strict management of high blood pressure and diabetes is essential to slow down kidney damage."),
                        ("vial", "<strong>Regular Monitoring:</strong> Expect regular blood and urine tests to monitor your kidney function.")
                    ]
                else: # This handles the 'Low Probability' case
                    context['result'] = "Low Probability of CKD"
                    context['recommendations_title'] = "General Recommendations for Kidney Health"
                    context['recommendations'] = [
                        ("balance-scale", "<strong>Balanced Diet:</strong> Eat a diet rich in fruits, vegetables, and whole grains. Reduce salt intake."),
                        ("running", "<strong>Regular Exercise:</strong> Aim for at least 150 minutes of moderate-intensity exercise per week."),
                        ("smoking-ban", "<strong>Avoid Smoking:</strong> Smoking can damage blood vessels and reduce blood flow to the kidneys."),
                        ("glass-whiskey", "<strong>Limit Alcohol:</strong> Adhere to recommended guidelines for alcohol consumption."),
                        ("pills", "<strong>Use Caution with NSAIDs:</strong> Avoid frequent use of over-the-counter anti-inflammatory drugs (NSAIDs) like ibuprofen."),
                        ("calendar-check", "<strong>Regular Check-ups:</strong> Continue with regular health check-ups to monitor your blood pressure and overall health.")
                    ]
            else:
                context['error_message'] = "Model is not available. Please contact the site administrator."
                
        except (ValueError, KeyError) as e:
            # Provide a more user-friendly error for missing or incorrect fields
            context['error_message'] = f'Invalid or missing input for "{e.args[0]}". Please ensure all fields are filled with valid numbers.'
        except Exception as e:
            # Catch any other unexpected errors
            context['error_message'] = f'An unexpected error occurred: {e}'

    # Always render the same page. The context will have results or errors after a POST.
    return render(request, 'prediction/predict.html', context)