import streamlit as st

st.title("Streamlit Function Showcase")

st.header("This demostrate multiple streamlit function")

#----input section---

name = st.text_input("Enter your name:")

age = st.number_input("Enter yor age:",min_value=18, max_value=50)

hobby = st.text_area("What are your hobbies?")

gender  = st.radio("Select your gender:", ["Male","female", "other"])

skills = st.multiselect( "select your skills: " ,["python", "Excel","SQl","Communication"])
                        
accept = st.checkbox("I accept the terms and conditions")

level = st.slider ("Rate your streamlit knowlege(1-10): " , 1, 10)

file = st.file_uploader("upload your resume (PDF): ")



#-----Button--------


if st.button("submit"):
    if not accept:
        st.warning("please accept the terms and conditon to continue")

    else:
        st.success("form submitted")
        st.write(f"Hello,{name}!")
        st.info (f"Age: {age}")
        st.write(f"Gender: {gender}")
        st.write(f"your hobbies: \n{hobby}")
        st.write(f"skills {','.join(skills)}")
        st.write(f"knowledge level: {level} / 10 ")
        if file:
            st.download_button("Download Resume", file.read(), file.name)

