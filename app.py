# import streamlit as st

# #app ka titel
# st. title("Unit Converter")

# #unit conversion
# conversion_types = ["Length","Weight","Temperature",]
# # user se convrsion choose karwana
# conversion_choice = st.selectbox("choos conversion Type:",conversion_types)

# #length conversion

# if conversion_choice == "Length":
#     length_units = ["Meters", "Kilometers","feet","Inches","Centimeters"]
#     input_value = st.number_input("Enter Length Value:",min_value=0.0, format = "%.2f")
#     from_unit = st.selectbox("from Unit",length_units)
#     to_unit = st.selectbox("To Unit:",length_units)

#     #conversion Dictionaries
#     length_conversion = {
#         "Meters":1,
#         "kilometers":1000,
#         "feet":0.3048,
#         "Inches":0.0254,
#         "Centimeters":0.01,
#     }

#     #conversion Logic
#     if st.button("Convert"):
#         result = input_value * (length_units[from_unit] / length_units[to_unit])
#         st.success(f'{input_value}{from_unit}is equal to {result}{to_unit}')

#     #Weigth conversion
#     elif conversion_choice == "weight":
#         weight_units = ["kilograms","Grams","pounds","Ounces"]
#         input_value = st.number_input("Enter Weight Value:",min_value=0.0, format = "%.2f")
#         from_unit = st.selectbox("from Unit",weight_units)
#         to_unit = st.selectbox("To Unit:",weight_units)

#     #conversion Dictionaries
#     weight_conversion ={
#         "kilogroms":1,
#         "Grams":0.001,
#         "pounds":0.453592,
#         "Ounces":0.0283495
#     }

#     ##conversion Logic
#     if st.button("Convert"):
#         result = input_value * (weight_units[from_unit] / weight_units[to_unit])
#         st.success(f'{input_value}{from_unit}is equal to {result:.2f}{to_unit}')

#     #Temperature conversion
#     elif conversion_choice == "Temperature":
#         temperature_units = ["Celsius","fahrenhit","Kelvin"]
#         input_value = st.number_input("Enter Temperature Value:",min_value=0.0, format = "%.2f")
#         from_unit = st.selectbox("from Unit",temperature_units)
#         to_unit = st.selectbox("To Unit:",temperature_units)

#         def convert_temperature(value, from_unit, to_unit):
#             if from_unit =="Celsius":
#                 if to_unit == "fahrehit":
#                     return (value * 9/5) + 32
#                 elif to_unit == "Kelvin":
#                     return value + 273.15
#             elif from_unit == "fahrenhit":
#                 if to_unit == "Calsius":
#                     return (value - 32) * 5/9
#                 elif to_unit == "kelvin":
#                     return (value-32)* 5/9 +273.15
#             elif from_unit == "Kelvin":
#                 if to_unit == "Celsius":
#                     return value - 273.15
#                 elif to_unit == "Fahrenhit":
#                     return (value-273.15) * 9/5 +32
#             return value
#          #conversion Logic
#         if st.button("Convert"):
#            result = convert_temperature (input_value, from_unit, to_unit)
#            st.success(f'{input_value}{from_unit}is equal to {result}{to_unit}')










# import streamlit as st

# # App title
# st.title("Unit Converter")

# # Unit conversion options
# conversion_types = ["Length", "Weight", "Temperature", "Area", "Volume"]
# conversion_choice = st.selectbox("Choose conversion Type:", conversion_types)

# # Length conversion
# if conversion_choice == "Length":
#     length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
#     input_value = st.number_input("Enter Length Value:", min_value=0.0, format="%.2f")
#     from_unit = st.selectbox("From Unit", length_units)
#     to_unit = st.selectbox("To Unit:", length_units)

#     # Length conversion dictionary
#     length_conversion = {
#         "Meters": 1,
#         "Kilometers": 1000,
#         "Feet": 0.3048,
#         "Inches": 0.0254,
#         "Centimeters": 0.01,
#     }

#     # Decimal precision
#     precision = st.slider("Select Decimal Precision:", min_value=0, max_value=5, value=2)

#     # Conversion logic for length
#     if st.button("Convert", key="convert_length"):
#         from_unit_index = length_units.index(from_unit)
#         to_unit_index = length_units.index(to_unit)
#         result = input_value * (length_conversion[length_units[from_unit_index]] / length_conversion[length_units[to_unit_index]])
#         st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# # Weight conversion
# elif conversion_choice == "Weight":
#     weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
#     input_value = st.number_input("Enter Weight Value:", min_value=0.0, format="%.2f")
#     from_unit = st.selectbox("From Unit", weight_units)
#     to_unit = st.selectbox("To Unit:", weight_units)

