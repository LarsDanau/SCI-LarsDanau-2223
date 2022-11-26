#Functie voor het berekenen van een  cash flow (CF)
def calculate_cash_flow():
    pass

# Functie voor het berekenen van een future value (FV) zonder payment
def calculate_future_value(present_value, period_rate, number_of_periods):
    return present_value*(1 + period_rate)**number_of_periods


# Functie voor het berekenen van een future value (FV) met payment
# De when staat voor wanneer de payment ter beschikking wordt gesteld, 'end' = 0, 'begin' = 1, default is 'end
def calculate_future_value_with_payment(present_value, period_rate, number_of_periods, payment, when='end'):
    payment_rate = 0
    if when == 'begin':
        payment_rate = 1
    else:
        payment_rate = 0

    return present_value*(1 + period_rate)**number_of_periods + payment*(1 + period_rate * payment_rate)/ period_rate*((1 + period_rate)**number_of_periods -1)

def calculate_net_present_value(rate, cashflows):
    net_present_value = cashflows[0]
    
    for i in range(1, len(cashflows)):
        net_present_value += cashflows[i]/(1 + rate)**i

    return net_present_value


# Functie voor het berekenen van de internal rate of return (IRR) met een gegeven cashflow (array)
def calculate_internal_rate_of_return(cashflows):
    pass

# Testen van alle functies
print(calculate_future_value(100, 0.1, 2))

print(calculate_future_value_with_payment(0, 0.1, 2, 100))

print(calculate_net_present_value(0.112, [-100,50,60,70,100,20]))
