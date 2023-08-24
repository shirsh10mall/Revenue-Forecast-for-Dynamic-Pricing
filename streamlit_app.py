import streamlit as st
import joblib
import pickle
import pandas as pd 
import json
# from xgboost import XGBRegressor
import xgboost as xgb
from xgboost import DMatrix
# from shap import initjs
# from shap import force_plot
# from shap import summary_plot
# from shap import TreeExplainer
# from shap import getjs
# from st import components


# path = "C:\Users\shirs\Desktop\Revenue_Forecast_for_Dynamic_Pricing\Web_App"
with open(r'./group_values_list.json', 'r') as file:
    group_values_list = json.load(file)
group_values_list=list(group_values_list)

with open(r'./unit_list.json', 'r') as file:
    unit_list = json.load(file)
unit_list=list(unit_list)

with open(r'./pharmForm_list.json', 'r') as file:
    pharmForm_list = json.load(file)
pharmForm_list = list(pharmForm_list)

with open(r'./content_list.json', 'r') as file:
    content_list = json.load(file)
content_list = list(content_list)

with open(r'./salesIndex_list.json', 'r') as file:
    salesIndex_list = json.load(file)
salesIndex_list = list(salesIndex_list)

model = xgb.Booster()
model.load_model(r"./xgboost_model.json")


def convert_content_column_into_numbers(item):
    try:
        return float(item)
    except:
        # extract numbers seperated by alphabet (using regex)
        import re
        item = re.findall(r'\d+\.?\d*', item)
        # multiply the numbers to get the final number
        final_number = 1
        for i in item:
            final_number = final_number*float(i)
        return final_number


def show_predict_page():
    
    st.write("""# Revenue Forecast for Dynamic Pricing """)
    st.write("""### Enter information for prediction """)        
    
    adFlag = st.selectbox('Advertising Flag | Product is part of an advertising campaign or not?', options=["Yes", "No"]  )
    if adFlag == "Yes":
        adFlag = 1
    else:
        adFlag = 0

    availability = st.selectbox('Availability Status ', options=[1,2,3,4] )
    
    click = st.selectbox('Click Flag ', options=["Yes","No"] )
    if click == "Yes":
        click = 1
    else:
        click = 0

    basket = st.selectbox('Shopping Basket Flag ', options=["Yes","No"] )
    if basket == "Yes":
        basket = 1
    else:
        basket = 0
    
    order = st.selectbox('Purchase Flag ', options=["Yes","No"] )
    if order == "Yes":
        order = 1
    else:
        order = 0

    genericProduct = st.selectbox('Generic Flag ', options=["Yes","No"] )
    if genericProduct == "Yes":
        genericProduct = 1
    else:
        genericProduct = 0

    group = st.selectbox('Product Group ', options=group_values_list )
    group = int( group_values_list.index(group) )
    content = st.selectbox('Product Content ', options=content_list )
    content = convert_content_column_into_numbers(content)
    unit = st.selectbox('Unit ', options=['G', 'P', 'ST', 'CM', 'M', 'ML', 'KG', 'L'] )
    unit = int( unit_list.index(unit) )
    pharmForm = st.selectbox('Dosage Form ', options=pharmForm_list )
    pharmForm = int( pharmForm_list.index(pharmForm) )
    salesIndex = st.selectbox('Dispensing Regulation Code ', options=salesIndex_list )
    salesIndex = int( salesIndex_list.index(salesIndex) )

    # campaignIndex = st.selectbox('Campaign Action Label ', options=["A", "B", "C"] )

    day = st.slider( 'Day in the observed time period ', 1, 92)
    competitorPrice = st.slider( 'Lowest Competitor Price ', 0.5, 126.0, 0.1)
    price = st.slider( 'Product Price', 0.0, 380.0, 0.1 )
    manufacturer = st.slider( 'Manufacrurer ID ', 0, 1067 )
    category = st.slider( 'Main Shopping Catagory ID ', 1, 48 )
    rrp = st.slider( 'Reference', 0.0, 405.0, 0.1 )
    
    ok = st.button("Predict")
    
    columns_name = ['day', 'adFlag', 'availability', 'competitorPrice', 'click', 'basket',
       'order', 'price', 'revenue', 'manufacturer', 'group', 'content', 'unit',
       'pharmForm', 'genericProduct', 'salesIndex', 'category', 'rrp']
       # 'campaignIndex'

    values = { "day":[day], "adFlag":[adFlag], "availability":[availability], "competitorPrice":[competitorPrice], "click":[click], "basket":[basket], "order":[order], 
               "price":[price], "manufacturer":[manufacturer], "group":[group], "content":[content], "unit":[unit], "pharmForm":[pharmForm], "genericProduct":[genericProduct], "salesIndex":[salesIndex], "category":[category], "rrp":[rrp] } # "campaignIndex":[campaignIndex],

    df = pd.DataFrame(values)
    DM_df = DMatrix(df)

    # values = [  day, adFlag, availability, competitorPrice, click, basket,
    #    order, price, manufacturer, group, content, unit,
    #    pharmForm, genericProduct, salesIndex, category, rrp]

    if ok:
    
        predictions = model.predict(DM_df)

        st.write("#### Predicted Revenue : "+str( predictions[0] ) )

        # # plot the force plot in streamlit in API
        # def st_shap(plot, height=None):
        #     shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
        #     components.html(shap_html, height=height)

        # st.write("""### Explainable AI (using Shap)""")  
        # shap_values = shap.TreeExplainer(model).shap_values(data)
        
        # st_shap(shap.summary_plot(shap_values, data, plot_type="bar") )

        # # shap.initjs()
        # st_shap(shap.force_plot(shap.TreeExplainer(final_model).expected_value[0], shap_values[0][:], data))

show_predict_page()