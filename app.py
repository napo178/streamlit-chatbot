import streamlit as st 
from nltk.chat.util import Chat, reflections
from pyjokes import get_joke


pairs = [
    
         ['hi', ['Hola soy un chatbot en que te puedo ayudar']],
         ['Has tenido un problema con tu orden', ['Yes Sir, I can Do many Tasks.']],
        #  ['open (.*)', ['Sorry Sir, I cant open %1 .I am still a Chatbot. I cant automate things.', webbrowser.open('%1')]],
         ['do you think there is a creator', ['Yes, According to me there is creator of all this because even I have been created by Abdul Rehman']],
         ['acerca de ti', ['Soy un ChatBot created by Napoleon to Hugo']],
    
         ['Quien te creo?', ['Napoleon Perez has created me.']],
         ['Que es Hugo', ['Mi delivery app Favorita']]

            
]  


st.title("Rule based Chatbot")
st.subheader("This is a Rule based Chatbot demo ")


def main():
    st.write("El Bot inicia diciendo Hi ")
    ref = st.text_input("Comience su chat")

    # a = st.text_input("Initialize your Conversation By Typing Hi")
    # chat.converse()
    chat = Chat(pairs, reflections)
    respo = chat.respond(ref)
    st.write(respo)

if __name__=="__main__":
    main()
