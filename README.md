# FloodPINN

### Uncertainty-Aware Physics-Informed SAR-Optical Fusion for Flood Inundation Mapping of the 2022 Pakistan Mega-Flood

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.11-orange)](https://pytorch.org)
[![GEE](https://img.shields.io/badge/Google%20Earth%20Engine-API-green)](https://earthengine.google.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📌 Overview

This repository contains the full implementation of a novel deep learning 
framework for flood inundation mapping that combines three key innovations:

| Innovation | Description |
|-----------|-------------|
| **Multi-Sensor Fusion** | Sentinel-1 SAR + Sentinel-2 Optical + SRTM DEM |
| **Physics-Guided Training** | Water flow constraints embedded in loss function |
| **Uncertainty Quantification** | MC Dropout for pixel-level confidence estimation |

Applied to the catastrophic **2022 Pakistan flood** — one of the worst 
climate disasters in recorded history — which submerged one-third of the 
country and displaced over 33 million people.

---

## 🎯 Motivation

During the 2022 Pakistan monsoon flood (August–September), **zero 
cloud-free Sentinel-2 optical images** were available over Sindh province. 
This repository demonstrates that physics-informed SAR-optical fusion with 
uncertainty quantification provides more accurate and trustworthy flood maps 
than single-sensor or traditional deep learning approaches.

---

## 🗂️ Repository Structure

FloodPINN/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Initial SAR + optical exploration
│   ├── 02_data_download.ipynb         # Dataset download scripts
│   ├── 03_pakistan_data.ipynb         # Pakistan 2022 data collection
│   ├── 04_preprocessing.ipynb         # Image chip generation
│   ├── 05_unet_baseline.ipynb         # Standard U-Net baseline
│   ├── 06_physics_uncertainty.ipynb   # Main model (core contribution)
│   └── 07_results_figures.ipynb       # Paper figures and tables
│
├── models/
│   ├── unet.py                        # Standard U-Net architecture
│   ├── physics_unet.py                # Physics-informed U-Net
│   └── uncertainty.py                 # MC Dropout uncertainty module
│
├── preprocessing/
│   ├── sar_preprocess.py              # SAR speckle filtering + calibration
│   ├── optical_preprocess.py          # Cloud masking + water indices
│   └── chip_generator.py             # 512x512 image tiling
│
├── utils/
│   ├── losses.py                      # BCE + Dice + Physics loss
│   ├── metrics.py                     # IoU, F1, uncertainty metrics
│   └── visualise.py                  # Result plotting utilities
│
├── config.py                          # All hyperparameters and paths
├── train.py                           # Model training script
├── evaluate.py                        # Evaluation and inference script
├── requirements.txt                   # Python dependencies
└── README.md                          # This file

---

## 📊 Dataset

All data is freely available and accessed via Google Earth Engine:

| Dataset | Source | Resolution | Purpose |
|---------|--------|-----------|---------|
| Sentinel-1 GRD | ESA Copernicus | 10m | SAR flood detection |
| Sentinel-2 SR | ESA Copernicus | 10m | Optical reference |
| SRTM DEM | NASA/USGS | 30m | Terrain elevation |
| MERIT HAND | MERIT Hydro | 90m | Flood susceptibility |
| JRC Surface Water | EU JRC | 30m | Permanent water mask |
| Sen1Floods11 | Cloud to Street | 10m | Training labels |

**Study Area:** Sindh Province, Pakistan  
**Flood Event:** August–September 2022  
**GEE Project:** `ee-newazkhn`

---

## 🧠 Model Architecture
INPUT (8 channels)
SAR VV before │ SAR VH before │ SAR VV flood │ SAR VH flood
MNDWI before  │ DEM           │ Slope        │ HAND index
│
▼
ENCODER (ResNet34 pretrained)
Feature extraction with skip connections
│
▼
DECODER with MC Dropout (p=0.3)
Upsampling + physics-constrained training
│
▼
OUTPUT
Flood extent map + Uncertainty map

**Loss Function:**
Total Loss = 0.5 × BCE Loss
+ 0.4 × Dice Loss
+ 0.1 × Physics Loss (water flow constraint)

**Uncertainty Estimation:**
Run N=20 forward passes with dropout active
Mean prediction → flood extent map
Std deviation   → uncertainty/confidence map

---

## ⚙️ Environment Setup
```bash
# Step 1 — Create conda environment
conda create -n floodpinn python=3.10
conda activate floodpinn

# Step 2 — Install dependencies
pip install -r requirements.txt

# Step 3 — Authenticate Google Earth Engine
earthengine authenticate

# Step 4 — Launch Jupyter Lab
cd C:\FloodPINN
jupyter lab
```

---

## 🚀 Quickstart
```python
# Run notebooks in order:
# 1. Collect data
jupyter nbconvert --to notebook --execute notebooks/03_pakistan_data.ipynb

# 2. Preprocess
jupyter nbconvert --to notebook --execute notebooks/04_preprocessing.ipynb

# 3. Train baseline
jupyter nbconvert --to notebook --execute notebooks/05_unet_baseline.ipynb

# 4. Train main model
jupyter nbconvert --to notebook --execute notebooks/06_physics_uncertainty.ipynb

# 5. Generate figures
jupyter nbconvert --to notebook --execute notebooks/07_results_figures.ipynb
```

---

## 📈 Results

Results will be updated as experiments complete.

| Model | IoU ↑ | F1 ↑ | Precision | Recall | Uncertainty |
|-------|--------|------|-----------|--------|-------------|
| SAR only (baseline) | - | - | - | - | ✗ |
| U-Net (SAR + Optical) | - | - | - | - | ✗ |
| + Physics Loss | - | - | - | - | ✗ |
| **FloodPINN (Ours)** | - | - | - | - | **✓** |

---

## 📝 Citation

If you use this code in your research, please cite:
```bibtex
@article{khan2026floodpinn,
  title   = {Uncertainty-Aware Physics-Informed SAR-Optical Fusion 
             for Flood Inundation Mapping of the 2022 Pakistan Mega-Flood},
  author  = {Khan, Newaz Ibrahim},
  journal = {Remote Sensing of Environment},
  year    = {2026},
  note    = {Under review}
}
```

---

## 👤 Author

**Newaz Ibrahim Khan**  
BSc in Computer Science & Engineering  
World University of Bangladesh  
📧 newazkhn@gmail.com  
🔗 [GitHub](https://github.com/newazkhn)

---

## 📄 License

This project is licensed under the MIT License.  
Free to use with attribution.

---

## 🙏 Acknowledgements

- European Space Agency (ESA) for Sentinel-1 and Sentinel-2 data
- NASA/USGS for SRTM DEM data
- Cloud to Street for Sen1Floods11 benchmark dataset
- Google Earth Engine for cloud computing platform
