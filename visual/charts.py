import matplotlib.pyplot as plt
import pandas as pd

def show_chart(logs):
    if not logs:
        print("No data")
        return

    df = pd.DataFrame([log.to_dict() for log in logs])
    summary = df.groupby("name")["used"].sum()

    summary.plot(kind="bar")
    plt.show()