#     # Weight conversion dictionary
#     weight_conversion = {
#         "Kilograms": 1,
#         "Grams": 0.001,
#         "Pounds": 0.453592,
#         "Ounces": 0.0283495,
#     }

#     # Conversion logic for weight
#     if st.button("Convert", key="convert_weight"):
#         from_unit_index = weight_units.index(from_unit)
#         to_unit_index = weight_units.index(to_unit)
#         result = input_value * (weight_conversion[weight_units[from_unit_index]] / weight_conversion[weight_units[to_unit_index]])
#         st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# # Temperature conversion
# elif conversion_choice == "Temperature":
#     temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
#     input_value = st.number_input("Enter Temperature Value:", min_value=0.0, format="%.2f")
#     from_unit = st.selectbox("From Unit", temperature_units)
#     to_unit = st.selectbox("To Unit:", temperature_units)

#     def convert_temperature(value, from_unit, to_unit):
#         if from_unit == "Celsius":
#             if to_unit == "Fahrenheit":
#                 return (value * 9/5) + 32
#             elif to_unit == "Kelvin":
#                 return value + 273.15
#         elif from_unit == "Fahrenheit":
#             if to_unit == "Celsius":
#                 return (value - 32) * 5/9
#             elif to_unit == "Kelvin":
#                 return (value - 32) * 5/9 + 273.15
#         elif from_unit == "Kelvin":
#             if to_unit == "Celsius":
#                 return value - 273.15
#             elif to_unit == "Fahrenheit":
#                 return (value - 273.15) * 9/5 + 32
#         return value

#     # Conversion logic for temperature
#     if st.button("Convert", key="convert_temperature"):
#         result = convert_temperature(input_value, from_unit, to_unit)
#         st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# # Area conversion
# elif conversion_choice == "Area":
#     area_units = ["Square Meters", "Square Kilometers", "Acres", "Square Feet"]
#     input_value = st.number_input("Enter Area Value:", min_value=0.0, format="%.2f")
#     from_unit = st.selectbox("From Unit", area_units)
#     to_unit = st.selectbox("To Unit:", area_units)

#     # Area conversion dictionary
#     area_conversion = {
#         "Square Meters": 1,
#         "Square Kilometers": 1e6,
#         "Acres": 4046.86,
#         "Square Feet": 0.092903,
#     }

#     # Conversion logic for area
#     if st.button("Convert", key="convert_area"):
#         from_unit_index = area_units.index(from_unit)
#         to_unit_index = area_units.index(to_unit)
#         result = input_value * (area_conversion[area_units[from_unit_index]] / area_conversion[area_units[to_unit_index]])
#         st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# # Volume conversion
# elif conversion_choice == "Volume":
#     volume_units = ["Cubic Meters", "Liters", "Cubic Inches", "Gallons"]
#     input_value = st.number_input("Enter Volume Value:", min_value=0.0, format="%.2f")
#     from_unit = st.selectbox("From Unit", volume_units)
#     to_unit = st.selectbox("To Unit:", volume_units)

#     # Volume conversion dictionary
#     volume_conversion = {
#         "Cubic Meters": 1,
#         "Liters": 1000,
#         "Cubic Inches": 0.000016387064,
#         "Gallons": 3.78541,
#     }

#     # Conversion logic for volume
#     if st.button("Convert", key="convert_volume"):
#         from_unit_index = volume_units.index(from_unit)
#         to_unit_index = volume_units.index(to_unit)
#         result = input_value * (volume_conversion[volume_units[from_unit_index]] / volume_conversion[volume_units[to_unit_index]])
#         st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')










import streamlit as st
import requests

# App title
st.title("Advanced Unit Converter")

# Unit conversion options
conversion_types = ["Length", "Weight", "Temperature", "Area", "Volume", "Currency", "Speed", "Power", "Time", "Fractional"]
conversion_choice = st.selectbox("Choose conversion Type:", conversion_types)

# Decimal precision slider
precision = st.slider("Select Decimal Precision:", min_value=0, max_value=5, value=2)

