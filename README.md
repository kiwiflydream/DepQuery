# DepQuery

#### 功能：快速查询项目依赖（Maven、Gradle、Ivy）

#### 功能演示图：

![](http://ww1.sinaimg.cn/large/68f7efe0gy1fjr6ysbwqng212w10o4qz.gif)

#### 插件构成

![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr8ivyiq2j20xz0gl404.jpg)

#### 安装：

1、首先安装Alfred软件

2、下载本[插件包](https://gitee.com/MrWood/DepQuery/attach_files/download?i=96253&u=http%3A%2F%2Ffiles.git.oschina.net%2Fgroup1%2FM00%2F01%2FF2%2FPaAvDFnDcUaAQS2OAAdx6-k2V9s.alfred%3Ftoken%3D048f8e69d6703656ea6d696e9abc5f9b%26ts%3D1505980759%26attname%3DDepQuery.alfredworkflow)，双击安装



#### 使用：

1、调起Alfred窗口

![](http://ww1.sinaimg.cn/large/68f7efe0gy1fjr73s5ztgj211q09oh0y.jpg)

2、输入命令

命令目前支持通过dq、mvn、gradle、ivy 四个关键词触发，目前他们功能完成一样

![](http://ww1.sinaimg.cn/large/68f7efe0gy1fjr773281uj20yy0aawpr.jpg)

![](http://ww1.sinaimg.cn/large/68f7efe0gy1fjr77l532kj20yk09w48g.jpg)

![](http://ww1.sinaimg.cn/large/68f7efe0gy1fjr78q5slnj20z80a4n8k.jpg)

![](http://ww1.sinaimg.cn/large/68f7efe0gy1fjr7979zrwj20yo0a013c.jpg)



3、输入查询关键词查询项目

![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr7b47zyyj20zo0xmb29.jpg)



4、选择你要查询的项目

比如我选择了上图的Spring Web 项目，选择后会进入大版本选择界面

5、选择你要的大版本

![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr7jn44g1j20zo0xeb29.jpg)

6、选择你要的小版本

![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr7m9zxhfj20xg0r2h8e.jpg)

7、选择你要的构建工具类型

![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr7nj8ce9j20ye0esdsk.jpg)

8、选择类型后鼠标点击或按一下回车键就会把依赖信息复制到你的粘贴板

![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr7u7jh7zj20la04gwgm.jpg)

不同类型复制的结果如下：

- Maven

```xml
<!-- https://mvnrepository.com/artifact/org.springframework/spring-web -->
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-web</artifactId>
    <version>5.0.0.RC2</version>
</dependency>
```

- Gradle

```groovy
// https://mvnrepository.com/artifact/org.springframework/spring-webmvc
compile group: 'org.springframework', name: 'spring-webmvc', version: '5.0.0.RC2'
```

- Ivy

```xml
<!-- https://mvnrepository.com/artifact/org.springframework/spring-web -->
<dependency org="org.springframework" name="spring-web" rev="5.0.0.RC2"/>
```



#### 进阶使用

- 分页
  - 关键词:页码
  - ![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr7xpwsxkj20yi0x24qp.jpg)
  - 不推荐使用：因为默认返回前10条记录，如果没有你想要的，推荐更改关键词，更具体的关键词可以使结果更少
- 精确查询
  - 形式：命令 '关键词'（就是多加一个单引号）
  - ![](http://ww1.sinaimg.cn/mw690/68f7efe0gy1fjr8hcis80j20yg0xi4qp.jpg)
  - 推荐使用：默认的 "命令 关键词"，当你输入第一个字母开始就可以不停的搜索请求了，例如你输入mvn spring，除非你单身够久，手速够快否则已经发送了搜索s、搜索sp、搜索spr、搜索spri、搜索sprin、搜索spring总共6次请求。导致搜索结果展示有点延迟。如果使用"命令 '关键词'"的形式，会等待你输入最后一个" ' "单引号才发送请求，效果更好。（注意单引号不要一下打完，再在里面输入，这样跟上面的形式没有区别） 