import pickle
from sklearn.preprocessing import LabelBinarizer
from collections import Counter
import pandas as pd
import numpy as np

#--------------------------------------------------
# 载入样本的工具函数
def patchMatrix(doc,dst_size=(0,0),default=0,dtype=np.int32):
    '''fill items with default value to unify each dimension of them
    '''
    doc=[row for row in doc]
    if dst_size[1]==0:
        max_len=np.max([len(item) for item in doc])
    else:
        max_len=dst_size[1]
    for i in range(len(doc)):
        length=len(doc[i])
        if length<max_len:
            doc[i]=list(doc[i])+[default]*(max_len-length)
    if dst_size[0]>len(doc):
        doc.extend([[default]*max_len]*(dst_size[0]-len(doc)))
    return np.array(doc,dtype=dtype)


#--------------------------------------------------------
# 采样工具函数
def over_sample(train_df,pos_rate=0.3,neg_rate=0.2):
    '''过采样方法,对train_df中的正中负样本比例进行调整
    pos_rate: 正样本占比
    neg_rate: 负样本占比
    中性样本占比将计算得出
    
    该函数中保证原始样本中的每一条都至少被采样一次，以保证样本的完全性
    其中中性样本数量扩充到原来的1.1倍，其他样本数量依概率计算得出
    注意，不要对验证集使用样本过（欠）采样方法！
    '''
    if pos_rate==0 or neg_rate==0:
        return train_df
    pos=train_df[train_df.Opinion=='pos'].index.tolist()
    neg=train_df[train_df.Opinion=='neg'].index.tolist()
    neu=train_df[train_df.Opinion=='neu'].index.tolist()
    
    neu_rate=1-neg_rate-pos_rate
    total_cnt=1.1*np.max([len(neu)/neu_rate,len(pos)/pos_rate,len(neg)/neg_rate])
    add_neg_cnt=int(total_cnt*neg_rate-len(neg))
    add_pos_cnt=int(total_cnt*pos_rate-len(pos))
    add_neu_cnt=int(total_cnt*neu_rate-len(neu))

    pos_items=train_df.loc[np.random.choice(pos,size=(add_pos_cnt))]
    neg_items=train_df.loc[np.random.choice(neg,size=(add_neg_cnt))]
    neu_items=train_df.loc[np.random.choice(neu,size=(add_neu_cnt))]
    df=pd.concat([train_df,pos_items,neg_items,neu_items],ignore_index=True)
    df=df.iloc[np.random.permutation(len(df))].reset_index(drop=True)
    return df

'''载入数据
'''
def load_data(filename='data/car_review_data.pkl',pos_rate=0.2,neg_rate=0.2):

    import pickle
    import numpy as np
    from collections import Counter
    data,w2v,vocs,id2words,id2pos=pickle.load(open(filename,'rb'))
    valid_data=data

    df=valid_data
    print('data info:')
    cnter=Counter(df.Opinion.tolist())
    for key in cnter:
        print(key,cnter[key],cnter[key]/len(df))

    '''划分训练集，验证集'''
    from sklearn.cross_validation import StratifiedShuffleSplit
    ti,vi=list(StratifiedShuffleSplit(df.Opinion,n_iter=5,test_size=0.2,random_state=100))[0]
    tids=set(df.loc[ti,'SentenceId'].tolist())
    valid_df=df[df.SentenceId.apply(lambda x:x not in tids)].reset_index(drop=True)
    train_df=df[df.SentenceId.apply(lambda x:x in tids)].reset_index(drop=True)

    neg_df=train_df[train_df.Opinion=='neg']
    pos_df=train_df[train_df.Opinion=='pos']

    import pandas as pd
    train_df=over_sample(train_df,pos_rate=pos_rate,neg_rate=neg_rate)

    print('dst info:')
    cnter=Counter(train_df.Opinion.tolist())
    for key in cnter:
        print(key,cnter[key],cnter[key]/len(train_df))
        
    return train_df,valid_df,w2v,id2words,id2pos