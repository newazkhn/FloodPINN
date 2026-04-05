# ============================================================
# config.py — Central configuration for FloodPINN
# ============================================================
# All hyperparameters and paths are defined here.
# Modify this file to change experiment settings.
# Never hardcode values inside model or notebook files.
# ============================================================

import os

# ── Project paths ────────────────────────────────────────
BASE_DIR    = r'C:\FloodPINN'
DATA_DIR    = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR  = os.path.join(BASE_DIR, 'outputs')
MODEL_DIR   = os.path.join(BASE_DIR, 'models')

# ── Google Earth Engine ──────────────────────────────────
GEE_PROJECT = 'ee-newazkhn'
GEE_FOLDER  = 'FloodPINN_Pakistan'

# ── Study area — Sindh Province, Pakistan ────────────────
STUDY_AREA = {
    'name'   : 'Sindh Province, Pakistan',
    'bbox'   : [66.5, 23.5, 71.5, 29.0],
    'center' : [26.5, 68.5],
    'zoom'   : 7
}

# ── Flood event dates ────────────────────────────────────
DATES = {
    'before_start' : '2022-01-01',
    'before_end'   : '2022-05-31',
    'flood_start'  : '2022-08-01',
    'flood_end'    : '2022-09-30'
}

# ── Input data bands (8 channels) ────────────────────────
INPUT_BANDS = [
    'SAR_VV_before',  # SAR VV polarisation pre-flood
    'SAR_VH_before',  # SAR VH polarisation pre-flood
    'SAR_VV_flood',   # SAR VV polarisation during flood
    'SAR_VH_flood',   # SAR VH polarisation during flood
    'MNDWI_before',   # Modified water index pre-flood
    'DEM',            # Terrain elevation (metres)
    'Slope',          # Terrain slope (degrees)
    'HAND',           # Height above nearest drainage (m)
]
N_CHANNELS = len(INPUT_BANDS)  # 8 total input channels

# ── Model architecture ───────────────────────────────────
MODEL = {
    'encoder'      : 'resnet34', # Pretrained ResNet34 encoder
    'in_channels'  : N_CHANNELS, # 8 input channels
    'out_channels' : 1,          # Binary flood mask output
    'dropout_rate' : 0.3,        # MC Dropout probability
    'n_mc_samples' : 20,         # Monte Carlo forward passes
}

# ── Training hyperparameters ─────────────────────────────
TRAIN = {
    'chip_size'    : 512,    # Image chip size in pixels
    'batch_size'   : 8,      # Training batch size
    'epochs'       : 50,     # Number of training epochs
    'lr'           : 1e-4,   # Initial learning rate
    'weight_decay' : 1e-5,   # L2 regularisation strength
    'val_split'    : 0.2,    # Validation set fraction
    'test_split'   : 0.1,    # Test set fraction
    'seed'         : 42,     # Random seed for reproducibility
}

# ── Loss function weights ────────────────────────────────
LOSS = {
    'bce_weight'     : 0.5,  # Binary cross entropy weight
    'dice_weight'    : 0.4,  # Dice loss weight
    'physics_weight' : 0.1,  # Physics constraint weight
}

# ── Export settings ──────────────────────────────────────
EXPORT = {
    'scale'      : 30,        # Pixel resolution in metres
    'max_pixels' : 1e10,      # Maximum GEE export pixels
    'format'     : 'GeoTIFF', # Output file format
}

# ── Uncertainty thresholds ───────────────────────────────
UNCERTAINTY = {
    'high'   : 0.10,  # Std < 0.10 = high confidence
    'medium' : 0.25,  # Std < 0.25 = medium confidence
    'low'    : 0.40,  # Std > 0.40 = low confidence
}