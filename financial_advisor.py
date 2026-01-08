# Game : Financial advisor

print("👨‍💼 Game: Financial advisor")
print("=" * 60)
print("You are a financial advisor. Help your clients!")
print("=" * 60)

# CLIENT DATABASE 
clients = {
    "Ivan": {
        "age": 25,
        "income": 5000,
        "savings": 10000,
        "risk_profile": "agressive", 
        "goals": ["save for car", "invest in stocks"]
    },
    "Maria": {
        "age": 45,
        "income": 8000,
        "savings": 50000,
        "risk_profile": "moderate",
        "goals": ["pension savings", "children's education"]
    },
    "Aleksey": {
        "age": 60,
        "income": 6000,
        "savings": 200000,
        "risk_profile": "conservative",
        "goals": ["preserve capital", "receive dividends1"]
    }
}

# Functions to analyze clients
def analyze_client(client_name):
    """Analyzes a client and gives recommendations"""
    client = clients[client_name]
    
    print(f"\n CLIENT: {client_name}")
    print("-" * 40)
    print(f"Age: {client['age']} years")
    print(f"Income: {client['income']} $/month")
    print(f"Savings: {client['savings']} $")
    print(f"Risk profile: {client['risk_profile']}")
    print(f"Goals: {', '.join(client['goals'])}")
    
    # RECOMMENDATIONS
    print("\n RECOMMENDATIONS:")
    
    # Age factor
    if client['age'] < 30:
        print("  Young age - can take more risks")
        recommended_investment = "growth stocks (technology companies)"
    elif client['age'] < 50:
        print("   Middle age - balanced approach")
        recommended_investment = "mixed portfolio (stocks + bonds)"
    else:
        print("  Pre-retirement age - conservative investments")
        recommended_investment = "bonds, dividend stocks"
    
    # Profile search
    if client['risk_profile'] == "agressive":
        risk_multiplier = 0.7  
        print(" Aggressive profile - high-risk assets")
    elif client['risk_profile'] == "moderate":
        risk_multiplier = 0.5  
        print(" Moderate profile - balances risk ")
    else:
        risk_multiplier = 0.3  
        print("  Safe profile - capital preservation")
    
    # Calculate investment distibution
    safe_investment = client['savings'] * (1 - risk_multiplier)
    risky_investment = client['savings'] * risk_multiplier

    print(f"\n Capital:")
    print(f"  Safe investments: {safe_investment:.0f} $")
    print(f"  Risky investments: {risky_investment:.0f} $")
    print(f"  Recommended investment: {recommended_investment}")
    
    # Goals advice
    print(f"\n To achieve goals:")
    for goal in client['goals']:
        if "car" in goal.lower():
            print(f"  For '{goal}': save {client['income']*0.2:.0f} $/month")
        elif "pension" in goal.lower():
            print(f"  For '{goal}': invest in pension funds")
        elif "education" in goal.lower():
            print(f"  For '{goal}': use saving plans for education")
    
    return {
        "safe": safe_investment,
        "risky": risky_investment,
        "recommendation": recommended_investment
    }

def compare_clients(client1, client2):
    """Comares two clients"""
    print(f"\n Compare clients:")
    print(f"{client1} vs {client2}")
    print("=" * 40)
    
    data1 = clients[client1]
    data2 = clients[client2]
    
    print(f"\n{client1}:")
    print(f"  Age: {data1['age']}, Income: {data1['income']}, Savings: {data1['savings']}")
    
    print(f"\n{client2}:")
    print(f"  Age: {data2['age']}, Income: {data2['income']}, Savings: {data2['savings']}")
    
    # Who has more savings?
    if data1['savings'] > data2['savings']:
        print(f"\n {client1} have more savings")
    else:
        print(f"\n {client2} have more savings")
    
    # Who younger?
    if data1['age'] < data2['age']:
        print(f" {client1} younger, can take more risks")
    else:
        print(f" {client2} younger, can take more risks")

# Game cycle
print("\n Your clients:")
for client in clients.keys():
    print(f"  - {client}")

while True:
    print("\n" + "=" * 60)
    print(" Choose what to do::")
    print("1. Analyze a client")
    print("2. Compare two clients")
    print("3. Finish game")

    choice = input("\n Your choice (1-3): ")

    if choice == "1":
        client_name = input("Name of client (Ivan/Maria/Aleksey): ")
        if client_name in clients:
            analyze_client(client_name)
        else:
            print(" Client not found!")
    
    elif choice == "2":
        client1 = input("First client: ")
        client2 = input("Second client: ")
        if client1 in clients and client2 in clients:
            compare_clients(client1, client2)
        else:
            print(" Client not found!")
    
    elif choice == "3":
        print("\n Goodbye!")
        break
    
    else:
        print(" Wrong choice!")

print("\n" + "=" * 60)
print(" Game over!")