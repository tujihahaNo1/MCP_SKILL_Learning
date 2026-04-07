# GitHub上传流程指南

## 📋 完整上传步骤

### 第1步: 初始化Git仓库

```bash
cd /f/Learningproject
git init
```

### 第2步: 配置.gitignore文件

创建 `.gitignore` 文件避免上传不必要的文件：

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# 环境配置(含敏感信息)
.env
.env.local

# 其他
.adk/
**/​.adk/
*.log
```

### 第3步: 配置Git用户信息

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 第4步: 添加文件并提交

```bash
# 添加所有文件 (统计/目录已在.gitignore中被排除)
git add .

# 首次提交
git commit -m "Initial commit: ADK框架、MCP服务器和Skill"
```

### 第5步: 在GitHub上创建空仓库

1. 登录 https://github.com
2. 点击右上角 `+` → `New repository`
3. 填写信息:
   - **Repository name**: `Learningproject` (或自定义)
   - **Description**: "ADK Agent框架学习项目 + 应急评分数据分析"
   - **Visibility**: 选择 Public/Private
   - **不要勾选** "Add README"、"Add .gitignore"、"Add license"
4. 点击 `Create repository`

### 第6步: 关联远程仓库

复制GitHub提供的HTTPS或SSH链接，然后：

```bash
# HTTPS方式 (推荐新手)
git remote add origin https://github.com/YOU_USERNAME/Learningproject.git

# 或 SSH方式 (需配置SSH密钥)
git remote add origin git@github.com:YOU_USERNAME/Learningproject.git
```

### 第7步: 推送到GitHub

```bash
# 重命名默认分支为main (可选，GitHub默认)
git branch -M main

# 推送代码
git push -u origin main
```

---

## 🔐 认证方式选择

### 方式A: HTTPS + Token (更简单)

1. GitHub → Settings → Developer settings → Personal access tokens → Generate new token
2. 勾选 `repo` 作用域
3. 复制token
4. 第一次push时，GitHub会提示输入用户名和密码，password字段填token
5. 或配置凭证管理:
   ```bash
   git config --global credential.helper store
   ```

### 方式B: SSH密钥 (更安全)

```bash
# 生成SSH密钥
ssh-keygen -t ed25519 -C "your.email@example.com"

# 将公钥内容添加到GitHub
# Settings → SSH and GPG keys → New SSH key
# 将~/.ssh/id_ed25519.pub的内容粘贴进去

# 测试连接
ssh -T git@github.com
```

---

## 📦 首次推送的完整命令组

```bash
cd /f/Learningproject

# 1. 初始化
git init

# 2. 配置用户信息
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 3. 添加.gitignore (已在项目中)
# 4. 提交本地代码
git add .
git commit -m "Initial commit: ADK框架学习项目"

# 5. 关联远程 (替换URL)
git remote add origin https://github.com/USERNAME/Learningproject.git

# 6. 设置默认分支并推送
git branch -M main
git push -u origin main
```

---

## 📊 日常更新流程

```bash
# 修改代码后

# 查看状态
git status

# 添加修改
git add .

# 提交
git commit -m "描述修改内容"

# 推送到GitHub
git push
```

---

## 🐛 常见问题

### Q: 上传时忘记添加.gitignore，现在.venv等文件已经上传了？
**A:** 先删除已追踪的文件:
```bash
git rm --cached .venv/ -r
git commit -m "Remove venv from tracking"
git push
```

### Q: 想修改已推送的提交信息？
**A:** 最后一次提交可以修改:
```bash
git commit --amend -m "新的提交信息"
git push --force-with-lease  # 谨慎使用
```

### Q: 如何克隆项目到其他电脑？
**A:** 
```bash
git clone https://github.com/USERNAME/Learningproject.git
cd Learningproject
pip install -r requirements.txt
```

### Q: .env文件包含敏感信息，已经推送了怎么办？
**A:** 
```bash
# 从历史记录中删除
git rm --cached .env
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Remove .env from tracking"
git push

# 然后更新GitHub上的.env (操作GitHub网页删除)
# 重新生成新的API密钥
```

---

## ✅ 推荐的项目README模板

上传前，将 `README.md` 更新为:

```markdown
# Learningproject

🎓 ADK(Agent Development Kit) 框架学习项目

## 📋 项目内容

### 1. ADK框架示例体系
- **agents/**: ADK代理实现，集成豆包模型
- **mcp_server/**: MCP服务器(天气工具演示)
- **skills/**: Skill定义

## 🚀 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 启动ADK Web
adk web
```

访问 `http://localhost:3000` 使用Web界面

## 📁 项目结构

见 PROJECT_LAYOUT.md

## 🔑 环境配置

创建 `.env` 文件:
```
LLM_API_KEY=your_key_here
LLM_BASE_URL=http://your_api_base
LLM_MODEL=doubao-seed-1-8-251228
```

## 📚 学习资源

- ADK官方文档: https://adk-docs.example.com
- MCP文档
- 示例代码和工具

## 📝 License

MIT
```

---

## 🎯 总结清单

上传前检查清单:

- ✅ `git init` 已执行
- ✅ `.gitignore` 已创建
- ✅ 本地git commit已完成
- ✅ GitHub仓库已创建
- ✅ remote URL已配置
- ✅ `git push` 已推送
- ✅ README.md已更新
- ✅ .env文件未被上传
- ✅ __pycache__未被上传
- ✅ .venv未被上传

---

**需要我帮你立即执行这个流程吗？**

我可以:
1. ✨ 创建.gitignore文件
2. ✨ 执行git初始化和本地提交
3. ✨ 更新README.md
4. ✨ 生成push命令供你复制执行
