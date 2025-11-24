# Datasets from attacks.pdf

This document describes the datasets used in the **@papers/attacks.pdf** paper for evaluating frequency-estimation and heavy-hitter protocols.

## Overview

Three datasets are used throughout the paper (Section 5.1, p. 8) for both frequency-estimation and heavy-hitter evaluations (see also Fig. 4, p. 10).

## Dataset Details

### 1. Zipf (Synthetic)
- **Type**: Synthetic dataset
- **Items**: 1,024
- **Users**: 1,000,000
- **Purpose**: Used to mirror long-tailed popularity distributions

### 2. Fire (SF Fire Department "Alarms" subset)
- **Type**: Real-world dataset
- **Items**: Unit IDs (244 unique units)
- **Users**: 548,868
- **Source**: San Francisco Fire Department alarms data

### 3. IPUMS (U.S. Census 2017)
- **Type**: Real-world dataset
- **Items**: Cities (102 unique cities)
- **Users**: 389,894
- **Source**: U.S. Census 2017 data

## Usage in Paper

These datasets are used consistently across:
- Frequency-estimation evaluations
- Heavy-hitter evaluations
- Performance comparisons shown in Figure 4 (p. 10)
