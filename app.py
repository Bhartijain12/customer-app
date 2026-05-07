import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Analytics", layout="wide")

st.title("📊 Customer Shopping Behavior Analysis")
st.markdown("---")

# Load data
df = pd.read_csv("customer_shopping_behavior.csv")

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
selected_category = st.sidebar.multiselect(
    "Category", 
    df['Category'].unique(), 
    default=df['Category'].unique()
)

# Filter
filtered_df = df[df['Category'].isin(selected_category)]

# Key metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", filtered_df['Customer ID'].nunique())
col2.metric("Total Revenue", f"${filtered_df['Purchase Amount (USD)'].sum():,.0f}")
col3.metric("Avg Purchase", f"${filtered_df['Purchase Amount (USD)'].mean():.0f}")
col4.metric("Avg Rating", f"{filtered_df['Review Rating'].mean():.1f}")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Revenue by Category")
    cat_revenue = filtered_df.groupby('Category')['Purchase Amount (USD)'].sum()
    st.bar_chart(cat_revenue)

with col2:
    st.subheader("👥 Revenue by Gender")
    gender_revenue = filtered_df.groupby('Gender')['Purchase Amount (USD)'].sum()
    st.bar_chart(gender_revenue)

# Subscription insight
st.subheader("📈 Subscription Impact")
sub_data = filtered_df.groupby('Subscription Status')['Purchase Amount (USD)'].mean()
st.dataframe(sub_data)
st.info("💡 Subscribed customers spend more per transaction")

st.markdown("---")
st.caption("Built with Streamlit | 3,900+ Transactions")