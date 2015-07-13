title: shell中调用R语言并传入参数的两种方法
date: 2014-12-30 12:19:01
tags:
- r语言
- shell
- linux
---

第一种：
```bash
Rscript myscript.R
```
R脚本的输出
第二种：
```bash
R CMD BATCH myscript.R
# Check the output
cat myscript.Rout
```
调用R脚本的全部控制台log

传入参数：
在脚本中add
```R
args<-commandArgs(TRUE)
```
然后shell中：
```bash
Rscript myscript.R arg1 arg2 arg3
```
注意取出来的参数是所有参数连在一起的character
