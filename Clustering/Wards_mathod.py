# %%
# Colabでipynbとして動かす場合
import pandas as pd
import cv2
import numpy as np
# !pip install japanize_matplotlib
import japanize_matplotlib
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster, set_link_color_palette
from PIL import Image

# #20220203追記
# !pip install --upgrade openpyxl

# %%
from google.colab import drive
drive.mount('/content/drive')

# %%
#アンケートの読み込み
path = 'path'
dsq_raw = pd.read_excel(path,index_col=0)
# 行列は適宜変更
dsq_trim = dsq_raw.iloc[20:28, 1:21] 
print(dsq_trim)
dsq=dsq_trim.transpose()
print(dsq)

#ウォード法によるクラスタリング
linkage_result_dsq = linkage(dsq, method='ward', metric='euclidean')
#整形用
#plt.figure(num=None, figsize=(9, 3), facecolor='white', edgecolor='black',dpi=350)
#
plt.figure(num=None, figsize=(5, 2), facecolor='white', edgecolor='black',dpi=350)
set_link_color_palette(['red', 'blue']) 
dendrogram(linkage_result_dsq, labels=dsq.index,color_threshold=5,above_threshold_color='purple')
plt.savefig("path", format="eps")
plt.tick_params(labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.xlabel('Subjects',fontsize=13)
plt.ylabel('Distance',fontsize=13)
plt.savefig("path", format="png")
dsq_ward = cv2.imread("path")

plt.show()

