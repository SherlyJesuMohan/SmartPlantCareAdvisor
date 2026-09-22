import streamlit as st
from fuzzy_logic import calculate_care_score
from llm_helper import extract_plant_data


st.set_page_config(
    page_title="Smart Plant Care Advisor",
    page_icon="🌱"
)


st.title("🌱 Smart Plant Care Advisor")

st.write(
    "Describe your plant and its current conditions in normal language. "
    "The AI will understand the description and the fuzzy logic system "
    "will calculate the care requirement."
)


st.subheader("🌿 Describe Your Plant")

user_input = st.text_area(
    "Enter your plant details:",
    placeholder=(
        "Example: My tomato plant has dry soil, "
        "the temperature is 32°C and it gets bright sunlight."
    )
)


if st.button("🤖 Analyze Plant"):

    if user_input.strip() == "":
        st.warning("Please describe your plant first.")

    else:

        try:

            # -----------------------------------
            # LANGCHAIN AI COMPONENT
            # -----------------------------------

            plant_data = extract_plant_data(user_input)

            plant_name = plant_data["plant_name"]
            soil_moisture = float(plant_data["soil_moisture"])
            temperature = float(plant_data["temperature"])
            light = float(plant_data["light"])


            # -----------------------------------
            # FUZZY LOGIC COMPONENT
            # -----------------------------------

            care_score = calculate_care_score(
                soil_moisture,
                temperature,
                light
            )


            # -----------------------------------
            # DISPLAY AI EXTRACTED INFORMATION
            # -----------------------------------

            st.subheader("🤖 AI Extracted Information")

            st.write(
                "🌱 **Plant Name:**",
                plant_name
            )

            st.write(
                "💧 **Soil Moisture:**",
                f"{soil_moisture}%"
            )

            st.write(
                "🌡️ **Temperature:**",
                f"{temperature}°C"
            )

            st.write(
                "☀️ **Sunlight Level:**",
                f"{light}%"
            )


            # -----------------------------------
            # DISPLAY FUZZY RESULT
            # -----------------------------------

            st.subheader("🌿 Fuzzy Logic Result")

            st.metric(
                "Fuzzy Care Score",
                f"{care_score}/100"
            )


            # -----------------------------------
            # CARE RECOMMENDATION
            # -----------------------------------

            if care_score >= 60:

                st.error("🔴 High Care Needed")

                st.write(
                    "Your plant may need immediate attention. "
                    "Check its watering, temperature and sunlight conditions."
                )


            elif care_score >= 40:

                st.warning("🟡 Moderate Care Needed")

                st.write(
                    "Your plant conditions are moderate. "
                    "Continue monitoring the plant regularly."
                )


            else:

                st.success("🟢 Low Care Needed")

                st.write(
                    "The current conditions appear suitable. "
                    "Continue normal plant care."
                )


        except Exception as e:

            st.error(
                "The AI could not understand the plant description."
            )

            st.write(
                "Please try describing the plant more clearly."
            )

            st.caption(
                f"Technical details: {e}"
            )