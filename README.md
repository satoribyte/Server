# Server

This repository contains code to run a simple HTTP server that can execute PHP scripts and send responses to incoming GET requests.

## Requirements

Make sure you have the following programs installed on your system before running this repository:

- Python
- PHP
- Subprocess
- Wget

## Installation

1. Install the required packages by running the following command:

`pkg install python`

`pkg install php`

`pkg install subprocess`

`pkg install wget`


2. Download ngrok with the command:

`wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip`


3. Extract the downloaded ngrok archive:

`unzip ngrok-stable-linux-arm.zip`


4. Remove the ngrok zip file that is no longer needed:


`rm ngrok-stable-linux-arm.zip`


5. Move the ngrok file to the bin directory for global accessibility:

`mv ngrok $PREFIX/bin/`


6. Set ngrok authentication with your token:

`ngrok authtoken <Your Authtoken>`


## Running the Server

1. Open a terminal and navigate to the directory of this repository.

2. Start the server with the command:

`python app.py`


3. The server will start running on port 4646.

4. To access the server from the internet, open a new terminal and execute the following command to connect ngrok to the server:

`ngrok http 4646`


5. Ngrok will generate a forwarding URL that you can use to access the server remotely.

6. Test the server by sending GET requests to the provided ngrok URL or by accessing it locally at `http://localhost:4646`.

7. Press Ctrl+C in the terminal running the server to stop it.

## Developer

This repository is developed by Deni Gentara.

Connect with me on Instagram: [@denigentarcandana.id](https://www.instagram.com/denigentarcandana.id/)

