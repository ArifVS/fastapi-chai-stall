# /// Aim of This API
# The main aim of this API is to:
# 
# ✅ Display the Chai Menu – Users can view available tea options.
# ✅ Take Orders for Specific Chai Types – Users can place an order for their preferred tea.
# ✅ Handle Errors Gracefully – If the user orders a tea that’s not on the menu, it shows a friendly error message.

from fastapi import FastAPI #importing FastAPI framework
app = FastAPI() # Creating Object app fro FastAPI

chai_menu = {
    "ginger_chai":"Strong ginger-flavored tea",
    "masala_chai":"Spicy and flavorful masala tea",
    "plain_chai":"Simple and classic tea"
}

#Home Route
@app.get("/")
def home():
    return {"Message": "Welcome to Arif's Cahi Stall! ☕"}


@app.get("/order/{chai_type}") # @app.get("/<route_name>/{parameter}") basic syntax
def order_chai(chai_type: str):
    if chai_type in chai_menu:
        return {"Order": chai_type, "description":chai_menu[chai_type] ,"Status": " Order Confirmed ✅"}
    else:
        return {"error": "This tea is not available on the menu! 😅"}
    
@app.get("/menu")
def get_menu():
    return {"Chai Menu": chai_menu}

