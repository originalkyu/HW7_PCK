# 소수점 두번째 자리까지 출력
import numpy as np
import pandas as pd

def cos_sim(A, B):
    return np.dot(A, B) / (np.linalg.norm(A)*np.linalg.norm(B))

def main():
    # 데이터 준비
    Docs = [[int(i) for i in list("110101")], 
             [int(i) for i in list("111010")], 
             [int(i) for i in list("110100")]]
    npDocs = np.array(Docs)
    # print(npDocs)

    Query = np.array([1,1,0,0,1,0])
    for i, el in enumerate(npDocs):
        print("doc{}: {:.2f}".format(i+1,cos_sim(Query,el)))

if __name__ == "__main__":
    main()