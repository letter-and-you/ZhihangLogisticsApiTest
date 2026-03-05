# 智航物流接口自动化测试项目
## 项目简介
本项目是针对智航物流业务系统的接口自动化测试解决方案，旨在覆盖核心业务接口的功能验证、异常场景校验、数据一致性校验等测试场景，提升接口测试效率，保障物流业务系统接口的稳定性、准确性和安全性。

项目支持自动化执行接口用例、生成测试报告、快速定位接口问题，可集成至CI/CD流程中，实现接口质量的持续监控。

## 技术栈
- **开发语言**：Python 3.8+（可根据实际技术栈调整，如Java/Go等）
- **核心框架**：
  - 接口请求：Requests（Python）/ RestAssured（Java）
  - 测试框架：Pytest（Python）/ TestNG（Java）
  - 数据驱动：Excel/YAML/JSON（用例数据管理）
  - 报告生成：Allure（可视化测试报告）
- **辅助工具**：
  - 环境管理：PyEnv/VirtualEnv（Python）/ Maven/Gradle（Java）
  - 日志管理：Loguru（Python）/ Log4j（Java）
  - 配置管理：ConfigParser（Python）/ Properties（Java）

## 项目结构
```
zhihang-logistics-api-test/
├── config/                # 配置文件目录
│   ├── env_config.yaml    # 环境配置（测试/预生产/生产）
│   └── global_config.py   # 全局常量配置（接口地址、超时时间等）
├── data/                  # 测试数据目录
│   ├── case_data/         # 用例数据（Excel/YAML/JSON）
│   └── mock_data/         # 模拟数据（如异常请求体、测试用基础数据）
├── libs/                  # 公共库/工具类
│   ├── api_client.py      # 接口请求封装（统一请求头、超时、重试等）
│   ├── log_handler.py     # 日志处理工具
│   └── utils.py           # 通用工具（加密、数据校验、时间处理等）
├── testcases/             # 测试用例目录（按业务模块划分）
│   ├── logistics_order/   # 物流订单模块
│   ├── waybill_trace/     # 运单轨迹模块
│   ├── customer_manage/   # 客户管理模块
│   └── base_case.py       # 用例基类（公共前置/后置、断言封装）
├── reports/               # 测试报告目录（Allure报告、日志文件）
├── run.py                 # 用例执行入口
├── requirements.txt       # Python依赖（Java为pom.xml）
└── README.md              # 项目说明文档
```

## 环境准备
### 1. 依赖安装
#### Python版本
```bash
# 安装依赖包
pip install -r requirements.txt
# 安装Allure（用于生成可视化报告，需提前安装Java环境）
# Windows/macOS/Linux 参考Allure官方文档：https://allurereport.org/docs/install/
```

#### Java版本（若使用Java技术栈）
```bash
# 编译并安装依赖
mvn clean install
```

### 2. 配置修改
- 进入`config/env_config.yaml`，修改对应环境的接口域名、密钥、数据库连接（如需）等配置：
```yaml
test:
  base_url: "https://test-api.zhihang-logistics.com"
  app_key: "test_xxxxxx"
  app_secret: "test_xxxxxx"
  timeout: 10
prod:
  base_url: "https://api.zhihang-logistics.com"
  app_key: "prod_xxxxxx"
  app_secret: "prod_xxxxxx"
  timeout: 10
```

## 快速开始
### 1. 执行单个模块用例
```bash
# Python（执行物流订单模块用例）
pytest testcases/logistics_order/ -vs --alluredir=reports/temp
# 生成Allure报告
allure generate reports/temp -o reports/html --clean
allure open reports/html
```

### 2. 执行所有用例
```bash
# Python
python run.py
# 或直接通过pytest执行
pytest testcases/ -vs --alluredir=reports/temp
```

### 3. 执行指定标签用例（如冒烟用例）
```bash
# Python（需在测试用例上添加@pytest.mark.smoke标签）
pytest -m smoke -vs --alluredir=reports/temp
```

## 用例编写规范
1. 测试用例按**业务模块**划分目录，单个接口的用例文件命名格式：`test_接口名.py`（如`test_create_order.py`）；
2. 用例需包含**正向场景**（正常入参、预期返回）和**异常场景**（参数缺失、参数错误、权限不足等）；
3. 用例数据优先使用`data/case_data`目录下的结构化文件（YAML/Excel），避免硬编码；
4. 断言需覆盖核心字段（如返回码、业务状态、关键数据一致性）；
5. 用例前置/后置操作（如创建测试数据、清理数据）统一在`base_case.py`中封装，复用逻辑。

## 测试报告
- 执行用例后，Allure报告会生成在`reports/html`目录下，打开`index.html`可查看：
  - 用例执行通过率、失败/跳过原因；
  - 接口请求/响应详情、耗时；
  - 日志输出、错误堆栈信息；
- 日志文件默认存储在`reports/logs`目录，按执行时间命名，便于问题排查。

## 常见问题
1. **接口请求超时**：检查`config/env_config.yaml`中的`timeout`配置，或确认目标环境网络可达；
2. **Allure报告无法生成**：确认已安装Java环境（JDK 8+），且Allure命令行工具配置到系统环境变量；
3. **用例数据读取失败**：检查`data/case_data`下的文件路径、格式是否正确（如YAML语法错误）；
4. **接口鉴权失败**：核对`env_config.yaml`中的`app_key`/`app_secret`是否匹配对应环境。

## 维护与扩展
1. 新增业务模块：在`testcases`下新建对应模块目录，继承`base_case.py`编写用例；
2. 新增工具类：在`libs`目录下添加通用方法，统一导入使用；
3. 扩展环境配置：在`env_config.yaml`中新增环境节点，修改`run.py`支持多环境切换；
4. 集成CI/CD：可将用例执行命令配置到Jenkins/GitLab CI等工具，实现定时/触发式执行。

## 注意事项
1. 禁止在生产环境执行破坏性用例（如删除真实订单、修改核心数据）；
2. 敏感配置（如密钥、数据库密码）建议通过环境变量注入，避免硬编码；
3. 执行用例前确保测试环境数据隔离，避免影响真实业务；
4. 定期更新测试用例，同步接口文档的变更，保证用例覆盖率和有效性。
