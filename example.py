"""
快速开始示例脚本

这个脚本展示了如何使用本项目进行分析
"""

# 导入必要的库
from data_loader import load_annual_data, load_monthly_data, get_data_summary
from helper import get_statistics, get_monthly_statistics

def example_annual_analysis():
    """年度数据分析示例"""
    print("=" * 60)
    print("年度数据分析示例")
    print("=" * 60)

    # 加载数据
    data_annual = load_annual_data()
    print(f"\n数据已加载: {len(data_annual)} 个观测值")

    # 查看数据摘要
    summary = get_data_summary(data_annual, 'annual')
    print(f"\n股权溢价统计:")
    print(f"  均值: {summary['equity_premium_mean']:.4f}")
    print(f"  标准差: {summary['equity_premium_std']:.4f}")

    # 分析单个变量
    print(f"\n分析变量: dp (股息价格比)")
    result = get_statistics(
        data_annual,
        indep='dp',
        dep='equity_premium',
        start=1927,
        end=2005,
        est_periods_OOS=20,
        plot='no'
    )

    print(f"\n结果:")
    for key, value in result.items():
        print(f"  {key}: {value}")

    return result


def example_monthly_analysis():
    """月度数据分析示例"""
    print("\n" + "=" * 60)
    print("月度数据分析示例")
    print("=" * 60)

    # 加载数据
    data_monthly = load_monthly_data()
    print(f"\n数据已加载: {len(data_monthly)} 个观测值")

    # 查看数据摘要
    summary = get_data_summary(data_monthly, 'monthly')
    print(f"\n股权溢价统计:")
    print(f"  均值: {summary['equity_premium_mean']:.4f}")
    print(f"  标准差: {summary['equity_premium_std']:.4f}")

    # 分析单个变量
    print(f"\n分析变量: dp (股息价格比)")
    result = get_monthly_statistics(
        data_monthly,
        indep='dp',
        start='1927-12-01',
        end='2005-12-01',
        est_periods_OOS=240,
        plot='no'
    )

    print(f"\n结果:")
    for key, value in result.items():
        print(f"  {key}: {value}")

    return result


if __name__ == '__main__':
    # 运行示例
    print("Goyal & Welch (2008) 复现项目 - 快速开始示例\n")

    # 年度数据分析
    annual_result = example_annual_analysis()

    # 月度数据分析
    monthly_result = example_monthly_analysis()

    print("\n" + "=" * 60)
    print("示例分析完成!")
    print("=" * 60)
    print("\n提示:")
    print("1. 使用 'python main.py --help' 查看所有可用选项")
    print("2. 使用 'python main.py --mode all --plot' 运行完整分析并生成图表")
    print("3. 查看 README.md 了解更多使用方法")
