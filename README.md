# 🎯 Customer Loan Profile Analyzer
## 📌 What Is This Project?
This tool analyzes customer data and tells bank staff exactly which loan products to offer to each customer. Instead of guessing, you get data-driven recommendations in seconds.

One line summary: _Enter customer details_ → _Get segment_ → _Receive loan recommendations_

---
## 🎯 The Goal
| Goal |	Explanation |
| :--: | :----------: |
| Sell more loans |	Target customers who are likely to accept and afford loans |
| Reduce risk |	Avoid offering loans to customers who might default |
| Save time |	Stop guessing - know instantly what to offer |
| Improve customer | experience	Give relevant offers, not spam |

---
## 🧠 How It Works

### Step 1: Enter Customer Information
You provide  pieces of information about the customer:
| Field | What It Means |
| :---- | :----------: |
| Age |	How old is the customer |
| Occupation |	What job they do |
| Marital Status |	Single, married, or divorced |
| Credit Default History |	Have they ever missed payments? |
| Account Balance |	How much money they have in their account |
| Housing Loan |	Do they already have a mortgage? |
| Personal Loan |	Do they already have another loan? |
| Campaign Contacts |	How many times have we called them |
| Call Duration |	How long did they talk last time |
| Previous Contacts |	Were they contacted before this campaign|

### Step 2: Tool Analyzes the Data
The tool compares this customer against patterns learned from thousands of previous customers.

### Step 3: Get Recommendations
The customer is placed into one of 4 segments with specific loan recommendations.

### 📊 The 4 Customer Segments
| Segment |	Name |	Who They Are |	What To Offer |
| :------ | :--- | :-----------: | :------------: |
| 0 |	High-Value Professionals |	High balance, no existing loans, good credit |	Personal loans, credit cards, premium lines |
| 1 |	At-Risk | Customers	Negative balance, existing loans, has defaults |	Financial counseling, debt consolidation (NO new loans) |
| 2 |	Homeowners |	Has mortgage, good balance, good payment history |	Home equity loans, home improvement loans |
| 3 |	Personal Loan Holders |	Has personal loan, moderate balance, clean credit |	Debt consolidation, refinancing |

---
## 🖥️ How to Use the App
### Step-by-Step
**1. Open the app**
• Run streamlit run bank.py in your terminal

**2. Fill in customer information**
•Enter age, balance, etc.

• Select job,marital status from dropdowns

• Choose Yes/No for loan questions

**3. Click "Predict Segment" button**
**4. Read the results**
• See which segment the customer belongs to

• Read the recommended loan products

• Check the risk level
**5. Take action**
• Offer the recommended products to the customer

• Or provide financial counseling if in at-risk segment

---
## 💻 How to Run the App Locally
### 1️⃣ Clone the Repository
**Open your terminal (Command Prompt, PowerShell, or Terminal) and run the following commands:**
```git clone https://github.com/Olamilekan-23-ML/Loan_Segmentation.git```

 ```cd Loan_Segmentation```
### 2️⃣ Install Dependencies
**Ensure you have Python installed, then run:**
```pip install -r requirements.txt```
### 3️⃣ Run the Streamlit App
**Start the application with the following command:**
``streamlit run loan.py``

_Then open the URL shown in your terminal (usually http://localhost:8501) in your web browser._

---
## 📂 Project Structure
| File | Description |
| :--- | :--- |
| `loan.py` | Streamlit web application |
| `loan_analysis.ipynb` |Jupyter notebook for training the model |
| `loan_data.csv` | Original dataset (11,162 customers) |
| `kmeans.pkl` |Trained KMeans model |
| `scaler.pkl` | Feature scaling model |
| `encoders.pkl` | Encoders for categorical data |
| `requirements.txt` | List of Python dependencies required to run the app. |
| `README.md` | This file. |

---
🧰 Technologies Used

• Python

• Streamlit

• Scikit-learn

• NumPy & Pandas

• Pickle

---
## 📊 Data Source
• Original data: Bank marketing dataset (UCI repository)

• Records: 11,162 customers

• Features: 17 columns (demographics, financial, campaign data)

---
## 🔧 Technical Details
Machine Learning Method
| Component |	Details |
| :-------- | :------ |
| Algorithm |	K-Means Clustering |
| Number of Clusters |	4 (determined by elbow method) |
| Features Used |	10 (age, job, marital, default, balance, housing, loan, campaign, duration, previous) |
| Scaling |	StandardScaler |
| Categorical Encoding |	LabelEncoder |

**Why 4 Clusters?**
The elbow method showed that 4 clusters provide the best balance between:

• Within-cluster similarity (customers in same segment are similar)

• Between-cluster difference (different segments are distinct)

---
## 🤝 Contributing
1. Contributions are welcome! Please:
2. Fork the repository
3. Create a feature branch
4. Make your changes
5. Submit a pull request

---
## 📄 License
This project is for educational and portfolio purposes.

---
## 📧 Contact
For questions or suggestions about this project, please open an issue in the repository.

---
🙏 Acknowledgments
• Dataset source: Bank Marketing dataset (UCI Machine Learning Repository)

• Built as part of a data science portfolio project

---
## 👤 Author
*_OLAMILEKAN_*

*_GitHub: @Olamilekan-23-ML_*

---

