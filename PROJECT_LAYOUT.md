# 项目结构【已整理】

## 📁 项目目录树

```
Learningproject/
├── .adk/                             # ADK框架配置
├── .venv/                            # Python虚拟环境
├── .env                              # 环境变量配置(豆包API密钥)
│
├── agents/                           # ADK代理程序
│   ├── agent.py                      # ✅ 主代理(root_agent)
│   └── .adk/                         # ADK配置
│
├── mcp_server/                       # MCP服务器实现
│   ├── weather_mcp_server.py        # ✅ 天气MCP服务(包含3个工具)
│   └── .adk/                         # ADK配置
│
├── skills/                           # Skill定义(已转换格式)
│   └── weather_skill/
│       ├── SKILL.md                  # ✅ Skill定义文件
│       └── references/
│
├── 统计/                             # 本地数据分析(不上传GitHub)
│   ├── emergency_scores.json         # 原始数据(451,978条)
│   └── emergency_scores_analysis_report.md  # 分析报告
│
├── requirements.txt                  # Python依赖列表
├── README.md                         # 项目主文档
└── PROJECT_LAYOUT.md                 # 本文件
```

## 🗂️ 各目录说明

### `/agents` - ADK代理程序
- **agent.py**: 包含`root_agent`定义，使用LiteLLM连接豆包模型
- 责任：实现AI代理的主要逻辑，集成MCP工具

### `/mcp_server` - MCP服务器
- **weather_mcp_server.py**: MCP服务实现，提供3个工具
  - `get_weather`: 获取城市天气
  - `get_all_cities`: 列出所有城市
  - `compare_weather`: 比较两个城市天气

### `/skills` - Skill定义
- **SKILL.md**: Skill元数据和功能定义
- 用于代理快速查找和使用技能

### `/统计` - 数据分析项目
- **emergency_scores.json**: 原始数据集(JSONL格式)
- **emergency_scores_analysis_report.md**: 完整的统计分析报告
  - 包含9个分析section
  - 数据分布、统计指标、趋势分析
  - 洞察和优化建议

## 📋 核心配置文件

| 文件 | 用途 |
|------|------|
| `.env` | 环境变量：LLM_API_KEY, LLM_BASE_URL |
| `requirements.txt` | Python包依赖 |
| `README.md` | 项目文档 |

## ⚙️ 启动方式

### 启动ADK Web应用
```bash
# 安装依赖
pip install -r requirements.txt

# 启动ADK Web
adk web
```
访问 `http://localhost:3000` 使用Web界面

### 直接调用代理
```python
from agents.agent import root_agent

# 使用代理
result = await root_agent.run("查询北京的天气")
```

## 📊 数据分析输出

分析报告已保存在: `统计/emergency_scores_analysis_report.md`

**关键统计指标：**
- 总记录: 451,978
- 通过率: 0.01%
- 平均评分: 8.52
- 相似度: 0.5706 ± 0.026

## ✨ 项目现状

✅ **已完成**
- ADK框架集成完成
- MCP服务器实现
- 豆包模型配置(LiteLLM)
- 数据分析和报告生成
- 代码整理和清理

🔧 **可选扩展**
- 添加更多MCP工具
- 扩展Skill库
- 实现数据可视化

---

**最后更新**: 2026年4月3日
**项目状态**: 整理完成，可用状态
