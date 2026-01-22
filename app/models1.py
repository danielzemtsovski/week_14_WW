import pandas as pd

def add_colums(data):
    df = pd.DataFrame(data)
    df["risk_level"] = pd.cut(df["range_km"],
            bins=[-1, 20, 100, 300, 10000],
            labels=["low", "medium", "high", "extreme"])
    return df


def replacing_None_to_Unknown(data):
    df = pd.DataFrame(data)
    df["manufacturer"] = df["manufacturer"].astype(object).fillna("Unknown")
    return df