# Carbon Credit Prediction Using Sentinel-2 Satellite Data

A Streamlit-based web application that enables users to predict carbon credits for their agricultural fields using Sentinel-2 satellite imagery and machine learning algorithms.

## 🌱 Overview

This application leverages Sentinel-2 multispectral satellite data to estimate carbon sequestration potential in agricultural fields. Users can define their field boundaries, select time periods, and generate detailed monthly carbon credit reports. The system also provides predictive capabilities for future carbon credit estimation based on historical data patterns.

## ✨ Features

### Core Functionality
- **Interactive Field Selection**: Draw and define custom field boundaries on an interactive map
- **Sentinel-2 Integration**: Automated processing of multispectral satellite bands for vegetation analysis
- **Date Range Selection**: Flexible time period selection for carbon credit analysis
- **Monthly Reporting**: Generate comprehensive CSV reports with monthly carbon credit calculations
- **Predictive Analytics**: Forecast next year's carbon credits using historical field data

### Technical Capabilities
- Real-time satellite data processing
- Multiple vegetation indices calculation (NDVI, EVI, SAVI, etc.)
- Carbon sequestration modeling
- Time series analysis and forecasting
- Export functionality for data analysis

## 🚀 Installation

### Prerequisites
```bash
Python 3.8+
pip package manager
```

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/carbon-credit-prediction.git
cd carbon-credit-prediction
```

2. **Create virtual environment**
```bash
python -m venv carbon_env
source carbon_env/bin/activate  # On Windows: carbon_env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API credentials**
Create a `.env` file in the root directory:
```env
SENTINEL_HUB_CLIENT_ID=your_client_id
SENTINEL_HUB_CLIENT_SECRET=your_client_secret
GOOGLE_EARTH_ENGINE_KEY=your_gee_key
```

5. **Run the application**
```bash
streamlit run app.py
```

## 📋 Requirements

### Core Dependencies
```
streamlit>=1.28.0
folium>=0.14.0
geopandas>=0.13.0
rasterio>=1.3.0
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
requests>=2.31.0
sentinelhub>=3.9.0
earthengine-api>=0.1.360
```

## 🎯 Usage Guide

### Step 1: Field Boundary Selection
1. Launch the application using `streamlit run app.py`
2. Navigate to the **Field Selection** tab
3. Use the interactive map to draw your field boundaries
4. Click points to create a polygon around your area of interest
5. Confirm the selected area

### Step 2: Time Period Configuration
1. Go to the **Date Selection** tab
2. Choose your analysis start date
3. Select the end date for your study period
4. Ensure the time range covers your growing seasons

### Step 3: Generate Carbon Credit Report
1. Navigate to the **Analysis** tab
2. Click **"Process Satellite Data"** to begin analysis
3. The system will:
   - Fetch Sentinel-2 imagery for your specified area and time period
   - Calculate vegetation indices
   - Estimate carbon sequestration rates
   - Generate monthly carbon credit values

### Step 4: Download Results
1. Once processing is complete, review the summary statistics
2. Click **"Download Monthly Report"** to get your CSV file
3. The CSV contains:
   - Monthly carbon credit estimates (tons CO2 equivalent)
   - Vegetation index values
   - Weather correlation data
   - Confidence intervals

### Step 5: Future Predictions
1. Access the **Prediction** tab
2. Upload your historical data (or use data from previous analyses)
3. Select prediction parameters:
   - Forecast period (months ahead)
   - Model type (Linear Regression, Random Forest, LSTM)
4. Generate and download prediction results

## 📊 Output Data Structure

### Monthly Report CSV Format
```csv
Date,Carbon_Credits_tCO2,NDVI_Mean,EVI_Mean,Field_Area_ha,Confidence_Level
2023-01-01,2.45,0.68,0.52,10.5,0.87
2023-02-01,2.78,0.71,0.55,10.5,0.89
...
```

### Prediction Report Format
```csv
Prediction_Date,Predicted_Carbon_Credits,Lower_Bound,Upper_Bound,Model_Confidence
2024-01-01,2.89,2.34,3.44,0.82
2024-02-01,3.12,2.67,3.57,0.85
...
```

## 🛠️ Technical Architecture

### Data Processing Pipeline
1. **Satellite Data Acquisition**: Sentinel-2 L2A products via Sentinel Hub API
2. **Preprocessing**: Cloud masking, atmospheric correction, geometric correction
3. **Feature Extraction**: Vegetation indices, texture analysis, temporal metrics
4. **Carbon Modeling**: Machine learning models trained on ground truth data
5. **Report Generation**: Statistical analysis and CSV export

### Supported Satellite Bands
- Band 2: Blue (490nm)
- Band 3: Green (560nm) 
- Band 4: Red (665nm)
- Band 5: Vegetation Red Edge (705nm)
- Band 6: Vegetation Red Edge (740nm)
- Band 7: Vegetation Red Edge (783nm)
- Band 8: NIR (842nm)
- Band 8A: Narrow NIR (865nm)
- Band 11: SWIR (1610nm)
- Band 12: SWIR (2190nm)


## 🔬 Methodology

### Carbon Credit Calculation
The application uses a multi-factor approach to estimate carbon sequestration:

1. **Biomass Estimation**: Using vegetation indices to estimate above-ground biomass
2. **Soil Carbon**: Incorporating soil organic carbon changes based on land use
3. **Seasonal Variations**: Accounting for crop cycles and seasonal growth patterns
4. **Validation**: Cross-reference with ground truth measurements where available

### Prediction Models
- **Linear Regression**: For basic trend analysis
- **Random Forest**: For non-linear relationships and feature importance
- **LSTM Networks**: For complex temporal pattern recognition

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Code formatting
black src/
flake8 src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Common Issues
- **API Authentication**: Ensure your Sentinel Hub credentials are correctly configured
- **Large Fields**: Processing may take longer for areas >100 hectares
- **Data Gaps**: Some time periods may have limited satellite coverage due to clouds





## 🔄 Version History

- **v1.2.0** - Added LSTM prediction models and improved UI
- **v1.1.0** - Enhanced carbon modeling algorithms
- **v1.0.0** - Initial release with basic functionality

---

**Made with 🌱 for sustainable agriculture and carbon monitoring**
