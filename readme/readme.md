# 项目仓库创建流程

## 创建仓库

在PyCharm中，菜单栏选择 Git -->Github --> share Project on Github

![image-20240325180735314](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325180735314.png?raw=true)





在该页面填写仓库名称、描述等信息后，点击share即可

![image-20240325180910634.png](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325180910634.png?raw=true)



## 拉取代码

进入想要存放项目的目录下，打开git bash页面

![image-20240325181158210.png](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325181158210.png?raw=true)

输入命令：`git clone url`（其中url为仓库的地址）

![image-20240325181315773.png](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325181315773.png?raw=true)

实现下图中的效果就表示拉取成功

![image-20240325181446994.png](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325181446994.png?raw=true)

即可在对应目录下看到项目文件

![image-20240325181513914.png](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325181513914.png?raw=true)



## 提交代码

提交代码分为三步：

* `git add .` / `git add fileName` 
  * `git add .` 表示将该项目目录下所有文件的修改都进行提交
  * `git add fileName` 表示只将特定文件的修改进行提交
* git commit -m 'xxx' （xxx表示这次提交的描述信息）
* git push

![image-20240325181513914.png](https://github.com/tudouPotatoo/Personal_Information_Protection_Compliance_Audit_Information_System/blob/master/readme/%E6%95%99%E7%A8%8B.assets/image-20240325181513914.png?raw=true)

> 注意事项1：
>
> 需要先成为项目的Collaborator才可以提交代码
>
> 
>
> 注意事项2：
>
> 如果报：fatal: The current branch xxx has no upstream branch. To push the current branch and set the remote as upstream的错误
>
> 可以使用git push --set-upstream origin master该命令，将本地的master分支和远程的master建立关联，以后在本地master分支就可以用git push直接推送到远程的master分支了
>
> 
>
> 注意事项3：
>
> 如果远程仓库的代码有更新，且还没有拉取到本地，此时提交代码会失败。
>
> 需要先将远程仓库的代码拉取下来，手动进行代码合并之后再进行提交。

