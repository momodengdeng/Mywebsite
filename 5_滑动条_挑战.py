'''滑动条_应用'''
import streamlit as st

# 滑动条st.slider()
number1 = st.slider('数据1：', 1, 100, 50)
number2, number3 = st.slider('数据2和3：', 1, 10, (4, 6))
st.write('数据1：', number1)
st.write('数据2-3：', number2, '-', number3)

# 如何创建滑动条？
# 滑动条中可以有几个数据点？

# 挑战：显示七色彩虹的一部分，如“红橙黄绿”、“黄绿蓝靛紫”……
st.write('----')
msg_lst = ['红', '橙', '黄', '绿', '蓝', '靛', '紫']
begin, end = st.slider('选择显示的彩虹：', 1, len(msg_lst), (1, len(msg_lst)))
message = ''
for i in range(____, ____):
    message += ____
st.write(message)