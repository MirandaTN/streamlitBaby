import streamlit as st
import os

st.set_page_config(page_title= "1st Streamlit", page_icon=":tada" ,layout="wide")

st.title("TestPrepTool")
st.subheader("Welcome to your FAV test prep tool :star:")

st.write("Your are required to create a folder for a subject, provide a descriptive name of the subject."+
         "Upload slides and study notes. Upon doing so, a quiz will be generated from the files you uploaded !! ")


# Function to create a folder
def create_folder(folder_name):
    try:
        os.makedirs(folder_name)
        st.success(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        st.error(f"Folder '{folder_name}' already exists.")

# Function to add a file to a folder
def add_file(folder_name, file):
    if file is not None:
        file_path = os.path.join(folder_name, file.name)
        try:
            with open(file_path, 'wb') as f:
                f.write(file.read())
            st.success(f"File '{file.name}' added to folder '{folder_name}' successfully.")
        except FileNotFoundError:
            st.error(f"Folder '{folder_name}' not found.")
        except FileExistsError:
            st.error(f"File '{file.name}' already exists in folder '{folder_name}'.")
    else:
        st.warning("Please select a file to upload.")

# Function to delete a file from a folder
def delete_file(folder_name, file_name):
    file_path = os.path.join(folder_name, file_name)
    try:
        os.remove(file_path)
        st.success(f"File '{file_name}' deleted from folder '{folder_name}' successfully.")
    except FileNotFoundError:
        st.error(f"File '{file_name}' not found in folder '{folder_name}'.")

# Streamlit UI

# Create Folder
st.header("Create Folder")
new_folder_name = st.text_input("Enter folder name:")
if st.button("Create Folder"):
    create_folder(new_folder_name)
    

# Select Folder for File Addition
    st.header("Add File to Folder")
selected_folder = st.selectbox("Select a folder:", os.listdir(), key="add_file_selectbox")
if selected_folder:
    uploaded_file = st.file_uploader("Choose a file:", type=["txt", "pdf", "jpg", "png"])
    if st.button("Add File"):
        add_file(selected_folder, uploaded_file)  

  
# Select Folder for File Deletion
    st.header("Delete File from Folder")
delete_folder = st.selectbox("Select a folder:", os.listdir(), key="delete_file_selectbox")
if delete_folder:
    files_to_delete = st.multiselect("Select files to delete:", os.listdir(delete_folder))
    if st.button("Delete Files"):
        for file_to_delete in files_to_delete:
            delete_file(delete_folder, file_to_delete)


