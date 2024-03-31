# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st

from langchain.chat_models import ChatOpenAI
# from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

st.title('Q 킴의 Chat GPT 시 써주는 집')
st.title('아래에 원하는 시상을 적어 주세요 ~ :blue[cool] :sunglasses:')

content = st.text_input('원하시는 시상을 써봐', ' ')

if st.button('입력된 내용으로 시 읋기'):
    with st.spinner('시를 쓰고 있습니다...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")   
        st.write(result)


# result = chat_model.invoke(content + "에 대한 시를 써줘")   
# print(result)






