COIN=4383483
CREDIT=59852200

#1.96, 2.94(real)
COIN_FACTOR=2.94
#37.4/37.8(real)
TICKET_FACTOR=37.4

MONEY_SPEND=COIN/COIN_FACTOR
MONEY_GAIN=CREDIT/TICKET_FACTOR

MONEY_EARN=MONEY_GAIN-MONEY_SPEND

print("MONEY_EARN: "+str(MONEY_EARN))
print("Percentage: "+str(MONEY_EARN/MONEY_SPEND))
