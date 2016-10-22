## 0w Assignment
by @hysic

### 1. 图解中国人的生活水平变化
#### 1.1 你认为应该用什么样的数字来度量中国人的生活水平变化?
* 生活水平(Standard of living)[维基百科](https://en.wikipedia.org/wiki/Standard_of_living)给出,生活水平与众多因素相关, 包括收入, 职业, 阶层差异, 贫困率, 住房, 获得生活必需品所需要的工作时间, GDP, 通胀率, 年休假天数, 医保, 教育, 预期寿命, 疾病发生率, 物价, 基础设施, 经济增长, 经济政治稳定性, 政治宗教自由, 环境质量, 气候, 安全等许多方面.测量标准主要有人均实际收入(根据通胀调整)和贫困率, 其他的还包括医保, 收入增长不均, 教育水平, 预期寿命, 再比如特定商品的数量, 比如每1000人拥有的冰箱数量.
* 联合国的[2015人类发展报告(HDR)](http://hdr.undp.org/sites/default/files/2015_human_development_report_1.pdf)中, 用人类发展指数(HDI)来描述人类发展, 主要包括三个维度(pdf第17页): 健康长寿的身体, 汲取知识的能力, 拥有不错的生活水平. 其中生活水平一项是用人均国民总收入(Gross national income, GNI)来衡量的.
* 自己脑洞 + google: 城镇居民人均可支配收入/农村居民家庭人均纯收入, 恩格尔系数, 人均 GDP, 居民消费价格指数(CPI).
* 综合以上三点, 并结合能够获取的数据, 选取以下几项是反映生活水平: 人均可支配收入(未考虑通胀), 通胀率, 人均预期寿命, 贫困率.

#### 1.2 尝试找到这样的数据源并画出图看看。
* 其实国家统计局已经提供了很多类似的数据和图像.
* 城镇居民人均可支配收入/农村居民家庭人均纯收入变化图([数据及图像来源](http://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0A03&sj=2014))(注: 2013年之后二者合二为一, 称人均可支配收入)

![](https://cloud.githubusercontent.com/assets/5415646/12299877/e1ecb7ac-ba53-11e5-8561-23707d959f78.png)

* 另有[官方可视化产品](http://data.stats.gov.cn/jpg.htm?m=turnto&id=442)
* 人均预期寿命变化图([数据来源](http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/qgrkpcgb/201209/t20120921_30330.html))

![](https://cloud.githubusercontent.com/assets/5415646/12299896/f7939b0c-ba53-11e5-8d02-1435803fb556.png)

* 我还想画通胀率变化和贫困率变化, 可暂时找不到数据.

#### 1.3 用这种数字来衡量有什么样的缺点？
* 这些统计数据都是算术平均值, 无法反映具体数据的分布情况.(收入分配可以用[基尼系数](https://zh.wikipedia.org/wiki/%E5%9F%BA%E5%B0%BC%E7%B3%BB%E6%95%B0)来衡量)
* 这些知识纸面上冷冰冰的统计数据, 无法衡量很多主观上的东西, 比如幸福感, 生娃带来的焦虑感, 工作压力等等.


### 2. 理解双盲实验
From [维基百科](https://zh.wikipedia.org/wiki/%E9%9B%99%E7%9B%B2)
> 双盲是科学方法的一种，目的是避免研究结果受安慰剂效应或观察者偏向所影响。在各种科学研究领域中，从医学、食品、心理到社会科学及法证都有使用双盲方法进行实验。

* 双盲实验解决的痛点: [安慰剂效应](https://zh.wikipedia.org/wiki/%E5%AE%89%E6%85%B0%E5%8A%91%E6%95%88%E6%87%89); [观察者期望效应](https://zh.wikipedia.org/wiki/%E8%A7%80%E5%AF%9F%E8%80%85%E6%9C%9F%E6%9C%9B%E6%95%88%E6%87%89).
* 循证医学往往采用双盲+随机对照试验(RCT), 来检测药物/方法的有效性.


### 3. 学习使用 Google Ngram Viewer
> 学习使用Google Ngram Viewer服务，并研究你关心的某一组词汇的变化。

* TEDx演讲[我们从五百万本书里学到了什么](http://v.youku.com/v_show/id_XODAxMjA1MjQ4.html), 介绍了 Ngram 的来历和玩法, 官方也有[说明文档](https://books.google.com/ngrams/info).
* 我试了下牛顿, 爱因斯坦, 霍金三位物理大神的[频率对比](https://books.google.com/ngrams/graph?content=Isaac+Newton%2CAlbert+Einstein%2CStephen+Hawking&case_insensitive=on&year_start=1600&year_end=2008&corpus=15&smoothing=5&share=&direct_url=t4%3B%2CIsaac%20Newton%3B%2Cc0%3B%2Cs0%3B%3BIsaac%20Newton%3B%2Cc0%3B%3BISAAC%20NEWTON%3B%2Cc0%3B.t4%3B%2CAlbert%20Einstein%3B%2Cc0%3B%2Cs0%3B%3BAlbert%20Einstein%3B%2Cc0%3B%3BALBERT%20EINSTEIN%3B%2Cc0%3B.t4%3B%2CStephen%20Hawking%3B%2Cc0%3B%2Cs0%3B%3BStephen%20Hawking%3B%2Cc0%3B%3BSTEPHEN%20HAWKING%3B%2Cc0), 牛大神当年的人气真是牛啊, 碾压小爱和小金(这当然也和当前书籍数量较少有关).
* Ngram 还有其他语言, 其中就包括简体中文语料库, 试了下[四人帮的人气排名](https://books.google.com/ngrams/graph?content=%E7%8E%8B%E6%B4%AA%E6%96%87%2C%E5%BC%A0%E6%98%A5%E6%A1%A5%2C%E6%B1%9F%E9%9D%92%2C%E5%A7%9A%E6%96%87%E5%85%83&year_start=1949&year_end=2008&corpus=23&smoothing=1&share=&direct_url=t1%3B%2C%E7%8E%8B%E6%B4%AA%E6%96%87%3B%2Cc0%3B.t1%3B%2C%E5%BC%A0%E6%98%A5%E6%A1%A5%3B%2Cc0%3B.t1%3B%2C%E6%B1%9F%E9%9D%92%3B%2Cc0%3B.t1%3B%2C%E5%A7%9A%E6%96%87%E5%85%83%3B%2Cc0#t1%3B%2C%E7%8E%8B%E6%B4%AA%E6%96%87%3B%2Cc1%3B.t1%3B%2C%E5%BC%A0%E6%98%A5%E6%A1%A5%3B%2Cc1%3B.t1%3B%2C%E6%B1%9F%E9%9D%92%3B%2Cc1%3B.t1%3B%2C%E5%A7%9A%E6%96%87%E5%85%83%3B%2Cc1), 嗯...
* 当然, 目前这种统计方式只包括书, 不包括杂志, 报纸等其他出版物, Google 的野心显然更大, 它的目的是记录人类文明的历史, 其中包括手稿, 报纸, 当然还还包括非文字的内容, 比如艺术和绘画等等.


### 4. 理解 Simpson's Paradox
* 假设有两种治疗感冒的方法, A 和 B. 对于男人, A 的疗效比 B 好; 对于女人, A 的疗效也比 B 好. 可是把男女放在一起来统计, A 的疗效却不如 B.
* 这十分反直觉, 就好比说, 现在有一个感冒患者, 我们不知道TA的具体信息, 那么应该采用 B 疗法, 但 TA 不管是男是女, 又应该采用 A 疗法. 这不是很奇怪么? 可是这确是实实在在的[临床统计数据](https://en.wikipedia.org/wiki/Simpson%27s_paradox#Kidney_stone_treatment), 只不过治疗对象不是男女感冒, 而是大小两种肾结石.  

| |Treatment A | 	Treatment B |
| -------- | :----------------- | :----------- |
| Small Stones | 	Group 1: 93%(81/87)| Group 2: 87%(234/270)|
| Large Stones | 	Group 3: 73% (192/263) | Group 4: 69%(55/80) |
| Both |	78% (273/350) | 83% (289/350) |

* 从具体的数据中可以看出, 这并不是一个完全的随机试验, 两种疗法对两种不同结石的样本数有很大差异, 或者说对于每一种疗法来说, 两种结石的样本数在总数中所占的权重不同, 导致出现看似矛盾的结果. 或者说, 这种统计里还隐含着另一个变量, 结石大小, 会影响采用的具体疗法, 针对小结石更倾向于采取疗效稍差 B 疗法, 针对与大结石更倾向于采用疗效稍好 A 疗法.
* 这个[可视化产品](http://vudlab.com/simpsons/)非常直观, 针对的是加州伯克利大学申请中"疑似"性别歧视的案例. 通过改变女生申请 Easy Dept. 的比例, 可以生成类似的看似矛盾的数据: 每一个系的女生录取比例都高于男生, 而从全校来看女生录取比例却低于男生.


### 5. 利用贝叶斯定理解题

> 学习贝叶斯定理，做下题：
已知某种疾病的发病率是0.001，即1000人中会有一个人得病。现有一种试剂可以检验患者是否得病，它的准确率是0.99，即在患者确实得病的情况下，它有99%的可能呈现阳性。它的误报率是5%，即在患者没有得病的情况下，它有5%的可能呈现阳性。现有一个病人的检验结果为阳性，请问他确实得病的可能性有多大

C: 病人确实患病.
T: 病人检验结果为阳性.
把题目翻译一下: 已知 P(C) = 0.001, P(T|C) = 0.99, P(T|not C) = 0.05, 求P(C|T).
解:
P(T) = P(T|C) * P(C) + P(T|not C) * P(not C)
     = 0.99 * 0.001 + 0.05 * 0.999
     = 0.05094
P(C|T) = P(C and T)/P(T) = P(C)*P(T|C)/P(T)
       = 0.001 * 0.99 / 0.05094
       = 0.019
