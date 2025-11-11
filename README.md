# SIFT Extractor

A lightweight Dockerized tool for extracting **SIFT (Scale-Invariant Feature Transform)** features from images.  

## 🧱 Build the Docker Image

Clone the repository and build the Docker image:

```bash
docker build -t sift-extractor .
```

## 🚀 Run the Extractor

Run the container, mounting your local image folder and output directory:

```bash
docker run --rm   -v local_path/to/images:/app/images   -v $(pwd)/results:/app/output   sift-extractor
```

### Arguments:
- `local_path/to/images`: Path to your local directory containing images.  
- `$(pwd)/results`: Directory where extracted SIFT features will be saved.  

## 📁 Output

The extracted feature data will be available in the mounted `results` directory after processing.

## 🧩 Requirements

- [Docker](https://docs.docker.com/get-docker/) installed on your system.  

## 📝 License

This project is licensed under the [MIT License](LICENSE).
