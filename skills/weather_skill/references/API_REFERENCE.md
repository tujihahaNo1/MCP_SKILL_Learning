# 天气数据API参考

## 数据结构

每个城市的天气数据包含以下字段：

### 字段详解

| 字段 | 类型 | описание | 单位 |
|------|------|---------|------|
| `city` | string | 城市名称（中文） | - |
| `temperature` | number | 当前温度 | °C |
| `condition` | string | 天气状况（晴天、多云、雨、雪等） | - |
| `humidity` | number | 相对湿度 | % |
| `wind_speed` | number | 风速 | km/h |

## API工具

### 1. get_weather

**说明**: 获取指定城市的天气信息

**参数**:
- `city` (string, required): 城市英文名称

**返回**: 天气数据对象

**示例调用**:
```json
{
  "city": "beijing"
}
```

**示例响应**:
```json
{
  "city": "北京",
  "temperature": 20,
  "condition": "晴天",
  "humidity": 45,
  "wind_speed": 10
}
```

### 2. get_all_cities

**说明**: 获取所有支持的城市列表

**参数**: 无

**返回**: 城市列表对象

**示例响应**:
```json
{
  "cities": ["beijing", "shanghai", "guangzhou"],
  "count": 3
}
```

### 3. compare_weather

**说明**: 比较两个城市的天气信息

**参数**:
- `city1` (string, required): 第一个城市英文名称
- `city2` (string, required): 第二个城市英文名称

**返回**: 对比数据对象

**示例调用**:
```json
{
  "city1": "beijing",
  "city2": "shanghai"
}
```

**示例响应**:
```json
{
  "city1": {
    "city": "北京",
    "temperature": 20,
    "condition": "晴天",
    "humidity": 45,
    "wind_speed": 10
  },
  "city2": {
    "city": "上海",
    "temperature": 22,
    "condition": "多云",
    "humidity": 60,
    "wind_speed": 12
  },
  "comparison": {
    "temperature_diff": -2,
    "warmer_city": "shanghai"
  }
}
```

## 天气条件代码

| 代码 | 中文 | 描述 |
|------|------|------|
| sunny | 晴天 | 晴朗天空，无云或少云 |
| cloudy | 多云 | 有云但不是全覆盖 |
| rainy | 雨 | 降雨天气 |
| snow | 雪 | 下雪天气 |
| windy | 刮风 | 风力很强 |
| stormy | 暴风雨 | 雷暴天气 |
| foggy | 雾 | 能见度低 |

## 错误处理

### 错误响应示例

**不支持的城市**:
```json
{
  "error": "城市 'paris' 不支持。支持的城市: beijing, shanghai, guangzhou"
}
```

**缺少必需参数**:
```json
{
  "error": "缺少必需的参数: city"
}
```

## 使用提示

1. 城市名称必须是小写英文
2. 所有温度值都是摄氏度
3. 风速以公里/小时表示
4. 湿度值范围是0-100
5. 如果查询失败，总是提供有示例的支持城市列表
