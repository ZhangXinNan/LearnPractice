
# conda 导出环境
## 环境复制
方法 1：使用 conda create 命令的 --clone 参数可以直接复制一个环境 conda create --name <new_env> --clone <myenv>

方法 2：由于 conda 的环境其实是以一个文件夹的形式存在于 anaconda 的安装路径下，所以也可以直接找到这个文件夹（如~/anaconda3/envs），复制一份，修改文件夹名称为新环境名即可。

## 环境迁移
如果想在其他电脑上使用当前电脑的 conda 环境，需要分为两种情况讨论。

### 新电脑和当前电脑具有相同的平台和操作系统
有两种方法：
方法 1：使用 conda list 命令保存当前环境的包的信息到一个txt文件，即 conda list --explicit > spec-list.txt；根据这个文件可以在其他电脑上进行相同环境的安装，即conda create --name <new_env> --file spec-list.txt。

注意：对于pip安装的某些包，可能需要单独由pip通过类似的方法生成一个包的list（pip freeze >pip-requirements.txt），在新的电脑中再通过pip来安装这些包（pip install -r pip-requirements.txt）

方法2：利用 conda-pack 命令直接对环境进行打包，好处是打包之后得到是包文件可以直接复制到其他电脑后解压使用，不需要重新联网下载包了。具体步骤：

安装conda-pack包：conda install -c conda-forge conda-pack 或者 pip install conda-pack。
使用 conda pack 命令开始打包环境（尽量在待打包的环境之外的环境运行）：conda pack -n <my_env> 这个命令会将my_env环境打包生成一个my_env.tar.gz 的压缩文件，保存在当前路径下。
复制打包的压缩文件到新的电脑上，并解压到 anaconda的env目录下（如~/anaconda3/envs）：先在env目录中用打包环境的名字创建一个文件夹如 mkdir my_env， 然后将压缩包解压到这个目录 tar -xzvf my_env -C ~/anaconda3/envs/my_env
查看迁移环境是否存在：conda info -e

### 新电脑和当前电脑具有不同的平台和操作系统
导出 environment_name.yml 文件：conda env export > environment.yml
在新电脑上，利用生成的environment_name.yml 文件复现环境：conda env create -f environment.yml
注意：对于pip安装的某些包，可能需要单独由pip通过类似的方法生成一个包的list（pip freeze >pip-requirements.txt），在新的电脑中再通过pip来安装这些包（pip install -r pip-requirements.txt）


[anaconda / conda 环境复制和迁移](https://www.cnblogs.com/dawnlh/p/17341647.html)



