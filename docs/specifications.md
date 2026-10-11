# Bike Sharing Demand Prediction Project Specification

## 1. Overview
This project aims to build a machine learning model that predicts bike demand using historical bike-sharing data and then expose that prediction capability through an interactive web application. The model is developed in a Jupyter notebook, trained on environmental and time-related features, and then saved for later use in the application.

The final product is a Streamlit-based UI that lets a user choose conditions such as hour, weather, temperature, humidity, and wind speed, and immediately receives a predicted bike demand value along with a decision-support interpretation.

## 2. Problem statement
Bike-sharing systems often experience demand imbalance: certain times of the day or specific weather conditions can lead to empty stations or overloaded stations. This creates user dissatisfaction, operational inefficiency, and logistical challenges for transportation teams.

The solution should help operators predict expected bike demand in advance, so they can improve fleet planning and adjust rebalancing actions before shortages occur.

## 3. Project objective
The main goal is twofold:
1. Build and evaluate a demand prediction model in a notebook using historical bike-sharing data.
2. Develop a user-friendly Streamlit interface that loads the trained model and displays predictions for new scenarios.

The project is therefore a classic machine learning + application integration workflow: experimentation in the notebook, deployment of a trained model, and operational use through a dashboard.

## 4. Development workflow
The project follows this workflow:
- Data preparation and exploration in the notebook
- Feature engineering from bike-sharing and weather variables
- Train/test split and model training
- Evaluation using R², MAE, and RMSE
- Save the trained model bundle to a .joblib file
- Load the model in the Streamlit app
- Use the app to predict demand for user-defined input values

This makes the project a realistic end-to-end ML application, not just a model experiment.

## 4. Target users
### 4.1 City mobility operators
- Bike-sharing fleet managers
- Urban transportation planners
- Network rebalancing teams
- Smart city operations staff

These users need to know when and where demand will spike and which periods require intervention.

### 4.2 Analysts and data specialists
- Urban data analysts
- Research teams
- Students or project contributors studying mobility and machine learning

These users need to test prediction inputs, inspect model outputs, and understand the model’s behavior.

## 5. Core needs of the application
### 5.1 Operational forecasting
The system must estimate how many bikes are likely to be required during a given hour. Forecasting should depend on the most relevant variables, such as:
- hour of the day,
- whether it is a working day,
- temperature,
- humidity,
- wind speed,
- weather condition.

### 5.2 Decision support for logistics
The application must translate the predicted demand into a practical operational diagnosis, such as:
- normal / stable demand,
- high activity requiring monitoring,
- critical peak demand requiring rebalancing interventions.

### 5.3 Spatial awareness
The app should provide a simple spatial visualization of simulated pressure across the network so that staff can understand the system’s operational load as a whole.

### 5.4 Model transparency
The application should show the input vector used for the prediction and display key model metrics, including:
- R² score,
- MAE,
- RMSE.

This supports trust and helps users understand the reliability of the forecast.

## 6. Functional requirements
### 6.1 User input interface
The application must provide a sidebar with the following configurable values:
- Time of day (hour from 0 to 23)
- Day type (working day vs weekend or holiday)
- Feels-like temperature (°C)
- Relative humidity (%)
- Wind speed (km/h)
- Weather condition

These values represent the operational context that affects bike demand.

### 6.2 Demand prediction
The system must take the input values, build a structured feature set, and pass it to a trained machine learning model. The model output is an estimated bike demand value in bikes per hour.

Requirements:
- the prediction must be rounded to the nearest integer,
- negative predictions must be clamped to zero,
- the estimated demand must be compared to the baseline average demand.

### 6.3 Operational status classification
The application must classify the predicted demand into statuses:
- Critical peak demand: very high demand, likely causing significant station shortages
- High activity: notable demand, requiring monitoring and rotation planning
- Smooth traffic / quiet period: stable conditions, suitable for maintenance and system optimization

The thresholds used by the app are:
- 400+ bikes/hour: critical peak demand
- 180+ bikes/hour: high activity
- below 180: normal or quiet period

### 6.4 Dashboard output
The dashboard must display:
- estimated demand value,
- comparison to baseline demand,
- logistics diagnosis text,
- simulated station pressure network map,
- input vector table,
- model performance metrics.

### 6.5 Model loading and error handling
The app must load a pre-trained model from a joblib file. If the model is missing, the interface should show a clear error message rather than crashing.

