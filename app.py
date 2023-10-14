# import streamlit as st

# st.title('Title -> GeeksForGeeks')                      # Title
# st.header('Header -> GeeksForGeeks')                    # Header
# st.subheader('Subheader -> GeeksForGeeks')              # SubHeader
# st.text('Text -> GeeksForGeeks')                        # Text

# st.markdown('# Hi')                                     # Markdown

# st.success('Success!')                                  # Success
# st.info('Information!')                                 # Info
# st.warning('Warning!')                                  # Warning
# st.error('Error!')                                      # Error
# st.exception(ZeroDivisionError('Div not possible'))     # Exception

# st.subheader('Help')
# st.help(ZeroDivisionError)                              # Help

# st.subheader('Write')
# st.write("range(1,10)")                                 # Write
# st.write(range(1,10))
# st.write(1*2*3)

# st.subheader('Code')
# st.code('x = 10\n'                                      # Code
#         'for i in range(x):\n'
#         '\tprint(i)')

# st.subheader('Checkbox')
# st.checkbox('Male')                                     # Checkbox
# if(st.checkbox('Adult')):                               # Checkbox with Validation
#     st.write("You're an adult!")


# st.subheader('Radio Button')                            # Radio Button
# radioButton = st.radio('Select : ', ('Male','Female','Other'))
# if(radioButton == 'Male'):
#     st.write("You're a Male")
# elif(radioButton == 'Female'):
#     st.write("You're a Female")
# elif(radioButton == 'Other'):
#     st.write("You're an Other Gender")

# st.subheader('Select Box')                              # SelectBox
# selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
#                                                 'Deep Learning','Natural Language Processing',
#                                                 'Computer Vision','Image Processing'])
# st.write("You've selected : ", selectBox)

# st.subheader('MultiSelect Box')                         # MultiSelectBox
# multiSelBox = st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
#                                                     'Deep Learning','Natural Language Processing',
#                                                     'Computer Vision','Image Processing'])
# st.write("You've selected : ", len(multiSelBox) , 'courses')

# st.subheader("Button")                                  # Button
# if(st.button('Click me')):
#     st.write('Thanks for clicking me')

# st.subheader("Slider")                                  # Slider
# vol = st.slider('Select the volume',0,100,step = 1)
# st.write('Volume is : ',vol)

# st.subheader("Text Input")                              # Text-Input
# username = st.text_input('Username : ')
# password = st.text_input('Password : ', type = 'password')

# st.subheader("Text Area")                              # Text-Area
# st.text_area('Write something interesting about yourself')

# st.subheader("Input Number")                           # Input-Number
# st.number_input('Select your age',18,110)

# st.subheader("Input Date")                              # Input-Date
# st.date_input('Date')

# st.subheader("Input Time")                              # Input-Time
# st.time_input('Time')


import streamlit as st

st.title("Title -> GeeksForGeeks")              # Title
st.header("Header -> GeeksForGeeks")            # Header
st.subheader("Subheader -> GeeksForGeeks")      # SubHeader
st.text("Text -> GeeksForGeeks")                # Text


st.markdown('Hi')                               # Markdown
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('###### Hi')


st.success('Data is Submitted!')                            # Success
st.info("Information!")                                     # Info
st.warning("Warning!")                                      # Warning
st.error("Error!")                                          # Error
st.exception(ZeroDivisionError("Division not possible"))    # Exception

st.help(ZeroDivisionError)                                  # Help

st.write("range(1,10)")                                     # write
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x = 10\n'                                          # code
        'for i in range(x):\n'
        '    print(i)\n')

st.checkbox('Male')                                         # checkbox

if(st.checkbox('Adult')):                                   # checkbox with validation
    st.write("You're an Adult")


# radiobutton
radioButton = st.radio('Select : ', ('Male','Female','Other'))  

if(radioButton == 'Male'):
    st.write("You're a Male")
elif(radioButton == 'Female'):
    st.write("You're a Female")
elif(radioButton == 'Other'):
    st.write("You're an Other gender")


st.subheader('Select Box')                                  # Select Box
selectBox = st.selectbox('Data Science : ', ['Data Analysis','Web Scraping','ML','DL','NLP','Image Processing'])


st.write("You've selected : ",selectBox)

st.subheader('Multiselect Box')                             # Multiselect Box

multiselectBox = st.multiselect('Data Science : ', ['Data Analysis','Web Scraping','ML','DL','NLP','Image Processing'])

st.write("You've selected : ", len(multiselectBox), 'courses')


# creating a button
st.subheader('Button')
# st.button('Click Me')

if(st.button('Click Me')):
    st.write('Thanks for clicking the button')


# slider
st.subheader('Slider')
vol = st.slider('Select the volume',1,100,step = 1)
st.write('Volume is : ',vol)


# taking input from the user
st.subheader('Text Input')
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

# text area
st.subheader("Text Area")
textArea = st.text_area("Write something interesting about yourself in 20 characters", height = 20, max_chars = 20)
st.write(textArea)

# input a number
st.subheader('Input Number')
st.number_input('Select your age',18,100)

# input a date
st.subheader('Input Date')
st.date_input('Date')

# input a time
st.subheader('Input Time')
st.time_input('Time')