import streamlit as st

# Function to calculate the price with markup based on the input price and provided ranges
def calculate_price(input_price):
    if 0 <= input_price <= 10:
        multiplier = 4.5
    elif 11 <= input_price <= 20:
        multiplier = 4
    elif 21 <= input_price <= 30:
        multiplier = 3.5
    elif 31 <= input_price <= 40:
        multiplier = 3.25
    elif 41 <= input_price <= 75:
        multiplier = 2.75
    elif 76 <= input_price <= 125:
        multiplier = 2.5
    elif 126 <= input_price <= 175:
        multiplier = 2
    elif 176 <= input_price <= 275:
        multiplier = 1.75
    elif 276 <= input_price <= 100000:
        multiplier = 1.5
    else:
        return "Invalid price"

    # Multiply the input price by the multiplier
    base_price = input_price * multiplier
    
    # Add 35% markup and $15 to the base price
    final_price_with_markup = (base_price * 1.14)
    return round(final_price_with_markup)  # Rounded with no decimal

# Streamlit app UI
st.title("Hahas Heating & Cooling")

# Step 1: User input for price (in main area)
input_price = st.number_input("Enter the price:", min_value=0.0, step=0.01)

# All user questions in the sidebar
st.sidebar.title("Calculation Options")

# Step 2: Ask if using flat rate pricing (using dropdown instead of radio)
use_flat_rate = st.sidebar.selectbox("Are you using flat rate pricing?", ("Yes", "No"))

service_call_fee = 0
labor_cost_per_hour = 0
labor_hours = 0

if use_flat_rate == "Yes":
    # Step 3: Ask if it's commercial or residential (using dropdown)
    property_type = st.sidebar.selectbox("Is this for a commercial or residential job?", ("Residential", "Commercial"))

    # Step 4: Add service call fee based on type
    if property_type == "Residential":
        service_call_fee = 89.00
    elif property_type == "Commercial":
        service_call_fee = 150.00
    
    # Step 5: Ask if user wants to add labor (using dropdown)
    add_labor = st.sidebar.selectbox("Do you want to add labor?", ("Yes", "No"))

    if add_labor == "Yes":
        # Step 6: Ask if it's for a warranty company or not (using dropdown)
        warranty_company = st.sidebar.selectbox("Is this for a warranty company?", ("Yes", "No"))
        if warranty_company == "Yes":
            labor_cost_per_hour = 150.00  # Labor per hour for warranty company
        else:
            labor_cost_per_hour = 200.00  # Labor per hour for non-warranty company
        
        # Step 7: Ask how many labor hours (using number input)
        labor_hours = st.sidebar.number_input("Enter the number of labor hours:", min_value=0.0, step=0.5)

# Step 8: Ask if user wants to discount service call fee (using dropdown)
discount_service_call = st.sidebar.selectbox("Do you want to discount the service call fee?", ("Yes", "No"))

# Button to trigger the calculation (also in sidebar)
if st.sidebar.button("Calculate Final Price"):
    if input_price > 0:
        result = calculate_price(input_price)
        labor_cost = labor_hours * labor_cost_per_hour
        
        # Calculate the total price
        total_price = result + labor_cost
        
        # Apply service call fee only if not discounting it
        if discount_service_call == "No":
            total_price += service_call_fee
        
        # Displaying costs separately
        st.write(f"Service Call Fee: ${round(service_call_fee):,}" if discount_service_call == "No" else "Service Call Fee: $0")
        st.write(f"Labor Cost: ${round(labor_cost):,}")
        st.write(f"Total Price with Markup: ${round(total_price):,}")
    else:
        st.write("Please enter a valid price greater than 0.")
