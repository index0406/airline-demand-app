import pandas as pd

def process_flight_data(raw_data):
    if not raw_data:
        return None, None

    df = pd.json_normalize(raw_data)
    df['departure_time'] = pd.to_datetime(df['departure.scheduled'], errors='coerce')
    df.dropna(subset=['departure_time'], inplace=True)

    # Create hourly trend
    df['hour'] = df['departure_time'].dt.hour
    hourly_trend = df['hour'].value_counts().sort_index()

    return df, hourly_trend