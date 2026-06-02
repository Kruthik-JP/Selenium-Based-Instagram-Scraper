# Selenium-Based-Instagram-Scraper
Automated Instagram image downloader built using Python, Selenium, BeautifulSoup, and Requests. The tool logs into Instagram, navigates to a target profile, extracts image URLs, and downloads uploaded images automatically.
# Instagram Profile Image Downloader

## Overview

This project automates the process of downloading images from an Instagram profile. The application uses Selenium WebDriver for browser automation, BeautifulSoup for HTML parsing, and Requests for downloading image content.

### Features

* Automated Instagram Login
* Secure Credential Management with .env
* Dynamic Profile Navigation
* Infinite Scrolling Support
* Automatic Image URL Extraction
* Duplicate Image Detection
* Bulk Image Downloading
* Organized Local Storage

### Technologies Used

* Python
* Selenium
* BeautifulSoup4
* Requests
* python-dotenv

### Workflow

1. Load credentials from environment variables.
2. Launch Chrome browser using Selenium.
3. Log in to Instagram automatically.
4. Open the target Instagram profile.
5. Parse dynamically loaded content using BeautifulSoup.
6. Extract image URLs from posts.
7. Download images locally.
8. Continue scrolling until all available images are collected.

### Learning Outcomes

* Web Automation
* Dynamic Web Scraping
* Browser Control with Selenium
* HTML Parsing
* Python File Handling
* Environment Variable Management
* Data Extraction Techniques
