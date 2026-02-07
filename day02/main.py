print("🍕 Willkommen beim Pizza-Kostenrechner! 🧮")

price = float(input("💰 Wie hoch ist der Gesamtpreis der Pizza? € "))
people = int(input("👥 Wie viele Personen teilen sich die Pizza? "))
service_fee = int(input("💸 Wie viel Prozent Trinkgeld? 5 10 15: "))

fee_percent = service_fee / 100
service_amount = price * fee_percent
total_price = price + service_amount
price_per_person = total_price / people
final_price = round(price_per_person, 2)

print(f"✅ Jede Person sollte zahlen: €{final_price}")
