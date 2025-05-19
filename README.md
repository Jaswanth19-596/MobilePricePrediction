# MobilePricePrediction

## Overview

This project is designed to predict mobile phone prices based on various features using machine learning techniques. It encompasses data collection through web scraping, data preprocessing, model training, and deployment of a user-friendly interface for predictions.

## Project Structure

- **`archive/`**: Contains archived datasets or previous versions of data.
- **`data/`**: Houses the primary datasets used for training and evaluation.
- **`gsmarena_scraper/`**: Scripts and tools for scraping mobile phone data from GSMArena.
- **`models/`**: Serialized machine learning models and related artifacts.
- **`notebooks/`**: Jupyter notebooks detailing exploratory data analysis and model experimentation.
- **`src/`**: Source code for data processing, feature engineering, and model training.
- **`streamlit/`**: Streamlit application for interactive user predictions.
- **`main.py`**: Main script to orchestrate the training and prediction pipeline.
- **`requirements.txt`**: List of Python dependencies required to run the project.

## Features

The dataset includes various features that influence mobile phone pricing, such as:

- Battery capacity
- RAM and storage
- Camera specifications
- Screen size and resolution
- Processor details
- Brand and model information

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Jaswanth19-596/MobilePricePrediction.git
cd MobilePricePrediction
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

To train the machine learning model:

```bash
python main.py
```

This script will process the data, train the model, and save the trained model in the `models/` directory.

### Running the Streamlit App

To launch the interactive web application:

```bash
streamlit run streamlit/app.py
```

This will open a web interface where you can input mobile phone features and get a predicted price.

## 📊 Model Performance

The project employs various regression algorithms to predict mobile prices. Model performance metrics and comparisons are detailed within the Jupyter notebooks in the `notebooks/` directory.

## 📈 Future Enhancements

- Incorporate more diverse datasets for improved model generalization
- Implement advanced machine learning algorithms for better accuracy
- Enhance the Streamlit app with more interactive features and visualizations

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
