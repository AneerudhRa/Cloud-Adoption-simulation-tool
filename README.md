# Cloud Strategy Adoption Tool

This Flask application assists organizations in determining the most effective cloud adoption strategy based on their specific needs. The application gathers input on company size, budget, and IT infrastructure to provide tailored recommendations for cloud strategies.

## Application Overview

The application is built using Flask, a micro-framework for Python. It is designed to handle HTTP requests, process user inputs, and render cloud strategy recommendations based on the data provided.


## Features 

- **Dynamic Form-Based Inputs**: Collects essential information about the company size, budget, and existing IT infrastructure.
- **Tailored Recommendations**: Outputs specific cloud adoption strategies such as Rehost, Refactor, or Rebuild based on user inputs.
- **Responsive UI**: The user interface is built with Bootstrap, ensuring it is responsive and works well on both desktop and mobile devices.

## Getting Started 

### Prerequisites

- Python 3.8+
- pip for installing dependencies

### Installation

1. Clone the repository
2. pip install -r requirements.txt
3. python app.py

### Deployment 
This application is deployed on Azure App Service. To deploy your version, you can follow these general steps:

- Create or select an Azure App Service Plan.
- Configure the environment and deploy the application using FTP or through the Azure Portal.
- Set environment variables in the Azure portal under the "Configuration" settings of your App Service.

