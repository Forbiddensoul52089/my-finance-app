import streamlit as st
import pandas as pd
import numpy as np

# 设置网页标题
st.set_page_config(page_title="18岁非对称跨越：财富增长模拟器", layout="wide")

st.title("🚀 18岁非对称跨越：财富模拟系统")
st.markdown("---")

# 侧边栏：输入个人资料与财务数据
with st.sidebar:
    st.header("👤 个人及财务设置")
    name = st.text_input("您的姓名", value="未来架构师")
    age = st.number_input("当前年龄", min_value=1, max_value=100, value=18)
    
    st.markdown("---")
    savings = st.number_input("当前储蓄金额 (RM)", value=1000.0)
    investment = st.number_input("计划投资金额 (RM)", value=5000.0)
    rate = st.slider("预期年化收益率 (%)", 0.0, 50.0, 10.0) / 100
    years = st.slider("预测年限", 1, 40, 20)

# 核心计算逻辑
def calculate_wealth_curve(principal, rate, years):
    # 生成每年的财富数据
    data = []
    for year in range(years + 1):
        amount = principal * ((1 + rate) ** year)
        data.append(amount)
    return data

# 执行计算
savings_curve = calculate_wealth_curve(savings, 0.03, years) # 固定储蓄利率 3%
investment_curve = calculate_wealth_curve(investment, rate, years)

# 数据整合用于图表
chart_data = pd.DataFrame({
    '年份': list(range(years + 1)),
    '银行储蓄 (3%)': savings_curve,
    'AI系统投资': investment_curve
})

# 页面布局展示
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📊 {years}年后财富预测")
    st.metric("最终投资价值", f"RM {investment_curve[-1]:,.2f}", delta=f"{rate*100:.1f}% 利率")
    st.write(f"你好 {name}，根据你的设置，到 {age + years} 岁时，你的投资资产将增长到极具规模的水平。")

with col2:
    st.subheader("📈 财富增长曲线")
    st.line_chart(chart_data.set_index('年份'))

# 商业引导 (之前提到的电子书引导)
st.info("💡 **想知道如何通过 AI Agent 实现非对称收益？** 在 IG 私信我 'START' 获取完整电子书指南。")