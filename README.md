<br/>
<div align="center">
<a href="https://github.com/user/repo">
<img src=".project-images/project-logo.png" alt="Logo" height="128px">
</a>
<h3 align="center">Download File Sorter</h3>
<p align="center">
Sorts files from download directory into user specified directories in a Unix based system! 
<br/>
<br/>
</p>
</div>

Table of Contents

- [About The Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)

## About The Project

Download File Sorter is a Python script designed to automate the process of organizing downloaded files into predefined directories in a Linux system. 
By analyzing file extensions, the script intelligently sorts files into user-defined directories, such as Documents, Images, Videos, Music, 
and more. This saves you time and effort, keeping your downloads folder neat and organized.

### Built With

This project was built with the following technologies:
- <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python" />

## Getting Started

### Installation

1. **Clone the repository** 

  ```sh
  git clone git@github.com:venoblin/download-file-sorter.git
  ```

2. **Create `settings.json` file in the project root directory**

  ```sh
  cd download-file-sorter
  touch settings.json
  ```

3. **Modify `settings.json`** 

  ```json
  {
    "downloads": "/path/to/Downloads",
    "destinations": {
      ".file-extension": "/path/to/destination",
      ".file-extension": "/path/to/destination",
      ".file-extension": "/path/to/destination"
    }
  }
  ```

4. **Run `app.py`** 
  
  ```sh
  python3 app.py
  ```