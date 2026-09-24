# Software Packaging Foundations

## Overview
This repository is a multi-language monorepo demonstrating standard packaging, dependency management, and security auditing practices for Node.js, Python, and Java applications. 

## Project Structure
The repository contains three isolated application environments:
* `node-app/`: A JavaScript environment using Node.js and Express.
* `python-app/`: A Python environment using Django and virtual environments (`venv`).
* `java-app/`: A Java environment using Spring Boot and Maven (Java 21).

## Versioning Strategy
Semantic Versioning (`v1.0.0`) was implemented across all three applications to ensure consistent and predictable release tracking.

---

## Build and Audit Instructions

### 1. Node.js Environment
**Setup & Audit:**
```bash
cd node-app
npm install
npm audit
```
**Packaging & Running:**
```bash
npm pack
npm start
```
*Artifact generated: `node-app-1.0.0.tgz`*

### 2. Python Environment
**Setup & Audit:**
```bash
cd python-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install pip-audit
pip-audit
```
**Packaging & Running:**
```bash
python3 -m build
python manage.py runserver 8000
```
*Artifacts generated in `dist/`: `.whl` and `.tar.gz` files.*

### 3. Java Environment
*Note: Requires OpenJDK 21.*

**Setup & Audit:**
```bash
cd java-app
mvn clean install
mvn org.owasp:dependency-check-maven:check
```
*Note: The OWASP plugin is configured to use the NVD database (v12.1.0).*

**Packaging & Running:**
```bash
mvn clean package
java -jar target/demo-1.0.0.jar
```
*If port 8080 is occupied (e.g., by Jenkins), append `--server.port=8081` to the run command.*
*Artifact generated in `target/`: `demo-1.0.0.jar`*