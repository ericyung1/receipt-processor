# Receipt-Processor

This Flask-based web service processes receipt data, calculates reward points based on a set of rules, and provides a REST API to retrieve results. It is built with Python and can be deployed using Docker for ease of use.

## Getting Started

Follow the instructions below to run the project using Docker.

### 1. Clone the Repository

```
git clone https://github.com/your-username/receipt-processor.git
cd receipt-processor
```

### 2. Build the Docker Image
```
docker build -t receipt-processor .
```

### 3. Run the Docker Container
```
docker run -p 8000:8000 receipt-processor
```

## API Test Results

### GET Request Example
![GET Test](assets/get_test.png)

### POST Request Example
![POST Test](assets/post_test.png)
