
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [materials studio](#materials-studio)
  - [旋转分子](#旋转分子)
  - [内存占用高](#内存占用高)
  - [经验教程](#经验教程)
  - [图像重影问题](#图像重影问题)
  - [下载安装破解](#下载安装破解)
- [cluster](#cluster)
  - [bug](#bug)
    - [error](#error)
    - [solution](#solution)
- [VESTA](#vesta)

<!-- /code_chunk_output -->

# materials studio

## 旋转分子

SHIFT+右键  旋转
ALT+右键    平移

## 内存占用高

关闭结构窗口

## 经验教程
<http://muchong.com//t-11279111-1>

## 图像重影问题

MS界面→tools→options→Graphics ：
查看其中的选项是否勾选，如果没有勾选，全部勾选，重启MS；
如果已经勾选，现全部不勾选，重启MS。

## 下载安装破解
<https://www.zdfans.com/html/48131.html>

# cluster

## bug

### error

提交的任务一直显示run，并行程序却没有真正执行，标准输出中相关的内容什么都没有

### solution

mpi通信需要你的账号在计算节点之前可以ssh免密登录，但是你的.ssh目录不明原因被修改了导致节点互访出现问题

# VESTA

晶胞transform时先remove symmetry
