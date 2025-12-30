# Goyal & Welch (2008) 复现项目

复现论文: [A Comprehensive Look at The Empirical Performance of Equity Premium Prediction](https://www.ivo-welch.info/research/journalcopy/2008-rfs.pdf)

Goyal, A., & Welch, I. (2008). A comprehensive look at the empirical performance of equity premium prediction. The Review of Financial Studies, 21(4), 1455-1508.

## 项目简介

本项目提供了 Goyal & Welch (2008) 论文的完整 Python 复现代码，包括:
- 年度数据分析 (Annual Data Analysis)
- 月度数据分析 (Monthly Data Analysis)
- 样本内和样本外预测性能评估
- 可视化图表生成

## 项目结构

```
ReplicationGoyalWelch2008-main/
├── data/                           # 数据文件夹
│   ├── GW05_original_annual.csv    # 年度数据
│   ├── GW05_original_monthly.csv   # 月度数据
│   └── Goyal_Welch_2008updated.csv # 更新数据
├── output/                         # 输出文件夹（运行后生成）
│   ├── annual_results.csv          # 年度分析结果
│   ├── monthly_results.csv         # 月度分析结果
│   └── *.png                       # 生成的图表
├── main.py                         # 主程序入口
├── helper.py                       # 辅助函数
├── data_loader.py                  # 数据加载模块
├── config.py                       # 配置文件
├── requirements.txt                # 依赖包列表
├── GW08_replication.ipynb          # Jupyter notebook（可选）
└── README.md                       # 本文件
```

## 安装依赖

```bash
pip install -r requirements.txt
```

主要依赖:
- numpy >= 1.21.0
- pandas >= 1.3.0
- statsmodels >= 0.13.0
- matplotlib >= 3.4.0
- scipy >= 1.7.0

## 使用方法

### 1. 基本用法

运行所有分析（年度+月度数据）:
```bash
python main.py --mode all
```

仅运行年度数据分析:
```bash
python main.py --mode annual
```

仅运行月度数据分析:
```bash
python main.py --mode monthly
```

### 2. 生成图表

添加 `--plot` 参数生成可视化图表:
```bash
python main.py --mode all --plot
```

图表将保存在 `output/` 文件夹中。

### 3. 分析特定变量

分析特定的预测变量:
```bash
python main.py --mode monthly --variable dp --plot
```

查看所有可用变量:
```bash
python main.py --list-vars
```


## 可用的预测变量

### 年度数据变量
- `dp`: Dividend-price ratio (股息价格比)
- `dy`: Dividend yield (股息收益率)
- `ep`: Earnings-price ratio (盈利价格比)
- `de`: Dividend-payout ratio (股息支付率)
- `b/m`: Book-to-market ratio (账面市值比)
- `ntis`: Net equity expansion (净股票发行)
- `eqis`: Equity issuing activity (股票发行活动)

### 月度数据变量
- `de`: Dividend-payout ratio
- `svar`: Stock variance
- `lty`: Long-term yield
- `ltr`: Long-term return
- `infl`: Inflation
- `tms`: Term spread (期限利差)
- `tbl`: Treasury bill rate (短期国债利率)
- `dfy`: Default yield spread (违约收益率利差)
- `dp`: Dividend-price ratio
- `dy`: Dividend yield
- `ep`: Earnings-price ratio
- `b/m`: Book-to-market ratio
- `e10p`: 10-year moving average earnings-price ratio
- `csp`: Cross-sectional premium
- `ntis`: Net equity expansion

## 输出结果

### 年度数据输出指标
- `IS_R2_head_1927`: 样本内 R² (1927-2005)
- `IS_R2_head_OOS`: 样本内 R² (样本外预测期)
- `IS_R2_head_1965`: 样本内 R² (1965-2005)
- `OOS_oR2`: 样本外 R²
- `dRMSE`: RMSE 差异
- `MSEf`: MSE-F 统计量

### 月度数据输出指标
- `IS_R2_head_log`: 样本内 R² (对数股权溢价)
- `IS_R2_head`: 样本内 R²
- `IS_R2_head_trunc`: 样本内 R² (截断模型)
- `OOS_R2_head`: 样本外 R²
- `share_T`: 截断预测比例
- `share_U`: 斜率设为0的比例
- `OOS_R2_head_trunc`: 样本外 R² (截断模型)
- `dRMSE`: RMSE 差异

## 配置说明

可以在 `config.py` 中修改以下参数:
- 数据文件路径
- 分析时间段
- 样本外预测的估计期长度
- 输出设置（图表格式、DPI等）
## 复现结果和分析

**复现结果和分析详见本项目的result_and_analysis.md文件**
## 注意事项

1. 数据从1927年开始，因为完整的股票收益数据（包含分红）从该年份开始可用
2. 某些变量（如 `csp`）的数据起始时间较晚
3. 通货膨胀率 (`infl`) 有特殊处理：使用2期滞后（因为需要等待1个月获取数据）
4. 结果可能与原论文略有差异，这是由于数据更新和计算精度等因素造成的

## 参考文献

- Goyal, A., & Welch, I. (2008). A comprehensive look at the empirical performance of equity premium prediction. The Review of Financial Studies, 21(4), 1455-1508.
- Campbell, J. Y., & Thompson, S. B. (2008). Predicting excess stock returns out of sample: Can anything beat the historical average? The Review of Financial Studies, 21(4), 1509-1531.

## License

详见 [LICENSE](LICENSE) 文件。

## 其他资源

- 原论文: https://www.ivo-welch.info/research/journalcopy/2008-rfs.pdf
