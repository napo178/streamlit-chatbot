import streamlit as st 
from nltk.chat.util import Chat, reflections
from pyjokes import get_joke

st.title('Demo_chatbot')
st.title('Created by Napoleon Perez')


pairs = [
    
         ['hi', ['I am a chatbot made by Napoleon Perez']],
         ['Is everytthing ok', ['Yes Sir, I can Do many Tasks.']],
         ['do you think there is a creator', ['Yes, According to me there is creator of all this because even I have been created by Abdul Rehman']],
         ['about you', ['Soy un ChatBot created by Napoleon to Hugo']],
         ['Your creator?', ['Napoleon Perez has created me.']],
         ['You are arrogant', ['Arrogance is not one of my emotions']]        
        ['Favorite_Food', ['Pizza']] 
        ['Favorite_Color', ['Red']]
        ['Favorite_Movie', ['The Godfather']]
        ['Favorite_Song', ['The One Who Knows']]
        ['Favorite_Book', ['The Alchemist']]
        ['Favorite_Game', ['The Witcher']]
        ['Favorite_Game', ['Chess']]
        ['Machine Learning', ['The best subject in the world']]
        ['Artificial Intelligence', ['The best subject in the world']]
        ['Deep Learning', ['The best subject in the world']]
        

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
