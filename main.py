import streamlit as sl
import function as fn
todos = fn.get_todos()
def add_todo():
    todo = sl.session_state['new_todo']
    todos.append(todo+'\n')
    fn.write_todos(todos)


sl.title("To-Do Web App")
sl.subheader("This is my Todo web app")
for index,todo in enumerate(todos):
    checkbox = sl.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()


sl.text_input(label='',placeholder="Enter a To-Do",
              on_change=add_todo, key='new_todo')
