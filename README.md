# Local Food Share Network

A command-line interface (CLI) application built with Python to bridge the gap between food donors and local volunteers. The core objective of this project is to minimize food waste by streamlining the collection and distribution process within local communities.

## Core Features

- **Food Donation Management:** Donors can securely list surplus food, specifying the item name, quantity, pickup location, and estimated shelf-life/expiration hours.
- **Volunteer Registration:** Volunteers can register their profiles with their service locations and contact information.
- **Smart Area Matching:** Automatically pairs available food donations with registered volunteers in the same geographic location.
- **Distribution Tracking:** Allows administrators to mark food items as distributed, instantly updating the inventory and generating a permanent transaction log.
- **Audit & Activity Logs:** Keeps a detailed record of all successfully distributed food items for transparency and reporting.

## Project Architecture & Storage

This application follows a lightweight, file-based data persistence pattern. It does not require any external database setup and automatically manages the following local text files during runtime:
- `food_data.txt` - Stores food donation records and their current status.
- `volunteer_data.txt` - Stores registered volunteer profiles and locations.
- `distribution_log.txt` - Maintains the historical log of completed distributions.

## Getting Started

### Prerequisites
- Make sure you have **Python 3.x** installed on your system. No external libraries or dependencies are required as the project uses Python's built-in standard libraries (e.g., `os`).

### Limitations

* Volunteer matching is based on exact location-name matching.
* The program does not calculate actual distance or use GPS.
* Food expiry duration is stored, but automatic expiry checking is not implemented.
* Food safety should be checked by responsible people before distribution.

### Running the Application

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt inside the project directory.
3. Run the application using the following command:
   ```bash
   python main.py
