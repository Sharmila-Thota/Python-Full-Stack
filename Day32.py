#Create a Series
import pandas as pd
prices = pd.Series([2999, 15999, 52999, 4999])
print(prices)
#Create a DataFrame
import pandas as pd
data = {
    "Product": ["Laptop", "Phone", "Watch"],
    "Price": [50000, 20000, 5000],
    "Stock": [10, 20, 30]
}
df = pd.DataFrame(data)
print(df)
#Check shape, columns, and index
print(df.shape)
print(df.columns)
print(df.index)
#Select one column
print(df["Product"])
#Handle missing values
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Salary": [30000, None, 40000]
})
print(df.dropna())
print(df.fillna(0))
#groupby()
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 40000, 45000]
})
print(df.groupby("Department")["Salary"].mean())