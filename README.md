# Komba - Your Smart South African Taxi Navigator

## Introduction
Komba is a mobile application designed to enhance the navigation experience within South Africa's minibus taxi system. It provides real-time predictions of pick-up and departure times, suggests the nearest taxi ranks, and helps users discover points of interest along their routes. The app aims to simplify public transportation for both locals and tourists, promoting responsible tourism and supporting local businesses.

## Deployment
You can access the deployed version of the application here: [Komba App](https://github.com/gomolemontlhane/komba_app/blob/main/login.html)

## Blog Article
Read more about the development and features of Komba in our blog post: [Komba Development Blog](https://www.linkedin.com/pulse/blog-post-alx-komba-portfolio-project-gomolemo-ntlhane-qzqkf/)

## Author(s)
- [Gomolemo Ntlhane](https://www.linkedin.com/in/gomolemontlhane)

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gomolemontlhane/komba_app.git
   ```

2. **Navigate to the project directory**:
      ```bash
      cd koma_app
      ```

3. **Install the required packages: Make sure you have Python and pip installed, then run:**

```bash
pip install -r requirements.txt
```

4. **Run the applicatoin: Start the Flask server with the command**

```bash
flask run
```
## Project Structure

```graphql
komba_app/
│
├── app.py                    # Main application file
├── background.jpg            # Background image
├── komba_bg.jpg              # Additional background image
├── lock_FILL1_wght400_GRAD0_opsz24.svg  # SVG icon for lock
├── person_FILL1_wght400_GRAD0_opsz24.svg # SVG icon for person
├── models/                   # Directory for data models
│   └── models.py             # Data models
├── static/                   # Directory for static files
│   ├── images/               # Directory for images
│   ├── scripts.js            # JavaScript functionalities
│   └── style.css             # CSS styles
└── templates/                # Directory for HTML templates
    ├── home.html            # Home page
    ├── login.html           # Login page
    ├── signup.html          # Signup page
    └── success.html         # Success page
```

## Usage

1. **Running the Application:**
- Start the flask applicatoin by running:
   ```bash
   python app.py
   ```
- Open your web browser and navigate to http://127.0.0.1:5000/

2. **Login Page:**

- Navigate to /login to access the login page.
- Enter your credentials to log in.

3. **Signup Page:**

- Navigate to /signup to access the signup page.
Register a new account by providing the required information.

4. **Home Page:**
- Upon successful login, users will be redirected to the home page.

5. **Success Page:**
- After signup or successful actions, users will be redirected to the success page.

## Contributing
We welcome contributions to improve Komba. To contribute:

1. Fork the repository on GitHub.
2. Create a new branch for your changes.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a clear description of the changes.

For major changes or feature requests, please open an issue first to discuss the proposed changes.

## Licensing
This project is licensed under the MIT License. See the LICENSE file for more details.

## Screenshots
![Komba Login Page](./screenshot.png)
