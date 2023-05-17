# GoogleFormから送られて生成されたcsvを読みこむ

#%%
#ライブラリのインポート
import pandas as pd
import numpy as np
#ドライブのマウント
from google.colab import drive
drive.mount('/content/drive')

#%% 
#dataの取得
path = 'path'
data= pd.read_csv(path,encoding="UTF-8",index_col=0)
data.head()


#%%
#番号，名前，性別，年齢
def answer_subject(data):
  subject_lists = []
  data_len = len(data)
  for i in range(0,data_len):
    subject_lists_i = []
    for j in range(0,4):
      answer = data.iloc[i,j]
      subject_lists_i.append(answer)

    subject_lists.append(subject_lists_i)
    
  return subject_lists

#%% 
#アンケート1
def answer_dsq(data):
  data_len = len(data)
  dsq_lists = []
  for i in range(0,data_len):
    dsq_lists_i = []
    for j in range(4,22):
      #print(data.iloc[i,j])
      answer = data.iloc[i,j]
      if answer == '全く当てはまらない':
        answer = 1
      elif answer == '少し当てはまる':
        answer = 2
      elif answer == 'かなり当てはまる':
        answer = 3
      elif answer == '非常に当てはまる':
        answer = 4
      else:
        answer = answer

      dsq_lists_i.append(answer)
    dsq_lists.append(dsq_lists_i)
  return dsq_lists

#アンケート2
def answer_wsq(data):
  data_len = len(data)
  wsq_lists = []
  for i in range(0,data_len):
    wsq_lists_i = []
    for j in range(22,60):
      answer = data.iloc[i,j]
      if answer == '気にせず運転する':
        answer = 1
      elif answer == '気配りしながら運転するが負担ではない':
        answer = 2
      elif answer == '運転することを少し負担に感じる':
        answer = 3
      elif answer == '緊張や無理をしいられて負担が大きい':
        answer = 4
      elif answer == '負担が大きすぎて運転したくない':
        answer = 5
      else:
        answer = answer

      wsq_lists_i.append(answer)
    wsq_lists.append(wsq_lists_i)
  return wsq_lists

# %%
#取得データの確認
subject_lists = answer_subject(data)
print(subject_lists)
dsq_lists = answer_dsq(data)
print(dsq_lists)
wsq_lists = answer_wsq(data)
print(wsq_lists)
sdsq_lists = answer_sdsq(data)
print(sdsq_lists)

# %%
path_dsq_tool = "path"
dsq_tool = pd.read_excel(path_dsq_tool,sheet_name=1,index_col=0)
dsq_tool.head()
print(dsq_tool.head())
print(dsq_tool.shape)

# %%
path_wsq_tool = "path"
wsq_tool = pd.read_excel(path_wsq_tool,sheet_name=1,index_col=0)
wsq_tool.head()
print(wsq_tool.head())
print(wsq_tool.shape)

# %%
#アンケート１用excel作成
def dsq_excel(dsq_lists,dsq_tool):
  dsq_len = len(dsq_lists)
  for i in range(0,dsq_len):
    dsq_len_i = len(dsq_lists[i])
    for j in range(0,dsq_len_i):
      dsq_tool.iloc[j,i+1] = dsq_lists[i][j]
  return  dsq_tool

# %%
#アンケート２用excel作成
def wsq_excel(wsq_lists,wsq_tool):
  wsq_len = len(wsq_lists)
  for i in range(0,wsq_len):
    wsq_len_i = len(wsq_lists[i])
    for j in range(0,wsq_len_i):
      wsq_tool.iloc[j,i+1] = wsq_lists[i][j]
  return  wsq_tool


# %%
dsq_tool = dsq_excel(dsq_lists,dsq_tool)
print(dsq_tool.head())


# %%
wsq_tool = wsq_excel(wsq_lists,wsq_tool)
print(wsq_tool.head())

# %%
dsq_tool.to_excel('dsq_finish.xlsx',sheet_name='1')
wsq_tool.to_excel('wsq_finish.xlsx',sheet_name='1')