# 💰 Personal Expense Tracker (Python + MySQL)

## 📌 Overview

A command-line based personal expense tracker that stores and analyzes expenses using MySQL and visualizes data with Matplotlib.

## 🛠 Tech Stack

* Python
* MySQL
* Matplotlib

---

## ⚙️ Features

* Add expense
* View all expenses
* Categorize spending
* Data visualization (charts)

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker-python.git
cd expense-tracker-python
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup MySQL Database

Open MySQL Workbench and run:

```sql
CREATE DATABASE expense_tracker;
USE expense_tracker;

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    amount FLOAT NOT NULL,
    category VARCHAR(20),
    description TEXT,
    date date
);
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory and add:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=expense_tracker
```

---

### 5️⃣ Run the Application

```bash
python main.py
```

---

## ⚠️ Notes

* Do NOT share your `.env` file
* Make sure MySQL server is running

---

## 🚧 Future Improvements

* GUI version
* Authentication system
* Cloud database support
