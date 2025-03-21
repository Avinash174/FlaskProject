import streamlit as st
import pandas as pd 
import math

st.title("Calculator")

st.write("### Input Data")
col1,col2=st.columns(2)
home_value=col1.number_input("Home Value",min_value=0,value=500000)
deposite=col1.number_input("Deposite",min_value=0,value=1000000)
interested_rate=col2.number_input("Interest Rate (in %)",min_value=0.0,value=5.5)
loan_term=col2.number_input("Loan Term (in year)",min_value=1,value=30)

#calculate the repayment 

loan_amount=home_value-deposite
number_of_payments=loan_term *12
monthly_interest_rate=(interested_rate/100)/12
monthly_payment=(loan_amount*(1+ monthly_interest_rate) ** number_of_payments)/((1+monthly_interest_rate)**number_of_payments-1)

# Display the repayment

total_payment=monthly_payment*number_of_payments
total_interset=total_payment-loan_amount
st.write("### Repayment")

col1,col2,col3=st.columns(3)
col1.metric(label="Monthly Repayment",value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Repayment",value=f"${total_payment:,.0f}")
col3.metric(label="Total Interest",value=f"${total_interset:,.0f}")

# create data frame with shedule 

schedule=[]
remaining_balance=loan_amount

for i in range(1,number_of_payments +1):
    interest_payment=remaining_balance * monthly_interest_rate
    principal_payment=monthly_payment-interest_payment
    remaining_balance -=principal_payment
    year=math.ceil(i/12)
    schedule.append(
        [
            i,
        monthly_payment,
        principal_payment,
        interest_payment,
        remaining_balance,
        year
        ]
    )
    df=pd.DataFrame(
        schedule,
        columns=["Months","Payments","Principle","Interest","Remaining Balance","Year"]
    )
    
# Display in data-frame chart
    
st.write("### payment Schedule")
payment_df=df[["Year","Remaining Balance",]].groupby("Year").min()
st.line_chart(payment_df)
    
