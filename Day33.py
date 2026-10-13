#Pie Chart
import matplotlib.pyplot as plt
companies = ["A", "B", "C", "D"]
market_share = [40, 30, 20, 10]
plt.pie(market_share, labels=companies, autopct="%1.1f%%")
plt.title("Market Share")
plt.show()