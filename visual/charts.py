import matplotlib.pyplot as plt
import pandas as pd

def show_bar_chart(logs):
    if not logs:
        print("No data")
        return

    df = pd.DataFrame([log.to_dict() for log in logs])
    summary = df.groupby("name")["used"].sum()

    summary.plot(kind="bar")
    plt.title("Bar Chart")
    plt.show()


def show_line_chart(logs):
    if not logs:
        print("No data")
        return

    df = pd.DataFrame([log.to_dict() for log in logs])
    df["index"] = range(1, len(df) + 1)

    for item in df["name"].unique():
        item_data = df[df["name"] == item]
        plt.plot(item_data["index"], item_data["used"], marker='o', label=item)

    plt.legend()
    plt.title("Line Chart")
    plt.show()


def show_pie_chart(logs):
    if not logs:
        print("No data")
        return

    df = pd.DataFrame([log.to_dict() for log in logs])
    summary = df.groupby("name")["used"].sum()

    plt.pie(summary, labels=summary.index, autopct="%1.1f%%")
    plt.title("Pie Chart")
    plt.show()
