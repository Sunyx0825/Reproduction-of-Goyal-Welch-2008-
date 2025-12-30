# 快速开始指南

## 第一步：安装依赖

在项目根目录下运行:

```bash
pip install -r requirements.txt
```

或者单独安装各个包:

```bash
pip install numpy pandas statsmodels matplotlib scipy
```

## 第二步：验证安装

运行以下命令查看帮助信息:

```bash
python main.py --help
```

查看所有可用变量:

```bash
python main.py --list-vars
```

## 第三步：运行分析

### 选项1：运行示例脚本

```bash
python example.py
```

这将运行一个简单的示例，分析年度和月度数据的 dp 变量。

### 选项2：运行完整分析

运行所有变量的分析:

```bash
python main.py --mode all
```

生成图表:

```bash
python main.py --mode all --plot
```

### 选项3：分析特定变量

分析年度数据的特定变量:

```bash
python main.py --mode annual --variable dp --plot
```

分析月度数据的特定变量:

```bash
python main.py --mode monthly --variable dp --plot
```

## 第四步：查看结果

运行后，结果将保存在 `output/` 文件夹中:

- `annual_results.csv` - 年度分析结果
- `monthly_results.csv` - 月度分析结果
- `annual_*.png` - 年度数据图表
- `monthly_*.png` - 月度数据图表

## 常见问题

### Q: 如何修改分析参数？

A: 编辑 `config.py` 文件，修改以下参数:
- 起始和结束年份/日期
- 样本外预测估计期长度
- 输出图表格式和DPI

### Q: 如何添加新的预测变量？

A:
1. 在 `data_loader.py` 中添加新变量的计算
2. 在 `config.py` 中将新变量添加到 `indep_vars` 列表
3. 运行分析

### Q: 结果与论文不完全一致？

A: 这可能由以下原因造成:
- 数据更新（某些历史数据点被修正）
- 计算精度差异
- 软件包实现细节
- 论文中可能存在的勘误

这些差异通常很小，不影响主要结论。

## 下一步

- 阅读原始论文了解理论背景
- 阅读 `README.md` 了解详细的项目说明


## 需要帮助？

如果遇到问题，请检查:
1. 是否所有依赖都已正确安装
2. 数据文件是否在 `data/` 文件夹中
3. Python 版本是否 >= 3.7
