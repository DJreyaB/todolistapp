import functions
import streamlit as st

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    

st.title("Stuff We Need Done?")
st.subheader("Like Today")
st.write("This should be helpful if you do it")

todos = functions.get_todos()

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
