# 保存练习与同步 GitHub

Git 保存本地历史；GitHub 保存推送到远端的提交。仅保存文件或执行 commit 都不会自动上传。

## 平时学习后

先查看改动，确认只有本次代码、笔记和虚构示例数据，再执行：

```powershell
git status
git add main.py docs exercises tests data/samples
git commit -m "learn: 练习路径参数与请求校验"
git push
```

也可以通过 PyCharm 的 Commit 窗口选择文件并提交，再执行 Push。

## 首次连接远端（仅在尚未配置时）

在 GitHub 创建名为 `fastapi-learning` 的私有空仓库，不额外初始化 README。将下面的 `YOUR_USERNAME` 换成自己的用户名：

```powershell
git remote add origin https://github.com/YOUR_USERNAME/fastapi-learning.git
git push -u origin main
```

如果已有 origin，先用 `git remote -v` 查看，不要重复添加。如果还没有任何提交，先执行 `git add .` 和 `git commit -m "docs: 初始化 FastAPI 学习仓库"`。

首次 commit 若提示身份未配置，在本仓库设置自己的署名与 GitHub 提供的隐私邮箱，再重试：

```powershell
git config user.name "你的署名"
git config user.email "你的 GitHub 隐私邮箱"
```

通过正常登录窗口完成认证，不要把密码或访问令牌写进代码、笔记或远端 URL。

`.gitignore` 已忽略虚拟环境、PyCharm 本机配置、环境变量文件和本地数据库。示例数据放 `data/samples/`；不需要提交的个人数据放 `data/private/`。
