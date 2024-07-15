'''滑动条_应用'''
import streamlit as st

# 滑动条st.slider()
number1 = st.slider('数据1：', 1, 100, 50)
number2, number3 = st.slider('数据2和3：', 1, 10, (4, 6))
st.write('数据1：', number1)
st.write('数据2-3：', number2, '-', number3)

# 如何创建滑动条？
# 滑动条中可以有几个数据点？

# 应用：留言_显示范围控制
st.write('----')
msg_lst = ['留言1', '留言2', '留言3', '留言4', '留言5', '留言6', '留言7', '留言8']
begin, end = st.slider('选择显示的留言信息：', 1, len(msg_lst), (1, len(msg_lst)))
for i in range(begin-1, end):
    st.write(msg_lst[i])