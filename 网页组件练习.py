'''我的主页'''
import streamlit as st
import time
page = st.sidebar.radio('我的首页', ['进度条', '滑块开关', '跳转按钮', '单选框','滑动条','勾选框','页面布局','标题样式'])

def page_1():
    # 进度条st.progress(百分比，标题)
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i,'正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    # 如何创建组件？
    # 创建组件之后如何调用组件实现效果？
    # 两个参数的作用分别是？
    # 应用：词典_单词记忆挑战
    words_lst = ['fruit：水果', 'apple：苹果', 'banana：香蕉', 'orange：橘子']
    
    words = st.progress(0, '准备开始单词记忆挑战！')
    for i in range(4, 0, -1):
        time.sleep(3)
        words.progress(i*25, words_lst[-i])
    time.sleep(3)
    words.progress(0, '开始猜词吧！')
    st.write('刚才出现的单词是？他们的意思是？')
    

def page_2():
    # 滑块开关st.toggle()
    my_open = st.toggle('开关')
    if my_open:
        st.write('开启')
    else:
        st.write('关闭')
    
    # 如何创建组件？
    # 创建组件之后如何通过判断实现效果？
    
    # 应用：图片_功能判断开关
    ch = st.toggle('反色滤镜')
    bw = st.toggle('黑白滤镜')
    co = st.toggle('增强对比度')
    
    message = ''
    if ch:
        message += '反色' + ','
    if bw:
        message += '黑白' + ','
    if co:
        message += '增强对比度'
    st.write('你将会得到一张', message, '的图片')

def page_3():
    # 跳转按钮link_button(标题文本，跳转链接)
    st.link_button('百度首页', 'https://www.baidu.com/')
    
    # 如何创建跳转按钮
    # 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？
    
    # 应用：兴趣推广_分享链接指引
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

def page_4():
    # 单项选择框st.radio()
    choice = st.radio(
        '选择：',
        ['选项1', '选项2', '选项3'],
        captions=['这是第一个选项', '这是第二个选项', '这是第三个选项']
    )
    
    # 如何创建单选框？
    # 单选框中的两个必填参数分别是？都有什么作用？
    # captions参数的作用是？
    
    # 应用：游戏_数据模拟器
    st.write('----')
    level = st.radio(
        '选择游戏难度：',
        ['普通', '困难', '地狱'],
        captions=['怪物血量为100%,攻击力为100%', '怪物血量为200%,攻击力为150%', '怪物血量为300%,攻击力为200%']
    )
    hp = 100
    damage = 10
    if level == '困难':
        hp = 200
        damage = 15
    elif level == '地狱':
        hp = 300
        damage = 20
    st.write('怪物血量：', hp, '，怪物攻击力：', damage)
def page_5():
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
def page_6():
    # 滑动条st.slider()
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)
    
    # 如何创建勾选框？
    # 勾选框更适合单选还是多选？
    # 勾选框的返回值是选框中的字符串吗？不是的话，返回值是什么？
    
    # 应用：宣传_互联网知识
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，下面就让我来讲讲吧！')

def page_7():
    st.write('下面哪些小程序可以被嵌入网页中？')
    col1, col2 = st.columns([2, 1])
    with col1:
        cb1 = st.checkbox('A.turtle绘图作品A.turtle绘图作品A.turtle绘图作品')
        col3, col4 = st.columns([1, 1])
        with col3:
            cb2 = st.checkbox('C.图片处理工具')
        with col4:
            cb3 = st.checkbox('随便吧')
    with col2:
        cb4 = st.checkbox('D.pygame小游戏')
        cb5 = st.checkbox('E.Turtle小游戏')
    
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')
    st.write('下面哪些小程序可以被嵌入网页中？')
    col5, col6 = st.columns([1, 1])
    with col5:
        st.write('下面哪些小程序可以被嵌入网页中')
    with col6:
        st.write('下面哪些小程序可以被嵌入网页中？')
def page_8():
    st.title('这是一个大标题')  
    st.header('这是一个次大标题')  
    st.subheader('这是一个中等大小的标题')  
      
    # 使用 st.markdown 设置不同的HTML标签来定义字号  
    st.markdown('# 这是一个大标题')  
    st.markdown('## 这是一个次大标题')  
    st.markdown('### 这是一个中等大小的标题')  
      
    # 使用 st.markdown 自定义 CSS 样式设置字号  
    st.markdown('<h1 style="font-size:48px;">这是一个自定义字号的大标题</h1>', unsafe_allow_html=True)  
    st.markdown('<h2 style="font-size:36px;">这是一个自定义字号的次大标题</h2>', unsafe_allow_html=True)  
    st.markdown('<h3 style="font-size:24px;">这是一个自定义字号的中等标题</h3>', unsafe_allow_html=True)  

if page == '进度条':
    page_1()
elif page == '滑块开关':
    page_2()
elif page == '跳转按钮':
    page_3()
elif page == '单选框':
    page_4()
elif page == '滑动条':
    page_5()
elif page == '勾选框':
    page_6()
elif page == '页面布局':
    page_7()
elif page == '标题样式':
    page_8()
