import pandas as pd

data = {
    "Anlage": ["Sorter", "Förderband", "Sorter", "Shuttle", "Förderband"],
    "Stillstand_Minuten": [12, 5, 18, 0, 10],
    "Verarbeitete_Pakete": [120, 80, 95, 150, 70],
}

df = pd.DataFrame(data)

print("Logistikdaten:")
print(df)

print("\nGesamte Stillstandszeit:")
print(df["Stillstand_Minuten"].sum(), "Minuten")
print("\nStillstandszeit je Anlage:")
print(df.groupby("Anlage")["Stillstand_Minuten"].sum())
stillstand = df.groupby("Anlage")["Stillstand_Minuten"].sum()
anteil = stillstand / stillstand.sum() * 100

print("\nAnteil an der gesamten Stillstandszeit:")
print(anteil.round(1).astype(str) + " %")