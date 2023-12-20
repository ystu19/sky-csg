# sky-csg
光遇查身高，使用`应天API` `https://api.t1qq.com/user/register?cps=eLoJ0`提供的接口。
使用三种方式实现：
- 直接使用request请求接口
- 把request请求封装到tkinter中
- 使用flask框架做一个web页面查询

第一种和第三种方式已经实现，第二种方式目前不打算学习，精力投身到java学习中。
在使用第三种方式实现的过程中遇到了一些问题，大概描述一下：
- flask部署时有些页面的form提交到127.0.0.1:5000端口，好像在不同的地方都需要改，不知道有没有什么简单一点的方法。
- 使用docker部署的，熟悉了dockerfile文件的编辑以及构建。认识了alpine系统。
- 在国内服务器使用docker的时候需要配置docker源，使用alpine系统也需要配置它的源，它里面安装python后，pip也需要配置国内源。
- 时区不对可能会是因为使用的镜像的默认时区是UTC。
- python项目在pycharm运行正常，部署后运行不正常，可能是因为路径不对，引起不正常的地方有：自己写的模块导入的时候找不到模块；打开文件的时候找不到文件位置。


后续的更新方向可能是加入数据库，把查询过的id记录下来



使用docker部署
构建镜像：
docker build -t json_query2 .
运行：
docker run -d -v /opt:/opt -p80:8888 --name jaa json_query
dockerfile:

```Dockerfile
FROM alpine
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk update && apk add python3 py3-pip tzdata  \ 
    && cp -r -f /usr/share/zoneinfo/Hongkong /etc/localtime     \
    && apk del tzdata
RUN apk update && apk add python3 py3-pip
RUN pip3 install flask requests -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
WORKDIR /opt
EXPOSE 8888
CMD ["python3", "json_web_query/csg_web.py"]
```