生成Glue测试数据
===============

在学习大数据分析时需要制作很多测试数据，我就分享一下我制作测试数据的代码。

## 使用方法

### 制定生成数据件数

*glue_csv.py*

```py
DATA_COUNT=10
```

### 生成数据

```bash
python glue_csv.py
```

### 上传S3

```bash
aws s3 cp  ./data_0001.csv s3://${BUCKET_NAME}/input/data/sales_database/sails_csv/data_0001.csv  
```
