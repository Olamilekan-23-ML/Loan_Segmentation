# Importing Dependencies
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Loading Model
kmeans = pickle.load(open('kmeans.pkl','rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl','rb'))

# Label Encoding
job_encoder = encoders['job']
marital_encoder = encoders['marital']
binary_encoder = {'default':{'no':0,'yes':1},
            'housing':{'no':0,'yes':1},
            'loan':{'no':0,'yes':1}
            }

# Form Page 
st.title("🔍 Customer Loan Profile Analyzer")
st.markdown('### Identify which loan products to offer to different customer segments')
st.markdown('---')
st.subheader('👤 Personal Information')
col1, col2 = st.columns(2)
with col1:
    age = st.number_input('**Age**',
                          min_value=18,
                          max_value=100, 
                          value=35,
                          help="Customer's age in years"
                          )
    job = st.selectbox('**Job**',
                       job_encoder.classes_,
                       index = None,
                       help="Type of job or profession")
with col2:    
    marital = st.selectbox('**Marital Status**', 
                           marital_encoder.classes_,
                           index = None,
                           help='Current Marital Status')
    default = st.radio('**Credit Default History**',
                        ['No', 'Yes'], 
                        index = None,
                        help="Has the customer ever defaulted on credit payments?"
                        )
st.markdown('---')
st.subheader("💰 Financial Information")
col1, col2 = st.columns(2)
with col1:
        balance = st.number_input(
            '**Account Balance (€)**', 
            min_value=0.00, 
            max_value=1000000.00, 
            value=1000.0,
            help="Average yearly balance in euros"
        )
        
        housing = st.radio(
            '**Housing Loan**', 
            ['No', 'Yes'], 
            index=None,
            help="Does the customer have an existing housing loan?"
        )
with col2:
     loan = st.radio(
            '**Personal Loan**', 
            ['No', 'Yes'], 
            index = None,
            help="Does the customer have an existing personal loan?"
        )
st.markdown("---")
st.subheader("📞 Campaign Information")
col1, col2 = st.columns(2)
with col1:
     campaign = st.number_input(
            '**Campaign Contacts**', 
            min_value=1, 
            max_value=50, 
            value=2,
            help="Number of contacts performed during this campaign"
        )
     duration = st.number_input(
            '**Last Call Duration (seconds)**', 
            min_value=0, 
            max_value=2000, 
            value=300,
            help="Duration of the last contact in seconds"
        )
with col2:
        previous = st.number_input(
            '**Previous Campaign Contacts**', 
            min_value=0, 
            max_value=50, 
            value=0,
            help="Number of contacts performed before this campaign"
        )
# Encode input  
def encoder_input():
    return [
              float(age),
              job_encoder.transform([job])[0],
              binary_encoder['default'][default.lower()] if default else 0,
              float(balance),
              binary_encoder['housing'][housing.lower()] if housing else 0,
              binary_encoder['loan'][loan.lower()] if loan else 0,
              float(campaign),
              float(duration),
              marital_encoder.transform([marital])[0],
              float(previous)
              ]
st.markdown('---')
# Prediction
predict = st.button("🔍 Predict Segment", type="secondary", use_container_width=True)
if predict:
       input_encoder = encoder_input()
       input_scaled = scaler.transform([input_encoder])
       cluster = kmeans.predict(input_scaled)[0]
       st.success(f"✅ Customer belongs to **Segment {cluster}**")
       
# Show Customer summary
       st.subheader("📊 Customer Summary")
# Show metrics display
       col1, col2, col3 = st.columns(3)
       with col1:
        st.metric("🎂 Age", f"{age} years")
        st.metric("👔 Occupation", job)
        with col2:
              st.metric("💍 Marital Status", marital)
              st.metric("🏠 Housing Loan", housing)
        with col3:
              st.metric("💰 Balance", f"€{balance}")
# Detailed segment information                
              st.subheader("🎯 Recommended Loan Strategy")
# Cluser Information              
              cluster_info = {
                    0: {
            "name": "High-Value Professionals",
            "icon": "🏆",
            "description": "Customers with high balances, no existing loans, and stable jobs.",
            "strategy": "🎯 **Primary Target** - Personal loans, credit cards, premium credit lines",
            "risk": "Very Low",
            "color": "green" 
            },
            1: {
            "name": "At-Risk Customers",
            "icon": "⚠️",
            "description": "Customers with negative balances, defaults, and multiple existing loans.",
            "strategy": "⚠️ **Low Priority** - Financial counseling, debt consolidation, not new loans",
            "risk": "High",
            "color": "red"
            },
            2: {
            "name": "Homeowners",
            "icon": "🏠",
            "description": "Customers with housing loans, good balances, and high engagement.",
            "strategy": "🏠 **Medium Priority** - Home equity loans, home improvement financing",
            "risk": "Low",
            "color": "blue"
            },
            3: {
            "name": "Personal Loan Holders",
            "icon": "📊",
            "description": "Customers with personal loans, moderate balances, and clean credit.",
            "strategy": "📊 **Medium Priority** - Debt consolidation, refinancing, balance transfers",
            "risk": "Low-Medium",
            "color": "orange"
            }
            }              
              info = cluster_info.get(cluster, {
                    "name": "Unknown",
                    "icon": "❓",
                    "description": "Please review this customer profile manually.",
                    "strategy": "Review profile before making recommendations",
                    "risk": "Unknown",
                    "color": "gray"
                    })
# Display Segment info with appropraite Color
              if cluster == 0:
                    st.success(f"**{info['icon']} {info['name']}**")
              elif cluster == 1:
                   st.error(f"**{info['icon']} {info['name']}**")
              elif cluster == 2:
                   st.info(f"**{info['icon']} {info['name']}**")
              else:
                   st.warning(f"**{info['icon']} {info['name']}**")
                   st.markdown(f"**Description:** {info['description']}")
                   st.markdown(f"**Recommended Strategy:** {info['strategy']}")
                   st.markdown(f"**Risk Level:** {info['risk']}")
