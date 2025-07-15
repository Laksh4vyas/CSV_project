# 📊 CSV Analyzer — Smart Insights & Local Database Storage

A **powerful**, **elegant** web app built with **Streamlit** that lets you **upload, clean, filter, visualize**, and **analyze** CSV & JSON files — right in your browser!  
It even saves your upload history with a local **SQLite** database.  

---

## 🌐 **Live Demo**

👉 **Try it live here:**  
[**📂 CSV Analyzer on Streamlit Cloud 🚀**](https://csvproject-c2p4zaxcuwx2sjz268chcj.streamlit.app/)

---

## 🚀 **Key Features**

✨ **Upload** CSV or JSON files  
🔄 **Convert** JSON to CSV with download option  
👀 **Instant** data preview & summary  
🧹 **Smart** missing value handling (drop, fill with 0 or mean)  
🔍 **Filter**, **group**, & generate top-k frequency charts  
📊 **Beautiful** correlation heatmaps, pie charts, & custom plots  
🗃️ **Integrated SQLite DB** to store file metadata  
📚 **View upload history** (last 10 files)

---

## 🛠️ **Tech Stack**

- **Frontend:** Streamlit  
- **Backend & Logic:** Python, Pandas, NumPy, Seaborn, Matplotlib  
- **Database:** SQLite (via `sqlite3`)

---

## 📁 **Folder Structure**

📦 csv-analyzer-app/
├── app.py # Main Streamlit app
├── database.py # SQLite DB connection & table management
├── csv_analyzer.db # Auto-created local DB file
├── requirements.txt # Python dependencies
└── README.md # Project info

yaml
Copy
Edit

---

## ⚙️ **How to Run Locally**

1️⃣ **Clone this repo**
```bash
git clone https://github.com/your-username/csv-analyzer-app.git
cd csv-analyzer-app
2️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copy
Edit
pip install streamlit pandas numpy matplotlib seaborn
3️⃣ Run the app

bash
Copy
Edit
streamlit run app.py
Open in your browser: http://localhost:8501

💾 About the Database
Local SQLite DB: csv_analyzer.db

Auto-creates on first file upload

Stores:

Filename

Number of rows & columns

Upload timestamp

🗂️ Upcoming Features
🚧 Save filtered/cleaned datasets
🔐 User login for personal upload history
📤 Export reports as Excel or PDF
☁️ Cloud DB integration (MySQL/PostgreSQL)

🙌 Author
Made with ❤️ by Laksh Vyas
📧 lakshvyas462006@gmail.com

📜 License
This project is open-source under the MIT License — use it freely, learn from it, and improve it!

✅ Bonus: Example requirements.txt
nginx
Copy
Edit
streamlit
pandas
numpy
matplotlib
seaborn
