

```bash
#!/bin/bash
 
echo "ps:目前只支持x64场景,arm场景请酌情修改脚本."
read -p "请输入你vscode的commit id : " commit
if [ ! -z "$commit" ]; then
test -d ${HOME}/.vscode-server/bin/$commit || mkdir -p ${HOME}/.vscode-server/bin/$commit
echo "通过国内加速站下载vscode文件"
mkdir -p ~/vscode-backup
wget --no-check-certificate https://vscode.download.prss.microsoft.com/dbazure/download/stable/$commit/vscode-server-linux-x64.tar.gz -O ~/vscode-backup/vscode-server-linux-x64.tar.gz
tar -zxvf ~/vscode-backup/vscode-server-linux-x64.tar.gz -C ~/vscode-backup
cp -rf ~/vscode-backup/vscode-server-linux-x64/* ${HOME}/.vscode-server/bin/$commit/
echo "vscode配置完毕"
rm -rf ~/vscode-backup/
echo "清理旧文件"
else
echo "请查看vscode的关于找到对应的版本commit id"
fi
```


# 参考资料
[解决 VS Code 自动更新版本后卡在连接界面](https://www.lfhacks.com/tech/vscode-server/)


