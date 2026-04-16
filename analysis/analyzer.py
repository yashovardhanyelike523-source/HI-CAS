import numpy as np
import pandas as pd

def numpy_analysis(logs):
    if not logs:
        print("No data")
        return

    values = [log.used for log in logs]
    arr = np.array(values)

    print("Average:", np.mean(arr))
    print("Max:", np.max(arr))
    print("Min:", np.min(arr))


def pandas_analysis(logs):
    if not logs:
        print("No data")
        return

    df = pd.DataFrame([log.to_dict() for log in logs])
    print(df.groupby("name")["used"].sum())