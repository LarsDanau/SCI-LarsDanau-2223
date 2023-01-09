# Importeren van NumPy Financial
import numpy_financial as npf

# Cashflows (CF) = Aantal geld dat in en uit een bedrijf wordt gebracht
# Inputs en Outputs
# Beschrijft gebruik van cash over een bepaalde periode en de mogelijke resources van het bedrijf
# Initiele investering van €100. Vervolgens wordt er €50, €60, €70, €100 en €20 uit terug.
cashflows = [-100, 50, 60, 70, 100, 20]


# Interest Rate (I) = De vergoeding bovenop een af te betalen kapitaal van een lening dat betaald moet worden
# Rentetarief kan ook een verdiend bedrag zijn bij een bank.
# Interest kan voorkomen als: enkelvoudig of samengesteld

# Stel je wilt in 40 jaar op pensioen gaan met een bedrag van 1.700.000,00€, Hiervoor investeer je maandelijks 1300€, Hoeveel bedraagt het jaarlijkse nodige rentebedrag?
# Antoord: 4,40%
print(f"Interest Rate: { 12 * npf.rate(40*12, -1300, 0, 1700000)}")


# Internal Rate of Return (IRR)
# De Internal Rate Of Return (IRR) wordt gedefinieerd als de disconteringsvoet waarbij de NPV gelijk is aan nul.
# Interne rentabiliteit (NL) is een rendement dat bedrijven verwachten op een investering die ze kunnen doen. Hiermee wordt de winstgevendheid van investering gemeten.
# Antwoord: Er is dus een discount rate nodig van 20% om de NPV waarde 0 te maken
cashflows = [-100, 30, 40, 40, 50]
print(f"Internal Rate of Return: {npf.irr(cashflows)}")


# Net Present Value (NPV) / Netto Contante Waarde (NCW)= Wordt gebruik om te kijken of een project/investering genoeg winst op zal leveren. Er wordt gekeken naar toekomstige cashflows.
# Een positieve NPV = Waard om te ondernemen
# NPV Van 121.55, positief getal! Het project is het waard om te ondernemen
rate = 0.112
cashflows = [-100, 50, 60, 70, 100, 20]
print(f"Net Present Value: {npf.npv(rate, cashflows)}")


# Future Value (FV)
# Berekenen van de toekomstige waarde. Hiermee kunnen we berekenen hoe het geld dat we momenteel beschikken zal veranderen.
# De toekomstige waarde van een investering van 2000€ op dit moment, na 20 jaar aan een rente van 9% zou 11208€ waard zijn!
print(f"Future value: {npf.fv(0.09, 20, 0, -2000)}")


# Present Value (PV)
# Berekenen van de huidige waarde
# Wat is de huidige waarde van een investering dat zou uitkomen op 10.000€ na 15 jaar op een inflatie van 3% per jaar.
# Antwoord: 6418,62€
print(f"Present Value: {npf.pv(0.03, 15, 0, 10000)}")
