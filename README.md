# ADK、MCP和Skill完整示例

这是一个展示如何使用Google ADK（Agent Development Kit）、Model Context Protocol（MCP）和Skills来构建AI代理的完整示例。

## 项目结构

```
Learningproject/
├── mcp_server/
│   └── weather_mcp_server.py      # MCP服务器实现
├── skills/
│   └── weather_skill/
│       ├── SKILL.md               # Skill主文件（必需）
│       └── references/
│           └── API_REFERENCE.md   # API参考文档
├── agent.py                       # ADK Agent主文件
├── requirements.txt               # Python依赖
├── .env                          # 环境变量配置
└── README.md                     # 本文件
```

## 核心概念

### 1. **MCP（Model Context Protocol）**
Model Context Protocol是一个开放标准，用于规范LLM如何与外部应用、数据源和工具通信。

**特点**：
- 采用客户端-服务器架构
- 标准化的工具、资源和提示符定义
- 支持local（stdio）和remote（SSE/HTTP）连接

**在本示例中**：
- `weather_mcp_server.py` 是MCP服务器
- 提供3个工具：`get_weather`、`get_all_cities`、`compare_weather`

### 2. **Skill（技能）**
Skill是一个自包含的功能单元，包含执行特定任务所需的指令、资源和工具。

**结构（3个层级）**：
- **L1 - 元数据** (SKILL.md frontmatter): 技能名称、描述
- **L2 - 指令** (SKILL.md body): 详细的使用说明和最佳实践
- **L3 - 资源** (references/, assets/): 额外的参考材料

**在本示例中**：
- `skills/weather_skill/SKILL.md` 定义了如何使用天气工具
- `references/API_REFERENCE.md` 提供详细的API文档

### 3. **ADK Agent（代理）**
ADK是一个Python框架，用于构建具有工具、内存、状态管理等功能的AI代理。

**在本示例中**：
- `agent.py` 创建了一个天气助手Agent
- 集成了MCP工具和Skill

## 快速开始

### 1. 安装依赖

```bash
# 创建虚拟环境（可选但推荐）
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
# 复制 .env.example 为 .env
cp .env.example .env   # macOS/Linux
# 或在Windows上: copy .env.example .env

# 编辑 .env 文件并填入真实的API密钥
# LLM_API_KEY=从豆包控制台获取
# LLM_BASE_URL=豆包API地址
```

**重要**: .env 文件包含敏感信息，已被 .gitignore 排除，**不会上传到GitHub**

### 3. 测试MCP服务器

```bash
# 直接运行MCP服务器进行测试（可选）
python mcp_server/weather_mcp_server.py
```

### 4. 使用ADK Web UI运行代理

```bash
# 启动ADK Web开发环境
adk web

# 在浏览器中访问 http://localhost:8000
# 选择 weather_assistant Agent进行交互
```

## 使用示例

### 示例1：查询单个城市天气

**用户**：北京现在的天气怎么样？

**Agent步骤**：
1. 识别用户要查询北京的天气
2. 调用MCP工具 `get_weather` with city="beijing"
3. 接收返回的天气数据
4. 使用Skill中的指导生成友好的回答

**为什么需要Skill？**
- Skill告诉Agent如何解释天气数据
- 提供温度、湿度等的解释指南
- 给出基于天气的建议

### 示例2：比较两个城市

**用户**：广州和上海哪里更暖和？

**Agent步骤**：
1. 识别需要比较两个城市
2. 调用MCP工具 `compare_weather` with city1="guangzhou", city2="shanghai"
3. 分析对比结果
4. 返回哪个城市更暖和

## 每个文件的详细说明

### `mcp_server/weather_mcp_server.py`

**作用**：实现MCP服务器
**关键部分**：
- `@app.list_tools()` - 定义服务器提供的工具
- `@app.call_tool()` - 执行工具调用的处理函数
- `main()` - 启动stdio服务器

**概念**：
```
MCP客户端 ←→ MCP服务器
(ADK Agent)   (weather_mcp_server.py)
   |              |
   |-- 请求工具列表 →|
   |← 返回工具定义 --|
   |              |
   |-- 调用工具 →|
   |← 返回结果 --|
```

