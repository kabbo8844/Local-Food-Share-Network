# Local Food Surplus & Community Share Network

A beginner-friendly Python command-line project that helps record food donations and match them with volunteers in the same area.

## Features

- Add food donations
- Register volunteers
- View available food
- Match food with a volunteer in the same area
- Mark food as distributed
- Keep a distribution log in text files

## Requirements

- Python 3
- No external libraries required

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal in that folder.
4. Run:

   ```bash
   python main.py
   ```

   On some Windows computers, use:

   ```bash
   py main.py
   ```

## Project Files

- `main.py` — main program
- `food_data.txt` — saved food donation records
- `volunteer_data.txt` — saved volunteer records
- `distribution_log.txt` — distribution records

The text files are initially empty. The program adds data as you use it.

## Important Limitations

This is an educational beginner project. Matching is based on exact area-name matching, not GPS or actual distance. The program stores the expiry duration entered by the donor but does not automatically check whether food has expired. Food safety must be checked by responsible people before real-world distribution.

## Built With

- Python
- Lists and strings
- Functions and loops
- Conditional statements
- Basic file handling
