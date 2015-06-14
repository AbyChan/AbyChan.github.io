title: R语言中RMySQL的简单应用
date: 2014-12-20 22:31:02
tags:
- R
- RMysql
---

有时候用R处理数据的时候想随便把数据存到数据库中，那样用mysql联合查询起来会方便很多
可以用RMySQL包，导入导出蛮简单的

###安装RMySQL包
```R
install.packages("RMySQL")
```

###加载
```R
library(RMySQL)
```

###建立连接
```R
conn <- dbConnect(MySQL(), dbname = "rmysql", username="rmysql", password="rmysql",host="127.0.0.1",port=3306
```

###然后写入数据库直接用这个函数就行了
```R
dbWriteTable(conn, "tablename", data)
```

###读表同理
```R
dbReadTable(conn, "tablename")
```

###关闭连接
```R
dbDisconnect(conn)
```
