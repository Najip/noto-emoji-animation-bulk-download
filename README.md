# Noto Emoji Animation Bulk Download

This script allows for the automated downloading of animated emojis from the [Google Fonts' Noto Emoji](https://googlefonts.github.io/noto-emoji-animation/) project. It leverages Selenium for navigating the website, identifying the animations, and downloading them in bulk.

## Getting Started

These instructions will guide you in setting up the project on your local machine.

### Prerequisites

To run this script, ensure you have Python installed on your system. The script employs Selenium which necessitates a WebDriver for interfacing with the browser. ChromeDriver is utilized for this script.

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Najip/noto-emoji-animation-bulk-download.git
cd noto-emoji-animation-bulk-download
```

Install Selenium using pip:

```bash
pip install selenium
```


### Setting Up ChromeDriver

1. Download ChromeDriver from the [Chrome for Testing availability](https://googlechromelabs.github.io/chrome-for-testing/) site. Make sure to download the version that corresponds with your Chrome browser version.
2. Extract and place `chromedriver.exe` in a known directory on your computer.
3. In the `download.py` script, update the path to `chromedriver.exe`:

```python
chrome_driver_path = "path/to/chromedriver.exe"  # Update this path
```

### Running the Script

Execute the script with the following command:

```bash
python download.py
```

The script will begin downloading the animated emojis into a `downloaded_gifs` directory within the project folder.

## Technologies Used

* [Python](https://www.python.org/) - The programming language utilized.
* [Selenium WebDriver](https://www.selenium.dev/documentation/en/) - Utilized for automating web browser interaction.

## Contributing

Feel encouraged to contribute to this project. Any contributions are welcome. Please submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```
