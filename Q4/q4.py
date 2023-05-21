import pandas as pd

def main():
    # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    # https://mizykk.tistory.com/16
    # use encoding, index_col
    # 2022년_계_총인구수 : [1]
    # 2022년_남_총인구수 : [5]
    df = pd.read_csv('gender2.csv', encoding='cp949', index_col=['2022년_계_총인구수'])
    columns = ['2022년_계_총인구수', '2022년_남_총인구수','2022년_여_총인구수']
    index = [0,1,2]
    # df = pd.read_csv('gender2.csv', encoding='cp949', index_col=columns)

    # Q 4_1, 4_2
    df = pd.read_csv('gender2.csv', encoding='cp949', usecols=columns)
    # print(df)

    # Q 4_3
    names = ['Total', 'Male', 'Female']
    cols_names = dict(zip(columns, names))
    df = df.rename(columns=cols_names)
    # df.columns=names
    print(df)
if __name__ == "__main__":
    main()