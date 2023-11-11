# WaveStamp_Audio_Extractor

This is a simple Flask web application.


## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
  

## Introduction

This Flask app is designed to extract Audio from the video and Watermark the video.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/) installed
- [Docker](https://www.docker.com/) installed (if running the app in a Docker container)
  

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/your-flask-app.git

2. Navigate to the project directory:

   cd your-flask-app

3. [If not using Docker] Install dependencies:

   pip install -r requirements.txt

4. Install ImageMagick:

   Follow the instructions on the [ImageMagick website](https://imagemagick.org/script/download.php) to download and install ImageMagick on your system.

5. For this app to work you need to create an directory called 'uploads' where your   uploaded video will be stored locally on your system. The path will be like this "app/uploads/". 


## Usage

To run the app:

1.  [If using Docker] Build the Docker image:

            docker build -t my-flask-app .

2.  [If using Docker] Run the Docker container:

             docker run -p 5000:5000 my-flask-app

    [If not using Docker] Run the app:

            python main.py

3.  Access the app in your web browser at [http://127.0.0.1:5000](http://localhost:5000).


## Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, please open an issue or create a pull request.
