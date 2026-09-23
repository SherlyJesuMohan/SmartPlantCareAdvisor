#  Smart Plant Care Advisor

##  Project Description

Smart Plant Care Advisor is an AI-based web application that helps users understand the care requirements of their plants.

The user describes the plant and its current conditions in normal language. The application uses Artificial Intelligence to extract important information such as plant name, soil moisture, temperature, and sunlight level.

The extracted values are then processed using a fuzzy logic system to calculate a plant care score.

The project provides a simple and user-friendly way to understand plant care requirements.

---

## Features

-  Accepts plant information in natural language
-  Uses AI to understand the user's description
-  Extracts soil moisture level
-  Extracts temperature
-  Extracts sunlight level
-  Uses fuzzy logic to calculate a care score
-  Displays the calculated care requirement
-  Simple and interactive Streamlit interface
-  API token is kept private using environment variables

---

##  Technologies Used

- **Python**
- **Streamlit**
- **LangChain**
- **Hugging Face**
- **scikit-fuzzy**
- **NumPy**
- **SciPy**
- **NetworkX**
- **python-dotenv**

---

##  AI Component

The project uses a Hugging Face language model through the Hugging Face Inference API.

LangChain is used to create and manage the prompt used for extracting plant information from the user's natural-language description.

The AI extracts:

- Plant name
- Soil moisture
- Temperature
- Light level

The extracted information is returned in JSON format and passed to the fuzzy logic system.

---

##  Fuzzy Logic Component

The project uses fuzzy logic to calculate a plant care score.

The following inputs are considered:

- Soil moisture
- Temperature
- Sunlight

The fuzzy logic system classifies the inputs into categories such as:

- Low
- Medium
- High

Based on predefined fuzzy rules, a final care score between 0 and 100 is calculated.

The result is displayed as:

- 🟢 Low Care Needed
- 🟡 Moderate Care Needed
- 🔴 High Care Needed

 ## Installation and Setup

 1. Clone the Repository

```bash
git clone https://github.com/SherlyJesuMohan/SmartPlantCareAdvisor.git

2. Open the Project Folder

cd SmartPlantCareAdvisor

3. Install Required Packages

pip install -r requirements.txt

4. Configure the Hugging Face Token

Create a .env file in the project folder.

Add:

HF_TOKEN=your_huggingface_token_here

The actual token should never be uploaded to GitHub.

 Running the Project

Run the following command:

python -m streamlit run app.py

The application will open in the browser.

GitHub Repository:

```https://github.com/SherlyJesuMohan/SmartPlantCareAdvisor

Deployment Link:

```https://smart-plant-care-advisor.streamlit.app
