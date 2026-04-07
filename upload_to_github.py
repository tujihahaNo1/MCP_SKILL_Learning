#!/usr/bin/env python3
"""GitHub项目上传脚本 - 跨平台版本"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """执行命令并处理错误"""
    print(f"\n[*] {description}")
    print(f"    执行: {cmd}")
    
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ 错误: {description}失败")
        return False
    print(f"✅ {description}成功")
    return True

def main():
    print("=" * 50)
    print("GitHub 项目上传助手")
    print("=" * 50)
    
    # 切换到项目目录
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # 第1步: 初始化Git
    print("\n【第1步】初始化Git仓库")
    if not Path(".git").exists():
        if not run_command("git init", "初始化Git仓库"):
            return False
    else:
        print("⚠️  Git仓库已存在")
    
    # 第2步: 配置用户
    print("\n【第2步】配置Git用户信息")
    username = input("GitHub用户名 (如已配置,留空跳过): ").strip()
    if username:
        email = input("邮箱地址: ").strip()
        if email:
            run_command(f'git config user.name "{username}"', "设置用户名")
            run_command(f'git config user.email "{email}"', "设置邮箱")
    
    # 第3步: 状态检查
    print("\n【第3步】检查Git状态")
    run_command("git status", "查看状态")
    
    # 第4步: 添加和提交
    print("\n【第4步】提交代码")
    if input("确认添加所有文件? (y/n): ").lower() == 'y':
        if not run_command("git add .", "添加文件"):
            return False
        
        message = input("提交信息 [默认: Initial commit]: ").strip()
        if not message:
            message = "Initial commit: ADK框架学习项目"
        
        if not run_command(f'git commit -m "{message}"', "提交代码"):
            print("提示: 可能没有新的变化")
    
    # 第5步: 配置Remote
    print("\n【第5步】配置远程仓库")
    repo_url = input("GitHub仓库URL (格式: https://github.com/用户名/仓库名.git): ").strip()
    
    if not repo_url:
        print("❌ 仓库URL不能为空")
        return False
    
    # 检查是否已存在remote
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    if "origin" in result.stdout:
        print("⚠️  origin已存在，更新URL...")
        run_command(f'git remote set-url origin "{repo_url}"', "更新remote URL")
    else:
        run_command(f'git remote add origin "{repo_url}"', "添加remote")
    
    # 第6步: 设置分支
    print("\n【第6步】设置默认分支")
    run_command("git branch -M main", "设置分支为main")
    
    # 第7步: 推送
    print("\n【第7步】推送到GitHub")
    print("=" * 50)
    print("即将执行: git push -u origin main")
    print("=" * 50)
    
    if input("确认推送? (y/n): ").lower() == 'y':
        if run_command("git push -u origin main", "推送到GitHub"):
            print("\n" + "=" * 50)
            print("✅ 上传成功！")
            print("=" * 50)
            print(f"项目地址: {repo_url}")
            return True
        else:
            print("\n❌ 推送失败")
            print("可能的原因:")
            print("1. 网络连接问题")
            print("2. 认证失败 - 需要GitHub Token")
            print("3. 仓库URL错误")
            print("\n获取Token: https://github.com/settings/tokens")
            return False
    else:
        print("用户取消推送")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 异常错误: {e}")
        sys.exit(1)
