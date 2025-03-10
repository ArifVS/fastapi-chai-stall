# fastapi-chai-stall
A simple FastAPI project that serves as a Chai Ordering API, allowing users to view the chai menu, place orders, and get confirmation messages.

# ☕ FastAPI Chai Stall API

This project is a simple FastAPI-based Chai Ordering API where users can view available chai types, place orders, and receive friendly responses.

## 📋 Features
✅ Display the Chai Menu  
✅ Place Orders for Specific Chai Types  
✅ Handle Errors Gracefully  

## 🔥 How to Run
1. Clone this repository:
2. Install dependencies:
3. Run the FastAPI server:


## 🌐 API Endpoints
| Method | Endpoint             | Description                          |
|---------|----------------------|--------------------------------------|
| `GET`    | `/`                   | Home Page - Welcome Message          |
| `GET`    | `/menu`               | Display Available Chai Types         |
| `GET`    | `/order/{chai_type}`  | Order a Specific Chai (e.g., `ginger_chai`) |

## 📄 Example Usage
1. **Home Route:** `http://localhost:8000/`  
2. **Menu Route:** `http://localhost:8000/menu`  
3. **Order Example:** `http://localhost:8000/order/ginger_chai` or  `http://localhost:8000/docs`

## 🛠️ Tech Stack
- FastAPI  
- Python  
- Uvicorn  

## ✨ Author
Developed by Velloresyed Arifulla 


