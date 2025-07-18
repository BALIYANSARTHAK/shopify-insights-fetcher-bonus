# 🛍️ Shopify Store Insights-Fetcher Application

This project is built as part of a **GenAI Developer Internship Assignment**. It provides a robust solution to fetch, store, and display insights from Shopify stores using a Python-based FastAPI backend and MySQL for data persistence. A simple frontend dashboard allows users to view and interact with store data.

---

## ✅ Project Features

### 🔹 Mandatory Section
- **Shopify Store Insights Fetching** via public endpoints
- **FastAPI Backend** to serve the data
- **Endpoints available at `/docs`** for testing via Swagger UI
- **MySQL Database** for persistent storage

### 🔸 Bonus Section
- 🧠 **Competitor Analysis** based on metrics like product count, popularity, and descriptions
- 📊 **Frontend Dashboard** to visualize and interact with the insights
- 🗃️ **MySQL Integration** for storing multiple store datasets

---

## 🛠 Tech Stack

| Component       | Technology         |
|----------------|--------------------|
| Backend         | FastAPI             |
| Language        | Python              |
| Database        | MySQL               |
| Frontend        | HTML/CSS + JavaScript |
| Testing         | Swagger UI (`/docs`) |
| Deployment Ready | ✅ Local / Postman / Docker Support |

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BALIYANSARTHAK/shopify-insights-fetcher-bonus.git
cd shopify-insights-fetcher-bonus
```

### 2️⃣ Set Up MySQL

- Create database:
```sql
CREATE DATABASE shopify_insights;
```

- Update `backend/db.py` or `.env` with your MySQL credentials.

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Backend Server
```bash
uvicorn main:app --reload
```

### 5️⃣ Access API Docs
Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📁 Project Structure

```
/shopify-insights-fetcher-bonus
├── backend/
│   ├── main.py
│   ├── db.py
│   └── routers/
├── frontend/
│   └── index.html
├── data/
├── models/
├── requirements.txt
├── README.md
└── final_report.pdf
```


## 🙌 Acknowledgements

This project was developed as part of a **GenAI Developer Internship Assignment**.

---

## 📫 Contact

**Sarthak Baliyan**  
📍 Roorkee, India  
📧 2003baliyansarthak@gmail.com

---

⭐ Don’t forget to **star** this repo if you found it helpful!