### 6.6 Data provenance
The application uses a bike-sharing dataset derived from hourly aggregated bike rental records, including environmental and seasonal information. The dataset is based on the Capital Bikeshare system and weather context data, and it supports regression-based demand prediction.

## 7. Data model and features
The core data used by the model includes the following features:
- hr: hour of the day
- workingday: whether the day is a working day
- temp_c: temperature in Celsius
- humidity: relative humidity
- windspeed_kmh: wind speed in km/h
- weathersit: weather condition category

The weather category is encoded in a simple scale:
- 1: clear / mostly clear
- 2: misty / cloudy
- 3: light rain / light snow
- 4: heavy rain / storm

The target variable is the predicted bike rental demand, expressed as a count of bikes needed per hour.

## 8. Non-functional requirements
### 8.1 Usability
- The interface must be simple, readable, and easy to use.
- The app should work well on desktop screens and support a modern dashboard layout.
- Sidebar controls must be clearly labeled and suitable for operational use.

### 8.2 Performance
- Prediction generation should happen instantly after the user changes a parameter.
- The app should remain responsive even when several dashboard components are displayed simultaneously.

### 8.3 Reliability
- The system must handle invalid or missing model files gracefully.
- The prediction logic must always return a valid non-negative output.
- The interface should show clear and structured outputs for all major states.

### 8.4 Maintainability
- The code should remain modular, with separate responsibilities for input collection, model loading, prediction logic, and dashboard rendering.
- The project should be easy to extend with additional features such as alternative models, more stations, or richer forecasting outputs.

### 8.5 Data quality and trust
- The app should show the actual model inputs and the metrics used to assess performance.
- The results should be interpretable by operators rather than pure black-box outputs.

## 9. Technical stack assumptions
The current project is built around the following technical components:
- Python
- Streamlit for the interactive web interface
- pandas and numpy for data preparation
- scikit-learn for machine learning model usage
- joblib for loading the trained model
- a pre-trained .joblib model bundle containing the model and evaluation metrics

This architecture is appropriate for a lightweight intelligent dashboard that focuses on operational forecasting rather than a full enterprise platform.

## 10. User stories
### 10.1 Mobility operator stories
- As a bike-sharing manager, I want to set the expected hour and weather conditions so that I can estimate bike demand.
- As a bike-sharing manager, I want to see whether the network is in a critical demand state so that I can trigger rebalancing actions.
- As a bike-sharing manager, I want to view the estimated demand and compare it with the average so that I can prioritize intervention.

### 10.2 Analyst stories
- As a data analyst, I want to inspect model inputs so that I can understand the prediction context.
- As a data analyst, I want to review evaluation metrics so that I can assess model reliability.
- As a project contributor, I want the model to be loaded from a reusable artifact so that the system is easy to maintain.

## 11. Acceptance criteria
The application is considered successful when:
- a user can configure operational inputs from the sidebar,
- the app predicts bike demand based on those values,
- the estimated demand is displayed with a meaningful operational interpretation,
- the dashboard shows the correct risk status classification,
- the model performance metrics are visible,
- the input vector used for prediction is shown,
- the map visualization is rendered for the current scenario,
- the app handles missing model files with an informative error,
- the solution is easy to understand and extend for future forecasting improvements.

## 12. Expected benefits
This application will help a city mobility team by:
- reducing station imbalance,
- improving vehicle redistribution planning,
- increasing user satisfaction,
- lowering operational inefficiencies,
- enabling data-informed decision making,
- making smart city transportation management more predictive and proactive.

## 13. Project scope summary
The initial version of the application includes:
1. user-driven forecasting inputs,
2. hourly bike demand prediction,
3. demand-level diagnosis,
4. network pressure visualization,
5. model metrics and feature inspection,
6. dataset-driven decision support for fleet operations.

Future extensions may include:
- more detailed station-level forecasts,
- maps with real geographic station data,
- time-series trend analysis,
- forecasting for multiple days or weeks,
- integration with live operational data and rebalancing APIs.

## 14. Final specification statement
The application should be a practical machine learning dashboard for a smart city bike-sharing system. Its purpose is to predict demand for bikes at specific times and weather conditions, classify operational risk, and support fleet rebalancing decisions. The product should be lightweight, interpretable, responsive, and useful to operators who need fast, data-informed guidance for managing urban mobility systems.
