import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Employee Analytics Dashboard",
  page_icon="📊",
  layout = "wide")

st.title("Employee Analytics Dashboard")
df = pd.read_csv("employee.csv")

departments = ["All"] + sorted(df["department"].unique().tolist())

selected_departments = st.sidebar.selectbox( "Select Department", departments)
if selected_departments != 'ALL':
  filtered_df = df[df["department"] == selected_departments]
else:
  filtered_df = df


col1,col2 = st.columns(2)
col1.metric("Total Employees: ", len(filtered_df))
col2.metric("Average Salary: f"Rs{filtered_df["salary"].mean():,.0f}")


st.subheader("Employee Detail)
st.dataframe(filtered_df)


st.subheader("Average Salary by Department")
salary_by_department = filtered_df.groupby("department")["salary"].mean()
st.bar_chart(salary_by_department)



                                            
