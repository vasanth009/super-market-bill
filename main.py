import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Sample item list with prices (in INR)
items = {
    "Apples": 120, "Bananas": 50, "Oranges": 80, "Grapes": 100, 
    "Strawberries": 200, "Blueberries": 300, "Lemons": 10, "Limes": 5,
    "Carrots": 40, "Broccoli": 150, "Spinach": 30, "Lettuce": 40,
    "Tomatoes": 30, "Onions": 25, "Potatoes": 20, "Bell Peppers": 50, 
    "Cucumbers": 20, "Parsley": 30, "Cilantro": 20, "Basil": 40, 
    "Mint": 20, "Rosemary": 50, "Milk": 60, "Cheese": 400, 
    "Yogurt": 40, "Butter": 50, "Eggs": 60, "Chicken Breast": 250, 
    "Ground Beef": 500, "Pork Chops": 450, "Bacon": 700, "Salmon": 1500, 
    "Shrimp": 800, "Tuna": 600, "Cod": 500, "Bread": 40, "Bagels": 30, 
    "Croissants": 40, "Muffins": 50, "Cookies": 200, "Cakes": 500, 
    "Frozen Vegetables": 100, "Frozen Fruits": 200, "Ice Cream": 150, 
    "Frozen Pizza": 300, "Frozen Fish Fillets": 400, "Beans": 50, 
    "Soup": 100, "Canned Vegetables": 50, "Canned Fruits": 100, 
    "Pasta Sauce": 150, "Salsa": 150, "Pasta": 50, "Rice": 60, 
    "Lentils": 80, "Quinoa": 300, "Flour": 40, "Sugar": 40, 
    "Chips": 30, "Crackers": 50, "Nuts": 800, "Candy": 10, 
    "Cookies": 100, "Popcorn": 50, "Water": 20, "Soda": 40, 
    "Juice": 120, "Coffee": 400, "Tea": 150, "Beer": 150, 
    "Wine": 700, "Spirits": 1200, "Ketchup": 100, "Mustard": 60, 
    "Mayonnaise": 150, "Salad Dressings": 150, "Olive Oil": 500, 
    "Vinegar": 50, "Salt": 20, "Pepper": 150, "Paprika": 200, 
    "Cumin": 150, "Cinnamon": 200, "Shampoo": 150, "Conditioner": 150, 
    "Soap": 100, "Toothpaste": 100, "Deodorant": 200
}

def send_email(to_address, subject, body):
    from_address = "your_mail@gmail.com"
    password = "your_app_password"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

def get_item_price(item_name):
    return items.get(item_name, None)

def print_bill(bill):
    print("\n--- YOUR BILL ---")
    print(f"Date & Time: {datetime.datetime.now()}")
    print("{:<20} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    total = 0
    bill_details = ""
    for item, (quantity, price) in bill.items():
        item_total = quantity * price
        total += item_total
        print("{:<20} {:<10} ₹{:,.2f}".format(item, quantity, item_total))
        bill_details += f"{item:<20} {quantity:<10} ₹{item_total:,.2f}\n"
    print(f"\nTotal Amount: ₹{total:,.2f}")
    print("-------------------------------")
    bill_details += f"\nTotal Amount: ₹{total:,.2f}\n"
    return bill_details

def main():
    bill = {}
    print("Welcome to the Market Hub!")
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for {item_name}: ").strip())
        price_per_unit = get_item_price(item_name)
        if price_per_unit is not None:
            bill[item_name] = (quantity, price_per_unit)
        else:
            print(f"Sorry, {item_name} is not available in the store.")

    if bill:
        bill_details = print_bill(bill)
        email = input("Enter your email address: ").strip()
        subject = "Your Supermarket Bill"
        body = f"--- YOUR BILL ---\nDate & Time: {datetime.datetime.now()}\n\n{bill_details}"
        send_email(email, subject, body)
        print("Receipt sent to your email.")
    else:
        print("No items in the bill. Exiting...")

if __name__ == "__main__":
    main()
