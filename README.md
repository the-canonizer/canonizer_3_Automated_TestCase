<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://canonizer3.canonizer.com">
    <img src="https://github.com/shahab-ramzan/read-me/blob/main/canonizer-fav.png" alt="Logo" width='80' >
  </a>
  <h3 align="center">Canonizer-3.0</h3>

  <p align="center">
    <br />
    <a href="https://canonizer3.canonizer.com/" style="color: #FFF;">View Demo</a>
    ·
    <a href="https://github.com/the-canonizer/canonizer-3.0-frontend/issues" style="color: #FFF;">Report Bug</a>
    ·
    <a href="https://github.com/the-canonizer/canonizer-3.0-frontend/issues" style="color: #FFF;">Request New Feature</a>
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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#contributing">Contributing</a>
      <ul>
        <li><a href="#Create-a-branch">Create a branch</a></li>
        <li><a href="#Make-the-change">Make the change</a></li>
        <li><a href="#Test-the-change">Test the change</a></li>
        <li><a href="#Push-the-change">Push the change</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![Product Name Screen Shot][product-screenshot]

A wiki system that solves the critical liabilities of Wikipedia. It solves petty "edit wars" by providing contributors the ability to create and join camps and present their views without having them immediately erased. It also provides ways to standardise definitions and vocabulary, especially important in new fields.

<p align="right">(<a href="#top">back to top</a>)</p>



## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- A system having OS Linux, Mac, or Windows
- System should have Python and PIP installed
- An IDE to setup the canonizer code, recommended PyCharm.

### Install Python and PIP

Generally, the Linux and Mac OS comes with the Python preinstalled. To verify whether the python is already installed or not, please run the below command on the terminal.

#### python
If it is installed in the host machine, then the following output will show.

*Python 3.10.3 (main, Jul 10 2022, 17:43:11) [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.*

If not installed, then you can install the python using the below command.


#### Ubuntu/Debian based OS
 sh
sudo apt-get install python3 
 
sh
sudo apt-get install python-pip
 
#### RedHat/CentOS
 sh
yum install python3

sh
yum -y install python-pip

#### Mac
sh
sudo apt-get install python3

sh
sudo apt-get install python-pip

#### Microsoft Windows
Visit the official website and download the installer of latest version of python and install it on the machine.

#### Install pip on Microsoft Windows
Download the  get-pip.py file and store it in the same python directory and run the below command.
sh
python3 get-pip.py



### Install/Upgrade Selenium
Verify whether the Selenium is already installed in the system or not, execute the below command.
- python3
- import selenium
If no error that means, we already have the Selenium installed. The above command also shows the version of the selenium installed. If it is not latest, then we need to upgrade it. Follow the below command to install or upgrade the Selenium.

#### To Install
sh
sudo pip3 install selenium

#### To Upgrade
sh
sudo pip3 install -U selenium;

### Install Chrome web-driver & web-driver manager
To install the Chrome web-driver, use the below command
#### Ubuntu/Debian
sh
apt install chromium-chromedriver

#### RedHat/CentOS
Download the package and run the command
sh
sudo yum install chromium-31.0.1650.63-1.el6.x86_64.rpm.

#### Mac OS
sh
apt install chromium-chromedriver

#### Microsoft Windows
Download from here and paste it in the project folder.

### Install IDE
The recommended IDE for Selenium with Python is PyCharm. It can be also configured with VSCode with the help of Python and Selenium extensions.
To install PyCharm, Download the required package or executable from the official website of PyCharm.

### Setting up project
Project can be setup in two ways in PyCharm IDE
- Clone the repository and pull the latest code into your file system and open the project by clicking on the File > Open menu option
- Import from the repository using Version Control System. 
        
        1. Click on the VCS > Get from Version Control
        2. Specify the repository URL
        3. Specify the directory where you want to clone the project in the machine
        4. Click on Clone button. 

Note: You must have the write access on the https://github.com/the-canonizer/canonizer_3_Automated_TestCase/. To get access on the repository please contact to Ashutosh Kukreti or Varun Gautam.






### Installation

1. Clone the repo
   sh
   git clone https://github.com/the-canonizer/canonizer-3.0-frontend.git
   
2. Go into the project root
   sh
   cd canonizer-3.0-frontend
   
3. Copy environment variables from `.env.example` to `.env` file
   sh
   cp .env.example .env
   
4. Install Dependency packages
   sh
   yarn
   
5. To start the hot-reloading development server
   sh
   yarn dev
   
6. To open the site in your favorite browser
   sh
   open http://localhost:4000
   

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->



<!-- LICENSE -->

## License

Lesser MIT License

Copyright (c) 2006-2023 Canonizer.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software with minimal restriction, including without limitation the rights to use, copy, modify, merge, publish, and distribute copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

Any activity arising from use under this license must maintain compliance with all related and dependent licensees.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

<!--
Distributed under the MIT License. See `LICENSE.txt` for more information.
 -->
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Brent Allsop - @Brent's_twitter - brent.allsop@gmail.com

Project Link: [https://canonizer3.canonizer.com](https://canonizer3.canonizer.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[product-screenshot]: https://github.com/shahab-ramzan/read-me/blob/main/Canonizer%20(1).png
