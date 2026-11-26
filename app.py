
import streamlit as st
import pandas as pd

# تحميل البيانات
df = pd.read_csv('clean.csv')

# تنظيف قيم الفلاتر
df['City'] = df['City'].str.strip()
df['City'] = df['City'].replace('NaN', 'Unknown')

df['Weatherconditions'] = df['Weatherconditions'].str.strip()
df['Weatherconditions'] = df['Weatherconditions'].str.replace(
    'conditions ', '', regex=False
)
df['Weatherconditions'] = df['Weatherconditions'].replace('NaN', 'Unknown')

df['Road_traffic_density'] = df['Road_traffic_density'].str.strip()
df['Road_traffic_density'] = df['Road_traffic_density'].replace(
    'NaN', 'Unknown'
)

df['multiple_deliveries'] = df['multiple_deliveries'].fillna('Unknown')


# عنوان التطبيق
st.title("Delivery Time Dashboard")
st.write("Dashboard to explore delivery time and the factors affecting it.")


# Filters
st.sidebar.header("Filters")

city_options = ['All'] + list(df['City'].unique())
selected_city = st.sidebar.selectbox("City", city_options)

weather_options = ['All'] + list(df['Weatherconditions'].unique())
selected_weather = st.sidebar.selectbox("Weather", weather_options)

traffic_options = ['All'] + list(df['Road_traffic_density'].unique())
selected_traffic = st.sidebar.selectbox("Road Traffic", traffic_options)

delivery_options = ['All'] + list(df['multiple_deliveries'].unique())
selected_delivery = st.sidebar.selectbox("Multiple Deliveries", delivery_options)


# Apply filters
filtered_df = df.copy()

if selected_city != 'All':
    filtered_df = filtered_df[filtered_df['City'] == selected_city]

if selected_weather != 'All':
    filtered_df = filtered_df[filtered_df['Weatherconditions'] == selected_weather]

if selected_traffic != 'All':
    filtered_df = filtered_df[filtered_df['Road_traffic_density'] == selected_traffic]

if selected_delivery != 'All':
    filtered_df = filtered_df[filtered_df['multiple_deliveries'] == selected_delivery]


# Create tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Insights", "Product"])


# =========================
# Overview
# =========================
with tab1:

    st.header("Key Metrics")

    if len(filtered_df) > 0:

        col1, col2, col3, col4 = st.columns(4)

        avg_time = filtered_df['Time_taken(min)'].mean()
        avg_distance = filtered_df['distance_km'].mean()
        avg_rating = filtered_df['Delivery_person_Ratings'].mean()

        col1.metric(
            "Average Delivery Time",
            round(avg_time, 2) if pd.notna(avg_time) else "N/A"
        )

        col2.metric("Total Orders", len(filtered_df))

        col3.metric(
            "Average Distance (km)",
            round(avg_distance, 2) if pd.notna(avg_distance) else "N/A"
        )

        col4.metric(
            "Average Rating",
            round(avg_rating, 2) if pd.notna(avg_rating) else "N/A"
        )

    else:
        st.warning("No data available for the selected filters.")


