# %%
# Colabでipynbとして動かす場合
import pandas as pd
import cv2
import numpy as np
# !pip install japanize_matplotlib
# import japanize_matplotlib
# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, set_link_color_palette
# from PIL import Image
from sklearn.cluster import KMeans

# #20220203追記
# !pip install --upgrade openpyxl

# %%
from google.colab import drive
drive.mount('/content/drive')



# %%
# %%
#アンケートの読み込み
path = 'path'
dsq_raw = pd.read_excel(path,index_col=0)
# 行列は適宜変更
dsq_trim = dsq_raw.iloc[20:28, 1:21] 
print(dsq_trim)
dsq=dsq_trim.transpose()
print(dsq)



# %%
path_dsq = 'path'
dsq_raw = pd.read_excel(path_dsq,index_col=0)
dsq_trim = dsq_raw.iloc[20:28, 1:21]
#print(dsq_trim)
dsq=dsq_trim.transpose()
cust_array = np.array([dsq[1].tolist(),
                       dsq[2].tolist(),
                       dsq[3].tolist(),
                       dsq[4].tolist(),
                       dsq[5].tolist(),
                       dsq[6].tolist(),
                       dsq[7].tolist(),
                       dsq[8].tolist(),
                       ])
cust_array = cust_array.T

random = np.random.RandomState(528)
pred = KMeans(n_clusters=2,random_state=random,n_init=50).fit_predict(cust_array)
dsq['cluster_id']=pred
print(dsq.sort_values('cluster_id'))
dsq

# %%
dsq['cluster_id'].value_counts(ascending=True)