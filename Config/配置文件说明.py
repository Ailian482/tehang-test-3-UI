# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/5/17 上午10:38


"""
1. 配置文件作用（主要用在大项目中）：
    ① 将项目中的路径信息、用户信息甚至是网页信息提取出来，写入配置文件里面，然后再case中读取这个配置信息，从而完成项目信息的配置。
    ② 用户信息和网址的复用性很高的时候（用例多），如果把这些信息都直接写到case中，那么一旦需要更改这些信息时，要修改的地方就很多，
    就会造成耗时耗力的现象，如果使用配置文件记录这些信息，只要修改配置文件对应信息即可
2. 配置文件常见的格式的类型：
    ini、yaml、xml、properties、txt、py
"""

