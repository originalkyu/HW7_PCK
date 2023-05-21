import numpy as np
import pandas as pd

def main():
    datas = np.array([[1000,25],[280,120],[900,30]])
    index = ["store"+str(i) for i in range(1,4)]
    columns = ["unit price", "number"]

    # Q3_1
    df = pd.DataFrame(datas, index=index, columns=columns)
    print(df)
    
    # Q3_2
    df['total price'] = df['unit price'] * df['number']
    print(df)

    # Q3_3
    df = df.sort_values(by='total price', ascending=False)
    print(df.head(2))

if __name__ == "__main__":
    main()