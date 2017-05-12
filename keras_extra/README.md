# 如何在Keras框架下进行多GPU并行

keras需要使用tensorflow作为backend

引用本文件夹`keras_extra.py中`的`make_parallel`函数

```
# use it like follows
model=Model(inputs=inputs,outputs=outputs)
model=make_parallel(model,2)  # this line is important
model.compile(optimizer='adadelta',loss='categorical_crossentropy',metrics=['accuracy'],)
```

The solution is according to https://medium.com/@kuza55/transparent-multi-gpu-training-on-tensorflow-with-keras-8b0016fd9012