# =========================
# Insights
# =========================
with tab2:

    st.header("Delivery Insights")

    if len(filtered_df) > 0:

        # Chart 1: Traffic
        traffic_avg = filtered_df.groupby(
            'Road_traffic_density'
        )['Time_taken(min)'].mean()

        st.subheader("Average Delivery Time by Road Traffic")
        st.bar_chart(traffic_avg)

        # Explanation
        if len(traffic_avg) > 0:
            st.write(
                f"Delivery time is highest during {traffic_avg.idxmax()} traffic "
                f"({traffic_avg.max():.2f} minutes) and lowest during "
                f"{traffic_avg.idxmin()} traffic "
                f"({traffic_avg.min():.2f} minutes)."
            )

        # Chart 2: Multiple Deliveries
        delivery_avg = filtered_df.groupby(
            'multiple_deliveries'
        )['Time_taken(min)'].mean()

        st.subheader("Average Delivery Time by Multiple Deliveries")
        st.bar_chart(delivery_avg)

        # Explanation
        if len(delivery_avg) > 0:
            st.write(
                f"Orders with {delivery_avg.idxmax()} multiple deliveries "
                f"have the highest average delivery time "
                f"({delivery_avg.max():.2f} minutes), while "
                f"{delivery_avg.idxmin()} has the lowest "
                f"({delivery_avg.min():.2f} minutes)."
            )

        # Chart 3: Order Hour
        filtered_df['Order_Hour'] = pd.to_datetime(
            filtered_df['Time_Orderd'],
            format='%H:%M:%S',
            errors='coerce'
        ).dt.hour

        hour_avg = filtered_df.groupby(
            'Order_Hour'
        )['Time_taken(min)'].mean()

        st.subheader("Average Delivery Time by Hour")
        st.line_chart(hour_avg)

        # Explanation
        if len(hour_avg) > 0:
            st.write(
                f"Delivery time is highest at {hour_avg.idxmax()}:00 "
                f"({hour_avg.max():.2f} minutes) and lowest at "
                f"{hour_avg.idxmin()}:00 "
                f"({hour_avg.min():.2f} minutes)."
            )


        # Key Findings and Recommendations
        st.header("أهم النتائج والتوصيات")

        st.subheader("أهم النتائج")

        st.write("""
        - يزداد وقت التوصيل مع ارتفاع كثافة حركة المرور، حيث سجلت حالة Jam أعلى متوسط.
        - الطلبات التي تحتوي على عدة توصيلات تستغرق وقتًا أطول، خصوصًا عند وجود 3 توصيلات.
        - أوقات التوصيل تكون أطول خلال ساعات المساء، خاصة حول الساعة 8 مساءً.
        """)

        st.subheader("التوصيات")

        st.write("""
        - مراعاة كثافة حركة المرور عند تقدير وقت وصول الطلب.
        - تنظيم الطلبات التي تحتوي على عدة توصيلات لتقليل التأخير.
        - توفير عدد أكبر من المندوبين خلال ساعات الذروة المسائية.
        """)

    else:
        st.warning("No data available for the selected filters.")


# =========================
# Product
# =========================
with tab3:

    # إضافة أداة تقدير وقت التوصيل
    st.header("Delivery Time Estimator")
    st.write("Estimate delivery time based on the selected factors.")

    # User inputs
    distance = st.number_input(
        "Distance (km)",
        min_value=1.0,
        max_value=21.0,
        value=5.0,
        step=1.0
    )

    weather = st.selectbox(
        "Weather",
        ['Sunny', 'Stormy', 'Sandstorms', 'Windy', 'Fog', 'Cloudy']
    )

    traffic = st.selectbox(
        "Road Traffic",
        ['Low', 'Medium', 'High', 'Jam']
    )

    deliveries = st.slider(
        "Multiple Deliveries",
        min_value=0,
        max_value=3,
        value=1
    )

    # Calculate estimated delivery time
    if distance <= 5:
        distance_time = 22.18
    elif distance <= 10:
        distance_time = 24.39
    elif distance <= 15:
        distance_time = 29.84
    else:
        distance_time = 29.87

    weather_time = {
        'Sunny': 21.86,
        'Stormy': 25.87,
        'Sandstorms': 25.88,
        'Windy': 26.12,
        'Fog': 28.92,
        'Cloudy': 28.92
    }

    traffic_time = {
        'Low': 21.27,
        'Medium': 26.70,
        'High': 27.24,
        'Jam': 31.18
    }

    delivery_time = {
        0: 22.88,
        1: 26.86,
        2: 40.45,
        3: 47.82
    }

    estimated_time = (
        distance_time +
        weather_time[weather] +
        traffic_time[traffic] +
        delivery_time[deliveries]
    ) / 4

    # Display result
    st.subheader("Estimated Delivery Time")
    st.metric(
        "Estimated Time (minutes)",
        round(estimated_time, 2)
    )

    st.write(
        "This estimate is based on the average delivery time "
        "for each selected factor in the dataset."
    )
