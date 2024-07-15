'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    '''我的兴趣推荐'''
    # 学生使用write()、image()、audio()等自行发挥
    #with open('霞光.mp3','rb') as f:
        #mymp3 = f.read()
    #st.audio(mymp3, format = 'audio/mp3', start_time=0)
    st.image('slogan.png')
    st.write('陈辰的电影推荐')
    st.write('----------------------------------')
    st.write('陈辰的游戏推荐')
    st.write('----------------------------------')
    st.write('陈辰的书籍推荐')
    st.write('----------------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片换色小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name = uploaded_file
        file_type = uploaded_file
        file_size = uploaded_file
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(image_change(img,0,2,1))
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3','改色4'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
            

def page_3():
    '''我的智能词典'''
    st.write('智能词典')
    with open('words_space.txt','r' , encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0])],i[2]
    
        

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('words_space.txt','r' , encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messagse_list = messagse_list[i].split('#')
    for i in messagse_list:
        if i [1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
             with st.chat_message('🍥'):
                 st.write(i[1],':',i[2])
    name = st.selectbox('我是.....',['阿短','编程猫'])
    new_message = st.text_input('想要说的话')
    if st.button('留言'):
        messagse_list.append([str(int(messagse_list[-1][0]+1)),name,new_message])
        with open('leave_message.txt', 'w' , encoding = 'utf-8') as f:
            message = ''
        for i in messagse_list:
            messagse_list += i[0] + '#' + i[1] + '#' + i[2] + '\n'
        message = message[:-1]
        f.write(message)
    

#if page == '我的兴趣推荐':
    page_1()
#elif page == '我的图片处理工具':
    page_2()
#elif page == '我的智能词典':
    page_3()
#elif page == '我的留言区':
    page_4()
def image_change(img,r_c,g_c,b_c):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img