# Shopify Insights Fetcher

## Overview
A FastAPI application to extract insights from any Shopify-based website without using the official API.

## Features
- Product catalog
- Hero products
- Contact details
- Social media handles
- About section
- Important links

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Usage

POST `/get_insights`
```json
{
  "website_url": "https://memy.co.in"
}
```