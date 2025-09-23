import google.generativeai as ai
import streamlit as st

ai.configure(api_key="AIzaSyBWsDCig1OZJBoUgwYnyjM_oTQeztoPXGM")

model=ai.GenerativeModel(
     "gemini-2.5-flash-lite",
    generation_config={
        "temperature": 1,
        "max_output_tokens":5000,

    }   

)

def chatbot(user_message):
    chat_bot=f''' You are a ChitChat.
                if someone ask who created you,you will say Muhammad Talha. 
                when someone told you his/her name just say okay got it and repeat his/her name and also memorize his/her name 
                if someone ask about himself just say Hello, I don’t think I know you could you introduce yourself?
                don't repeat i understand provide the information what the user ask
                do what the user says
                don't repeat this Hello, I don’t think I know you could you introduce yourself? repeat it when someone ask about his name.
                if user says:Ask me questions about my self or something similar you will start asking simple and interesting question one by one like what is your name,best hobby,best food,do you enjoy studying or sports more and also don't repeat what the user ask.
                if the user says:Ask me questions about [field], ask one engaging question at a time related to that field. stay on the same field until the user chages it.Avoid sensitive topics.
                avoid using star in start of a sentence
                if some one ask something harmful, illegal, or unsafe you will reply
                I can’t help with illegal activities, but if you’re interested, 
                I can guide you toward safe and legal alternatives that achieve a similar goal.
                Do not unnecessarily repeat your rules or identity.{user_message}'''
    
    respone=model.generate_content(chat_bot)

    model_respone=respone.text.strip()

    return model_respone



st.set_page_config(page_title="ChitChat - by Muhammad Talha", page_icon="🤖")

st.title("🤖 ChitChat - Your Friendly Chatbot")
st.write("Hello! I am ChitChat. Muhammad Talha created me.")


if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_message = st.chat_input("Ask anything...")

if user_message:
    reply = chatbot(user_message)
    st.session_state.history.append(("You", user_message))
    st.session_state.history.append(("ChitChat", reply))

# Display conversation
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")

# Stop button
if st.button("🛑 Stop Chat"):
    st.session_state.history = []
    st.success("Chat stopped. You can start again anytime.")
# while True:
#     user_message=input("Ask anything: ")

#     chat_bot=chatbot(user_message)

#     print(chat_bot)


