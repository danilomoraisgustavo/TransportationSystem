
# Administrative Transportation System

## Overview

This project is an Administrative Transportation System, designed to efficiently manage and track vehicle fueling processes. It's a full-stack application with Flask powering the backend, a responsive front-end built with HTML, CSS, and JavaScript, and a MySQL database.

## Features

- **User Authentication:** A secure system for user login and registration.
- **Fueling Records Management:** Functionality to log and view details of vehicle fueling.
- **Responsive Design:** Fully responsive web pages for a seamless experience across various devices.
- **Theme Customization:** Users can choose between light and dark mode for personalized UI experience.

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL

## Project Structure

```plaintext
Administrative Transportation System/
│
├── static/
│   ├── login.css
│   ├── login.js
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── login.html
│   ├── index.html
│   └── user.html (in development)
│
├── app.py
└── sql.sql
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/danilomoraisgustavo/TransportationSystem
   ```

2. **Set up the database:**
   - Execute the `sql.sql` script in your MySQL environment.

3. **Install dependencies:**

   ```bash
   pip install flask mysql-connector-python
   ```

4. **Run the application:**

   ```bash
   python app.py
   ```

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

Danilo de Morais - [@your_twitter_handle](https://danilomorais.netlify.app/)
Project Link: [https://github.com/your-username/your-project-name](https://github.com/danilomoraisgustavo/TransportationSystem)
