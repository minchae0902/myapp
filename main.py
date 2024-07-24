import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# Load the CSV file
file_path = '202406_202406_연령별인구현황_월간.csv'
data = pd.read_csv(file_path, encoding='cp949')

# Function to calculate the percentage of middle school age population
def calculate_middle_school_percentage(region):
    region_data = data[data['행정구역'].str.contains(region)]
    total_population = region_data['2024년06월_계_총인구수'].str.replace(',', '').astype(int).sum()
    middle_school_population = region_data[['2024년06월_계_12세', '2024년06월_계_13세', '2024년06월_계_14세']].replace(',', '', regex=True).astype(int).sum().sum()
    
    middle_school_percentage = (middle_school_population / total_population) * 100
    return middle_school_population, total_population, middle_school_percentage

# Streamlit app
st.title('지역별 중학생 인구 비율')

region = st.text_input('지역을 입력하세요:', '서울특별시')

if region:
    middle_school_population, total_population, middle_school_percentage = calculate_middle_school_percentage(region)
    
    labels = ['중학생 인구', '기타 인구']
    sizes = [middle_school_population, total_population - middle_school_population]
    colors = ['#ff9999','#66b3ff']
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    
    st.pyplot(fig1)
    st.write(f"{region}의 총 인구: {total_population}명")
    st.write(f"{region}의 중학생 인구: {middle_school_population}명")
    st.write(f"{region}의 중학생 인구 비율: {middle_school_percentage:.2f}%")