# 1. **Length Conversion**
if conversion_choice == "Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("Enter Length Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", length_units)
    to_unit = st.selectbox("To Unit:", length_units)

    # Length conversion dictionary
    length_conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01,
    }

    # Conversion logic for length
    if st.button("Convert", key="convert_length"):
        from_unit_index = length_units.index(from_unit)
        to_unit_index = length_units.index(to_unit)
        result = input_value * (length_conversion[length_units[from_unit_index]] / length_conversion[length_units[to_unit_index]])
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 2. **Weight Conversion**
elif conversion_choice == "Weight":
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    input_value = st.number_input("Enter Weight Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", weight_units)
    to_unit = st.selectbox("To Unit:", weight_units)

    # Weight conversion dictionary
    weight_conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }

    # Conversion logic for weight
    if st.button("Convert", key="convert_weight"):
        from_unit_index = weight_units.index(from_unit)
        to_unit_index = weight_units.index(to_unit)
        result = input_value * (weight_conversion[weight_units[from_unit_index]] / weight_conversion[weight_units[to_unit_index]])
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 3. **Temperature Conversion**
elif conversion_choice == "Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("Enter Temperature Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", temperature_units)
    to_unit = st.selectbox("To Unit:", temperature_units)

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value

    # Conversion logic for temperature
    if st.button("Convert", key="convert_temperature"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 4. **Currency Conversion (Using an API)**
elif conversion_choice == "Currency":
    currency_units = ["USD", "EUR", "INR", "GBP", "JPY"]
    input_value = st.number_input("Enter Currency Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Currency", currency_units)
    to_unit = st.selectbox("To Currency:", currency_units)

    # Fetch live conversion rates from an API (you can use the `ExchangeRate-API`)
    api_key = 'YOUR_API_KEY'  # Use your API key here
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_unit}'
    response = requests.get(url)
    data = response.json()
    rate = data["conversion_rates"].get(to_unit, 1)

    if st.button("Convert", key="convert_currency"):
        result = input_value * rate
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 5. **Speed Conversion**
elif conversion_choice == "Speed":
    speed_units = ["m/s", "km/h", "mph", "ft/s"]
    input_value = st.number_input("Enter Speed Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", speed_units)
    to_unit = st.selectbox("To Unit:", speed_units)

    # Speed conversion dictionary
    speed_conversion = {
        "m/s": 1,
        "km/h": 3.6,
        "mph": 2.23694,
        "ft/s": 3.28084,
    }

    # Conversion logic for speed
    if st.button("Convert", key="convert_speed"):
        from_unit_index = speed_units.index(from_unit)
        to_unit_index = speed_units.index(to_unit)
        result = input_value * (speed_conversion[speed_units[from_unit_index]] / speed_conversion[speed_units[to_unit_index]])
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 6. **Power Conversion**
elif conversion_choice == "Power":
    power_units = ["Watts", "Kilowatts", "Horsepower"]
    input_value = st.number_input("Enter Power Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", power_units)
    to_unit = st.selectbox("To Unit:", power_units)

    # Power conversion dictionary
    power_conversion = {
        "Watts": 1,
        "Kilowatts": 1000,
        "Horsepower": 745.7,
    }

    # Conversion logic for power
    if st.button("Convert", key="convert_power"):
        from_unit_index = power_units.index(from_unit)
        to_unit_index = power_units.index(to_unit)
        result = input_value * (power_conversion[power_units[from_unit_index]] / power_conversion[power_units[to_unit_index]])
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 7. **Time Conversion**
elif conversion_choice == "Time":
    time_units = ["Seconds", "Minutes", "Hours", "Days"]
    input_value = st.number_input("Enter Time Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", time_units)
    to_unit = st.selectbox("To Unit:", time_units)

    # Time conversion dictionary
    time_conversion = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
    }

    # Conversion logic for time
    if st.button("Convert", key="convert_time"):
        from_unit_index = time_units.index(from_unit)
        to_unit_index = time_units.index(to_unit)
        result = input_value * (time_conversion[time_units[from_unit_index]] / time_conversion[time_units[to_unit_index]])
        st.success(f'{input_value} {from_unit} is equal to {result:.{precision}f} {to_unit}')

# 8. **Fractional Input Support** (Using Python's `fractions` module)
elif conversion_choice == "Fractional":
    from fractions import Fraction
    input_value = st.text_input("Enter a Fraction (e.g., 1/2, 3/4):")
    if input_value:
        try:
            fraction_value = float(Fraction(input_value))
            st.write(f"The decimal equivalent is {fraction_value}")
        except:
            st.write("Invalid Fraction")

# Clear Button for Resetting the App
if st.button("Clear All", key="clear"):
    st.experimental_rerun()













