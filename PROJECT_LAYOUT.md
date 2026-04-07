# 项目结构说明

## 目录概览

```
Learningproject/
├── .adk/                    # ADK框架配置
├── .venv/                   # Python虚拟环境
├── .env                     # 环境变量(本地,不上传)
│
├── agents/                  # ADK代理
│   ├── agent.py            # 主代理实现
│   └── .adk/               # ADK配置
│
├── mcp_server/             # MCP服务器
│   ├── weather_mcp_server.py
│   └── .adk/               # ADK配置
│
├── skills/                 # Skill定义
│   └── weather_skill/
│       ├── SKILL.md
│       └── references/
│
├── 统计/                   # 本地数据(不上传)
│   ├── emergency_scores.json
│   └── emergency_scores_analysis_report.md
│
├── requirements.txt        # Python依赖
├── README.md              # 项目文档
├── PROJECT_LAYOUT.md      # 本文件
└── .env.example           # 环境配置示例
```

## 关键文件说明

| 文件 | 说明 |
|------|------|
| agents/agent.py | ADK代理,集成LiteLLM和豆包模型 |
| mcp_server/weather_mcp_server.py | MCP服务器实现 |
| skills/weather_skill/SKILL.md | Skill定义 |
| requirements.txt | Python包依赖 |
| .env.example | 环境配置模板 |

## 开发设置

1. 安装依赖: pip install -r requirements.txt
2. 配置.env: 复制.env.example并填入API密钥
3. 启动ADK: adk web
4. 访问: http://localhost:3000

## 本地文件(不上传GitHub)

- .env (敏感凭证)
- .venv/ (虚拟环境)
- __pycache__/ (Python缓存)
- 统计/ (本地数据)
- *.log (日志文件)

## 项目状态

- ADK框架集成完成
- MCP服务器已实现(3个工具)
- 豆包模型已配置(LiteLLM)
- 项目已准备好使用和扩展

最后更新: 2026年4月3日