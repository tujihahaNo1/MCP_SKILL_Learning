@echo off
REM GitHub上传脚本 - Windows版本

echo ========================================
echo GitHub 项目上传
echo ========================================

REM 第1步: 初始化Git仓库
echo.
echo [1/5] 初始化Git仓库...
git init
if errorlevel 1 (
    echo 错误: git初始化失败。请确保已安装Git。
    pause
    exit /b 1
)

REM 第2步: 配置用户信息
echo.
echo [2/5] 配置Git用户信息...
echo 请输入你的GitHub用户名（例如: your-username）:
set /p username=
echo 请输入你的GitHub邮箱（例如: your.email@gmail.com）:
set /p email=

git config user.name "%username%"
git config user.email "%email%"

REM 第3步: 添加所有文件
echo.
echo [3/5] 添加所有文件...
git add .
if errorlevel 1 (
    echo 错误: git add失败
    pause
    exit /b 1
)

REM 第4步: 提交
echo.
echo [4/5] 提交代码...
git commit -m "Initial commit: ADK框架学习项目"
if errorlevel 1 (
    echo 错误: git commit失败
    pause
    exit /b 1
)

REM 第5步: 添加远程仓库
echo.
echo [5/5] 关联远程仓库...
echo 请输入GitHub仓库URL (例如: https://github.com/你的用户名/Learningproject.git)
set /p repourl=

git remote add origin %repourl%
if errorlevel 1 (
    echo 错误: 可能已经配置过remote，尝试更新...
    git remote set-url origin %repourl%
)

REM 设置main分支并推送
echo.
echo 正在设置main分支...
git branch -M main

echo.
echo ========================================
echo 准备推送！
echo ========================================
echo.
echo 即将执行: git push -u origin main
echo.
pause

git push -u origin main
if errorlevel 1 (
    echo.
    echo 推送失败！
    echo 可能原因:
    echo 1. 网络问题
    echo 2. GitHub认证失败
    echo 3. 仓库URL错误
    echo.
    echo 如果是认证问题，可以使用GitHub Token:
    echo https://github.com/settings/tokens
    echo.
    pause
    exit /b 1
) else (
    echo.
    echo ========================================
    echo ✅ 推送成功！
    echo ========================================
    echo 项目已上传到: %repourl%
    echo.
    pause
)
