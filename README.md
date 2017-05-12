# DeepLearningPractice2017

大连理工大学信息检索研究室2017深度学习实践培训内容

## 运行环境
Python 3.5及以上 (建议安装[Anaconda](https://www.continuum.io/downloads/))

需要额外安装的包如下:

- Keras
- Theano
- gensim
- jieba


## 嵌入式词向量(Word Embedding)训练

包含了3种常用的词向量训练方法的代码，包括Word2Vec, FastText, GloVe。[点击进入](WordEmbedding/WordEmbedding.ipynb)

关于三种词向量方法效果的可视化对比，可参见 https://github.com/liyumeng/VisualWordEmbedding 

## 句子级情感分析

在豆瓣语料上，实现了简单的CNN及LSTM模型的句子级情感分析模型。

[CNN模型](SentimentAnalyze/douban_cnn.ipynb)

[LSTM模型](SentimentAnalyze/douban_lstm.ipynb)

## 面向评价对象的情感分析

在CCF2016[基于视角的领域情感分析](http://www.datafountain.cn/#/competitions/237/intro)竞赛的数据集上，实现了两种Aspect粒度的情感分析模型，包括：

TD-LSTM模型 [论文地址](https://arxiv.org/abs/1512.01100) [代码示例](AspectSentimentAnalyze/car_review_td_lstm.ipynb)

Deep-Memory模型 [论文地址](https://arxiv.org/abs/1605.08900) [代码示例](AspectSentimentAnalyze/car_review_memory_nn.ipynb)


#### 欢迎大家fork, *点击右上角star！*


![](others/banner.jpg)
