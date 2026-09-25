Software Packaging  
Overview 
Welcome to my Software Packaging project! This repository serves as a “monorepo"—a single central folder that houses multiple
independent projects. 
The goal of this project is to demonstrate how software is properly prepared for production environments. This involves
downloading necessary building blocks (dependencies), scanning them for security vulnerabilities (auditing), and bundling the final
code into a single distributed file (packaging). 
I have configured three separate web applications using three of the most popular programming languages in the industry:
JavaScript (Node.js), Python, and Java. 
Repository Structure 
This repository contains three isolated environments organized as follows: 
Packaging_popular_frameworks/
├── README.md
├── node-app/
│ ├── package.json
│ ├── package-lock.json
│ ├── .env
│ ├── index.js # Express server entry point
│ └── node_modules/ # Local dependencies
├── python-app/
│ ├── requirements.txt
│ ├── manage.py # Django application runner
│ ├── venv/ # Isolated virtual environment
│ └── dist/ # Compiled distribution artifacts
│ ├── python_packaging_demo-1.0.0-py3-none-any.whl
│ └── python_packaging_demo-1.0.0.tar.gz
└── java-app/
├── pom.xml # Maven configuration and dependencies
├── src/ # Java Spring Boot source code
└── target/ # Compiled Java artifacts
└── demo-1.0.0.jar

Versioning Strategy 
Every application in this project uses Semantic Versioning (SemVer) and is currently set to version 1.0.0. Semantic versioning is an
industry standard that uses three numbers (Major.Minor.Patch) to communicate to users exactly what kind of changes have been
made to the software over time. 
Step-by-Step Instructions 
If you want to run these applications or see how they were built locally, follow the steps below. 
1. Node.js Environment (node-app/) 
Node.js uses a tool called npm (Node Package Manager) to handle its dependencies and scripts. 
Step 1: Setup and Security Check First, we download the necessary code dependencies and scan them for known security flaws. 
cd node-app
npm install # Downloads required dependencies
npm audit # Scans the downloaded files for security vulnerabilities

Step 2: Package and Run Next, we bundle the app into a compressed archive for distribution, and then start the server to test it. 
npm pack # Bundles the code into a distributable archive
npm start # Boots up the local web server
 Environment Verification: You can view the running service by navigating to http://localhost:3000 in your web browser.Artifact Generated: A distributable file named node-app-1.0.0.tgz is created in the directory. 
2. Python Environment (python-app/) 
Python uses a tool called pip to manage its packages. We use a virtual environment (venv) to keep our workspace clean and
isolated. 
Step 1: Setup and Security Check We activate our safe workspace, install our tools, and run a security scan. 
cd python-app
python3 -m venv venv # Creates an isolated workspace
source venv/bin/activate # Enters the workspace
pip install -r requirements.txt # Downloads required dependencies
pip install pip-audit # Installs the security scanner
pip-audit # Scans the Python dependencies for vulnerabilities

Step 2: Package and Run We use Python’s build tool to create our final distributable files, and then launch the Django server. 
python3 -m build # Bundles the application
python manage.py runserver 8000 # Boots up the local web server
 Environment Verification: You can view the running service by navigating to http://localhost:8000 in your web browser.
Artifacts Generated: Inside the dist/ folder, the build process generates a .whl (Wheel) file and a .tar.gz (Source Archive)
file.
(Note: To exit the Python workspace when finished testing, run the deactivate command). 
3. Java Environment (java-app/) 
Java uses a tool called Maven (mvn) to manage the build process. (Note: This project requires Java/OpenJDK version 21). 
Step 1: Setup and Security Check We configure the Java workspace and run a deep security scan using the OWASP Dependency
Check plugin, which cross-references our dependencies with the National Vulnerability Database (NVD). 
cd java-app
mvn clean install # Prepares the Java workspace
mvn org.owasp:dependency-check-maven:check # Runs the security audit

Step 2: Package and Run We compile the code into a single, runnable Java archive and launch it. 
mvn clean package # Compiles and bundles the application
java -jar target/demo-1.0.0.jar # Boots up the Java server
 Environment Verification: You can view the running service by navigating to http://localhost:8080 in your web browser.
(If port 8080 is occupied, run java -jar target/demo-1.0.0.jar --server.port=8081 and visit port 8081 instead).
Artifact Generated: Inside the target/ folder, a standalone executable named demo-1.0.0.jar is created. 
Release Assets 
Environment Verification: Screenshots verifying the successful initialization and active JSON payloads of all three local web
servers are documented within the repository.
Packaged Artifacts: The final compiled assets (.tgz, .whl, and .jar) have been published to the Releases section of this
GitHub repository under version v1.0.0.
