# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Customize Your Smoothi :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothi
    """
);

option = st.selectbox(
    'What is your favorite fruite?',
    ('Banana', 'Strawberries', 'Peaches'))

st.write('Your favirite fruit is:', option);

import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("Customize Your Smoothie:cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie
    """)
name_on_order = st.text_input('Name on Smoothie')
st.write('The name uon your Smoothie will be:', name_on_order)
cnx =st.connection("snowflake")
session = cnx.session()
my_dataframe =session.table("smoothies.public.fruit_options").select (col('Fruit_Name'))
#st.dataframe(data=my_dataframe,use_container_width=True)

ingredients_list= st.multiselect (
 'choose up to 5 ingredients:' 
   ,my_dataframe 
)
if ingredients_list :
    st.write(ingredients_list)
    st.text(ingredients_list)
    
    ingredients_string=''
    for fruit_choosen in ingredients_list:
        ingredients_string +=fruit_choosen +' '
  #st.write(ingredients_string )
     
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

   #st.write(my_insert_stmt)
    time_to_insert =st.button('Submit Order')
    if ingredients_string :
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅");
