💳 Credit Card Fraud Detection System

📌 Overview

This project is a Machine Learning-based Credit Card Fraud Detection System.
It predicts whether a transaction is Fraud (1) or Normal (0) based on user behavior and transaction patterns.

---

🚀 Features

✔️ Detects fraudulent transactions in real-time
✔️ Uses multiple transaction-based features
✔️ Simple and efficient ML model
✔️ Easy to use and understand

---

📊 Input Features

The model takes the following inputs:

- distance_from_home → Distance between home and transaction location
- distance_from_last_transaction → Distance from previous transaction
- ratio_to_median_purchase_price → Purchase amount compared to usual spending
- repeat_retailer → (1 = Yes, 0 = No)
- used_chip → (1 = Yes, 0 = No)
- used_pin_number → (1 = Yes, 0 = No)
- online_order → (1 = Yes, 0 = No)

---

🧠 Model Output

- 0 → Normal Transaction ✅
- 1 → Fraud Transaction ❌

---

📥 Sample Inputs

✅ Normal Transaction

distance_from_home = 5
distance_from_last_transaction = 3
ratio_to_median_purchase_price = 1.2
repeat_retailer = 1
used_chip = 1
used_pin_number = 1
online_order = 0

👉 Output: 0 (Safe Transaction)

---

❌ Fraud Transaction

distance_from_home = 500
distance_from_last_transaction = 300
ratio_to_median_purchase_price = 8
repeat_retailer = 0
used_chip = 0
used_pin_number = 0
online_order = 1

👉 Output: 1 (Fraud Detected)

---

⚙️ Technologies Used

- Python 🐍
- Pandas
- NumPy
- Scikit-learn

---

▶️ How to Run

1. Clone the repository
2. Install dependencies
3. Run the model file
4. Provide input values
5. Get prediction output

---

🎯 Goal

The goal of this project is to prevent financial fraud by identifying suspicious transactions using machine learning.

---

📌 Future Improvements

🔹 Improve model accuracy
🔹 Add real-time API
🔹 Deploy as a web application

---

👨‍💻 Author

Your Name

---