### `skills/weather_skill/SKILL.md`

**结构**：
```yaml
---
name: weather-skill                    # L1: 元数据
description: 天气查询技能
---
# 本体内容为 L2: 指令
# - 使用方法
# - 工具调用指南
# - 错误处理建议
```

**作用**：
- 告诉Agent如何使用MCP工具
- 提供最佳实践和示例
- 指导Agent生成更好的回答

### `skills/weather_skill/references/API_REFERENCE.md`

**作用**：L3资源层
- 详细的API文档
- 数据结构说明
- 错误处理指南

### `agent.py`

**核心代码**：
```python
# 1. 加载Skill
weather_skill = load_skill_from_dir("skills/weather_skill")

# 2. 创建MCP工具
mcp_tools = McpToolset(connection_params=...)

# 3. 创建Agent，将两者都添加到tools列表
root_agent = Agent(
    tools=[
        skill_toolset.SkillToolset(skills=[weather_skill]),
        mcp_tools,
    ]
)
```

## 工作流程图

```
用户输入
  ↓
Agent接收
  ↓
Agent理解用户意图
  ↓
查看可用Skill ← Skill告诉Agent如何处理
  ↓
决定调用哪个MCP工具
  ↓
MCP服务器执行工具
  ↓
返回数据给Agent
  ↓
Agent根据Skill指导格式化回答
  ↓
返回给用户
```

## 扩展和修改

### 添加新的MCP工具

1. 在MCP服务器中添加工具定义：
```python
@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "new_tool":
        # 实现新工具逻辑
        pass
```

2. 在Skill中记录如何使用：
```markdown
## 新工具使用指南
...
```

### 添加新的Skill

1. 创建新目录：`skills/new_skill/`
2. 添加 `SKILL.md` 文件
3. 在 `agent.py` 中加载：
```python
new_skill = load_skill_from_dir("skills/new_skill")
skill_tools = skill_toolset.SkillToolset(
    skills=[weather_skill, new_skill]
)
```

### 使用不同的模型

在 `agent.py` 中修改 `model` 参数：
```python
root_agent = Agent(
    model='gemini-1.5-pro',  # 或其他支持的模型
    ...
)
```

## 🧠 关键学习点

### 为什么需要MCP？
- **标准化** - 统一的接口来集成各种工具
- **灵活性** - 支持本地和远程工具
- **可组合** - 轻松添加/移除工具

### 为什么需要Skill？
- **模块化** - 将功能组织成独立的单元
- **可重用** - Skill可以在多个Agent之间共享
- **上下文优化** - 只在需要时加载Skill信息
- **指导** - 为Agent提供最佳实践和使用指南

### MCP vs Skill对比

| 特性 | MCP | Skill |
|------|-----|-------|
| 作用 | 实现和暴露工具 | 指导代理如何使用工具 |
| 层级 | 2层（协议定义） | 3层（元数据、指令、资源） |
| 输出 | 工具执行结果 | 指导信息 |
| 位置 | 通常是独立进程/服务 | 本地文件 |

## 📖 更多资源

- ADK官方文档: https://adk.dev
- MCP规范: https://modelcontextprotocol.io
- Agent Skills规范: https://agentskills.io
- Google Gemini API: https://aistudio.google.com

## ❓ 常见问题

### Q: MCP服务器什么时候启动？
A: 当ADK Agent初始化时，McpToolset会自动启动MCP服务器进程。

### Q: Skill是必需的吗？
A: 不是。但Skill能显著改进Agent的性能和行为。

### Q: 可以在adk web中看到Skill的内容吗？
A: 是的。Agent会在需要时自动加载Skill的指令信息。

### Q: 如何调试MCP工具调用？
A: 检查MCP服务器的输出日志（print语句）和Agent的运行日志。

## 📝 许可证

本示例代码用于教学目的。

---

**祝你学习愉快！** 🎉
如有问题，欢迎参考官方文档或社区资源。
