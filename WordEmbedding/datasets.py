class SogouCACorpus(object):
    '''搜狗实验室全网新闻数据(SogouCA) version:2012
    下载地址：http://www.sogou.com/labs/resource/ca.php
    输入参数：fname 语料文件名，例如: news_tensite_xml.dat
    首次调用将在同级文件夹中生成以.jiebaresult结尾的分词后的文件
    '''
    def __init__(self,fname):
        self.fname=fname
        
    def __cut(self,fname):
        import jieba
        print('正在进行分词处理...')
        dst_filename=fname+'.jiebaresult'
        cnt=0
        with open(fname,encoding='gbk',errors='ignore') as f:
            dst=open(dst_filename,'w',encoding='utf8')
            for line in f.readlines():
                if line.startswith('<content>'):
                    cnt+=1
                    line=line.strip()[9:-10]
                    words=jieba.lcut(line)
                    dst.write(' '.join(words))
                    dst.write('\n')
                    if cnt%10000==0:
                        print('已处理完毕%d条数据..'%cnt)
            dst.close()
        print('%s 保存成功,共有数据%d条。'%(dst_filename,cnt))
        return dst_filename
    
    def __iter__(self):
        fname=self.fname
        #如果不存在分词后的结果，先进行分词处理
        if fname.endswith('.jiebaresult')==False:
            import os
            jieba_filename=fname+'.jiebaresult'
            if os.path.exists(jieba_filename)==False:
                self.__cut(fname)
        else:
            jieba_filename=fname
        
        #读取分好词的文件
        with open(jieba_filename,encoding='utf8',errors='ignore') as f:
            for line in f.readlines():
                yield line.strip().split(' ')