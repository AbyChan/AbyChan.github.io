title: ' python数据采集百度知道'
date: 2014-12-03 17:17:17
tags:
- python
- 数据采集
- 数据爬取
- 百度知道
---

dom解析，用的是BeautifulSoup
还有小小的bug，因为百度知道的标签太混乱了
url还好，都是连续的http://zhidao.baidu.com/question/ + 问题的id

```python
def parseHtml(resultHtml,questionid):
    soup = BeautifulSoup(resultHtml)
    if( soup.find("span", class_="ask-title  ") != None ):
        questiontitle = soup.find("span", class_="ask-title  ").text
    else:
        questiontitle = None
    if( soup.find("pre", class_="line mt-10 q-content") != None ):
        fullquestion = soup.find("pre", class_="line mt-10 q-content").text
    else:
        fullquestion = None
    if( soup.find("span", class_="grid-r ask-time") != None ):
        asktime = soup.find("span", class_="grid-r ask-time").text
    else:
        asktime = None
    bestanster = None
    if( soup.find("div", class_="wgt-best ") != None ):
        if( soup.find("div", class_="wgt-best ").find("pre",class_="best-text mb-10") != None ):
            bestanster = soup.find("div", class_="wgt-best ").find("pre",class_="best-text mb-10").text
        elif( soup.find("div", class_="wgt-best ").find("div", class_="bd answer").find("pre",class_="best-text expand-exp mb-10") != None ):
            bestanster = soup.find("div", class_="wgt-best ").find("div", class_="bd answer").find("pre",class_="best-text expand-exp mb-10").text
    elif ( soup.find("div", class_="wgt-recommend ") != None ):
        if( soup.find("div", class_="wgt-recommend ").find("div", class_="bd answer").find("pre",class_="recommend-text mb-10") != None ):
            bestanster = soup.find("div", class_="wgt-recommend ").find("div", class_="bd answer").find("pre",class_="recommend-text mb-10").text
        elif( soup.find("div", class_="wgt-recommend ").find("div", class_="bd answer").find("pre",class_="recommend-text expand-exp mb-10") != None ):
            bestanster = soup.find("div", class_="wgt-recommend ").find("div", class_="bd answer").find("pre",class_="recommend-text expand-exp mb-10").text
    else:
        bestanster = None

    if ( soup.find("div", class_="wgt-answers") != None ):
        otherDiv = soup.find("div", class_="wgt-answers")
        if(otherDiv.find("div", class_="bd answer answer-first    ") != None ):
            anster1 = otherDiv.find("div", class_="bd answer answer-first    ")\
            .find("pre", class_="answer-text mb-10").text
        elif(otherDiv.find("div", class_="bd answer answer-first   answer-fold ") != None ):
            anster1 = otherDiv.find("div", class_="bd answer answer-first   answer-fold ")\
            .find("pre", class_="answer-text mb-10").text
        else:
            anster1 = None
            anster2 = None
            anster3 = None
        if(otherDiv.find("div", class_="bd answer    answer-fold ") != None ):
                answerfold = otherDiv.find_all("div", class_="bd answer    answer-fold ")
                if( len(answerfold) >1 ):
                    anster2 = answerfold[0].find("pre", class_="answer-text mb-10").text
                    anster3 = answerfold[1].find("pre", class_="answer-text mb-10").text
                else:
                    anster2 = answerfold[0].find("pre", class_="answer-text mb-10").text
                    if(otherDiv.find("div", class_="bd answer  answer-last  answer-fold ") != None  ):
                        anster3 = otherDiv.find("div", class_="bd answer  answer-last  answer-fold ")\
                        .find("pre", class_="answer-text mb-10").text
                    elif(otherDiv.find("div", class_="bd answer  answer-last   ") != None ):
                        anster3 = otherDiv.find("div", class_="bd answer  answer-last   ")\
                        .find("pre", class_="answer-text mb-10").text
                    else:
                        anster3 = None
        elif(otherDiv.find("div", class_="bd answer     ") != None ):
                answerfold = otherDiv.find_all("div", class_="bd answer     ")
                if( len(answerfold) >1 ):
                    anster2 = answerfold[0].find("pre", class_="answer-text mb-10").text
                    anster3 = answerfold[1].find("pre", class_="answer-text mb-10").text
                else:
                    anster2 = answerfold[0].find("pre", class_="answer-text mb-10").text
                    if(otherDiv.find("div", class_="bd answer  answer-last  answer-fold ") != None ):
                        anster3 = otherDiv.find("div", class_="bd answer  answer-last  answer-fold ")\
                        .find("pre", class_="answer-text mb-10").text
                    elif(otherDiv.find("div", class_="bd answer  answer-last   ") != None ):
                        anster3 = otherDiv.find("div", class_="bd answer  answer-last   ")\
                        .find("pre", class_="answer-text mb-10").text
                    else:
                        anster3 = None
        elif(otherDiv.find("div", class_="bd answer  answer-last  answer-fold ") != None ):
            anster2 = otherDiv.find("div", class_="bd answer  answer-last  answer-fold ")\
            .find("pre", class_="answer-text mb-10").text
            anster3 = None
        else:
            anster2 = None
            anster3 = None
    else:
        anster1 = None
        anster2 = None
        anster3 = None
#解析出来的变量是
#questionid,questiontitle,fullquestion,asktime,bestanster,anster1,anster2,anster3
```
