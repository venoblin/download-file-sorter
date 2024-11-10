<a name="readme-top"></a>

[LinkedIn](https://www.linkedin.com/in/jonathanvillagomezhernandez/) |
[Website](https://www.jonweb.dev/)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  
  <h1 align="center">Download File Sorter</h3>

  <p align="center">
    Sorts files from download directory into user specified directories in a Unix based system!
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Download File Sorter is a Python script designed to automate the process of organizing downloaded files into predefined directories. By analyzing file extensions, the script intelligently sorts files into appropriate categories, such as Documents, Images, Videos, Music, and more. This saves you time and effort, keeping your downloads folder neat and organized.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
1. Create `settings.json` file in the project root directory
2. Add directories as so:
```json
{
  "downloads": "download directory",
  "destinations": {
    ".file_extension1": "destination directory",
    ".file_extension2": "destination directory",
    ".file_extension3": "destination directory"
  }
}
```
3. Run script with `python app.py`

<p align="right">(<a href="#readme-top">back to top</a>)</p>