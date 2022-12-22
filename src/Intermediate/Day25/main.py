import pandas as pd

data = pd.read_csv("Squirrel-Data.csv")

cinnamon_counts = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_counts = len(data[data["Primary Fur Color"] == "Black"])
gray_counts = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Primary Fur Color": ["Cinnamon", "Black", "Gray", ],
    "counts": [cinnamon_counts, black_counts, gray_counts, ]
}

df = pd.DataFrame(data_dict)
df.to_csv("New_Squirrel.csv")
print(df)
