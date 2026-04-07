# GitHub一键推送命令

## 🚀 快速方式1: 运行Python脚本 (推荐)

```bash
python upload_to_github.py
```

**优点:**
- 交互式界面，易于操作
- 自动错误处理
- Windows/Mac/Linux通用

---

## 💻 快速方式2: 运行批处理脚本 (仅Windows)

```bash
upload_to_github.bat
```

---

## ⚡ 快速方式3: 手动命令 (高手用)

```bash
# 一行一行执行

# 1. 初始化git
git init

# 2. 配置用户 (仅首次需要)
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱地址"

# 3. 添加所有文件
git add .

# 4. 创建初次提交
git commit -m "Initial commit: ADK框架学习项目"

# 5. 添加远程仓库 (替换URL)
git remote add origin https://github.com/你的用户名/Learningproject.git

# 6. 设置main分支并推送
git branch -M main
git push -u origin main
```

---

## 📝 注意事项

### ⚠️ 首次推送常见问题

**问题1: "fatal: not a git repository"**
- 解决: 确保工作目录是项目根目录，且已执行 `git init`

**问题2: "error: src refspec main does not match any"**
- 解决: 确保已执行 `git commit`，项目有至少一次提交

**问题3: "Permission denied (publickey)"** (SSH错误)
- 解决: 用HTTPS而不是SSH，或配置SSH密钥
- 改用: `git remote set-url origin https://github.com/用户名/仓库名.git`

**问题4: "fatal: A branch named 'main' already exists"**
- 解决: 已有main分支了，直接push
  ```bash
  git push -u origin main
  ```

**问题5: 认证失败 (用户名/密码错误)
- 解决: GitHub已废弃密码认证，需要使用Token
- 获取Token: https://github.com/settings/tokens
- Scope选择: `repo`
- 使用Token作为密码

---

## 🔑 Token生成步骤

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token"
3. 勾选 "repo" 权限
4. 复制生成的Token
5. 首次push时提示输入密码，粘贴Token即可
6. (可选) 保存Token到本地：
   ```bash
   git config --global credential.helper store
   ```

---

## 📦 推送后验证

推送成功后，访问GitHub仓库检查:

```
https://github.com/你的用户名/Learningproject
```

应该看到:
- ✅ README.md
- ✅ requirements.txt
- ✅ agents/ 目录
- ✅ mcp_server/ 目录
- ✅ skills/ 目录
- ❌ .env (已被.gitignore排除)
- ❌ .venv/ (已被.gitignore排除)
- ❌ __pycache__ (已被.gitignore排除)
- ❌ 统计/ (已被.gitignore排除)

---

## 📚 后续更新命令

每次修改后的推送流程:

```bash
# 查看状态
git status

# 添加修改
git add .

# 提交
git commit -m "描述修改内容"

# 推送
git push
```

---

**推荐:** 使用 `upload_to_github.py` 脚本，它会引导你完成全部过程！
