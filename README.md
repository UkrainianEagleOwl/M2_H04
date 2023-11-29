
# Simple Web App with UDP Socket Communication

## Overview
This project is a basic web application that serves two HTML pages (`index.html` and `message.html`) and handles static resources like CSS and images. It also includes a UDP socket server for processing data submitted through a form on `message.html`. The app runs on port 3000, and the socket server operates on port 5000.

## Features
- **Web Application**:
  - Routing for `index.html` and `message.html`.
  - Handles static resources: `style.css`, `logo.png`.
  - Custom 404 Not Found page using `error.html`.
- **Form Handling and Data Processing**:
  - Processes form data from `message.html`.
  - Communicates with a UDP socket server to process and store form data.
- **UDP Socket Server**:
  - Receives data from the web application.
  - Converts byte strings to a dictionary.
  - Stores data in `data.json` under the `storage` directory with a timestamp.
- **Multithreading**:
  - Runs HTTP and Socket servers in separate threads.

## Application Structure
```
project/
├── main.py              # Main application script
├── storage/
│   └── data.json        # JSON file for storing form data
└── templates/           # HTML templates for the web application
    ├── index.html
    ├── message.html
    └── error.html
```

## Usage
1. **Starting the Application**:
   - Run `main.py` to start both the web and socket servers.
   - Access the web application at `http://localhost:3000`.

2. **Interacting with the Application**:
   - Navigate to `http://localhost:3000/message.html`.
   - Fill out the form and submit. The data will be processed by the socket server and stored in `data.json`.

3. **Viewing Stored Data**:
   - Data sent through the form is stored in `storage/data.json` with timestamps.

## Installation
Clone the repository and ensure Python is installed. Dependencies may include web frameworks and libraries for handling UDP sockets.

## Development and Testing
- Test the routing of web pages and the serving of static files.
- Ensure the form on `message.html` correctly submits data to the socket server.
- Verify that `data.json` correctly logs the submitted data with timestamps.

---

This README provides a comprehensive guide on the functionality, structure, installation, and usage of the Simple Web App with UDP Socket Communication, adhering to the specified technical task requirements.
