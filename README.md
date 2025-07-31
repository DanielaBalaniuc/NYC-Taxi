# NYC Taxi Streamlit App

This app loads and displays NYC taxi data from a large Parquet file.

## How to Run Locally

```bash
git clone https://github.com/yourusername/hf-docker-taxi-app.git
cd hf-docker-taxi-app
docker build -t taxi-app .
docker run -p 8501:8501 taxi-app
```

Then visit [http://localhost:8501](http://localhost:8501)
