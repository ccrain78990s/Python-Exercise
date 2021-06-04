# jieba-tw

結巴(jieba)斷詞台灣繁體 特化版本


## 原理

採用和原始jieba相同的演算法，替換其詞庫及HMM機率表製做出針對台灣繁體的jieba斷詞器


## 安裝

```sh
pip install git+https://github.com/APCLab/jieba-tw.git
```

## 使用

本專案特化部分如下

```python
import jieba

jieba.case_sensitive = True # 可控制對於詞彙中的英文部分是否為case sensitive, 預設False
```

## 斷詞

```python
import jieba

#如果您的電腦同時要使用兩個版本的jieba，請自訂cache檔名，避免兩個cache互相蓋住對方
#jieba.dt.cache_file = 'jieba.cache.new'

seg_list = jieba.cut("新竹的交通大學在新竹的大學路上")
print(" / ".join(seg_list))
# 新竹 / 的 / 交通 / 大學 / 在 / 新竹 / 的 / 大學路 / 上 /

```

其餘操作請參考[結巴官方文件]

[結巴官方文件]: https://github.com/fxsjy/jieba

## 其餘注意事項

參考[ldkrsi版本]之說明

[ldkrsi版本]: https://github.com/ldkrsi/jieba-zh_TW
