# SatFlora Django Project
![Land Cover Classification](link_to_image)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

The Django Land Cover Classification Project is a web application designed for land cover classification using multispectral images. This project allows users to select a Region of Interest (ROI) and analyze the evolution of land cover over time based on the provided multispectral images.

The application provides an intuitive and interactive interface to assist users in exploring land cover changes within the selected region. By utilizing advanced image processing and machine learning algorithms, it generates maps and statistics, providing valuable insights for environmental studies, urban planning, and agriculture.

## Features

- User-friendly web interface for selecting ROIs on the map.
- Supports uploading and management of multispectral image datasets.
- Automatic land cover classification using state-of-the-art machine learning models.
- Visualization of land cover changes over time using interactive maps.
- Statistical analysis of land cover evolution with graphs and charts.
- User authentication and authorization for secure access to datasets and results.
- Exporting of classification results and statistics for further analysis.

## Installation

Follow these steps to set up the Django Land Cover Classification Project on your local machine:

1. Clone the repository:

    ```bash
    git clone https://github.com/jams01/django_SatFlora.git
    cd django_SatFlora
    ```

2. Create a virtual environment and activate it (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
    ```
3. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```
4. Create a file `.env` into the folder `django_SatFlora` with your database parameters

    ```
    DB_NAME=<database-name>
    DB_USER=<database-user>
    DB_PASSWORD=<database-pass>
    DB_HOST=<database-host>
    DB_PORT=<database-port>
    ```
5. Create a file `firebase_credentials.json` in the root directory and place your Firebase configuration.

6. Perform databse migration

    ```bash
    python manage.py migrate
    ```

7. Create a user in firebase an then a user in django and set the username to the UID given in firebase:
    ```bash
    python manage.py createsuperuser
    ```

8. Run the server
    ```bash
    python manage.py runserver
    ```
## Usage

1. Under construction

## LICENSE

The SatFlora is licensed under the [MIT License](LICENSE). You are free to modify and distribute the codebase as per the terms of the license.