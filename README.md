# 🧠 Chronic Kidney Disease (CKD) Predictor

A web application built using **Django** and **Scikit-learn** to predict the likelihood of Chronic Kidney Disease (CKD) from patient health metrics. Built for educational and prototyping purposes.

---

### 👤 Author

**Kiran Kumar**  
[GitHub Profile](https://github.com/kirankumarbarapati)

---

### ✨ Features

- **Web-Based Interface**: Clean and intuitive form for patient data entry  
- **Machine Learning Integration**: Predicts CKD in real time using a pre-trained model  
- **Data Preprocessing**: Complete pipeline from messy CSV to model-ready dataset  

---

### 🧰 Tech Stack

| Layer         | Technologies                            |
|---------------|------------------------------------------|
| Backend       | Django, Python                          |
| Machine Learning | Scikit-learn, Pandas, NumPy, Joblib   |
| Frontend      | HTML, CSS, JavaScript                   |
| Database      | SQLite                                  |

---

### ⚙️ Setup & Installation

#### 📦 Prerequisites
- Python ≥ 3.8  
- `pip`  
- `git`

#### 🔄 Clone & Configure
```bash
git clone https://github.com/kirankumarbarapati/CKD-Predictor.git
cd CKD-Predictor
```

#### 🧪 Create Virtual Environment
**Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 📥 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 🗃️ Run Migrations
```bash
python manage.py migrate
```

#### 🚀 Start the Server
```bash
python manage.py runserver
```

Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🧪 How to Use

1. Enter patient health metrics using the form  
2. Use dropdowns for categorical fields  
3. Click **Get Prediction**  
4. View results at the bottom of the page

---

### 📂 Project Notes

- **Dataset**: CKD dataset (400 rows, 25 features)  
- **Model**: `RandomForestClassifier` (Scikit-learn)  
- **File**: Saved to `prediction/saved_models/ckd_model.joblib`  
- **Note**: This is an educational tool — not for clinical use

---

### 📜 License

This project is licensed under the **MIT License**. You're free to use, modify, and distribute this code with proper attribution.  
See the [LICENSE](LICENSE) file for full details.

---
