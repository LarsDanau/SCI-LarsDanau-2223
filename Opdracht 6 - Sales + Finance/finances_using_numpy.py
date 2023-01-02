# Importeren van NumPy Financial
import numpy_financial as npf

# Cashflows (CF)
# Initiele investering van €100, Erna krijgen we er €50, €60, €70, €100 en €20 uit terug.
cashflows = [-100, 50, 60, 70, 100, 20]

# Interest Rate (I)
# We willen een lening afbetalen van €1700, Hiervoor maken we 10 maandelijkse betalingen van €180; de interest rate zal hiervoor 1,05% zijn
print(f"Interest Rate: {npf.rate(10, -180, 1700, 0) * 100}")

# Internal Rate of Return (IRR)
# De Internal Rate Of Return (IRR) wordt gedefinieerd als de disconteringsvoet waarbij de NPV gelijk is aan nul.
# Er is dus een discount rate nodig van 0.200 om de NPV waarde 0 te maken
cashflows = [-100, 30, 40, 40, 50]
print(f"Internal Rate of Return: {npf.irr(cashflows)}")

# Net Present Value (NPV)
# NPV Van 121.55, positief getal! Het project is het waard om te ondernemen
rate = 0.112
cashflows = [-100, 50, 60, 70, 100, 20]
print(f"Net Present Value: {npf.npv(rate, cashflows)}")

# Future Value (FV)
# Berekenen van de future value
# De future value van -100€ na 10 jaar, met maandelijks €100 te sparen op een jaarlijkse interest rate van 5% ==> 15692.93
print(f"Future value: {npf.fv(0.05/12, 10*12, -100, -100)}")

# Present Value (PV)
# Berekenen van de present value
# Future Value van 500, een jaarlijkse betaling van 40 euro aan een interest rate van 5%, zorgt ervoor dat we een present value hebben van -170.08
print(f"Present Value: {npf.pv(0.05, 6, -40, 500)}")
