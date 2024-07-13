# Intel Unnati Vehicle Cut-In Detection

This project focuses on detecting vehicle cut-in events using the Intel Unnati platform. The detection of vehicle cut-ins is a critical aspect of advanced driver-assistance systems (ADAS) to enhance road safety and driving comfort.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Inference](#inference)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview
Vehicle cut-in detection involves identifying scenarios where a vehicle abruptly changes lanes and moves into the path of another vehicle, which can potentially lead to hazardous situations. This project uses machine learning techniques to predict and detect such events.

## Dataset
The dataset used for this project is the **IDD (Indian Driving Dataset)**. The dataset consists of annotated driving videos captured in various traffic conditions in India. The annotations include various driving events and object bounding boxes.

## Installation
To get started, clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/sukritraj02/Intel_Unnati-Vehicle-cut-in.git
cd Intel_Unnati-Vehicle-cut-in
pip install -r requirements.txt
```
## Usage
Preprocessing
Download the IDD dataset from the official website.
Extract the dataset and organize it as follows:
