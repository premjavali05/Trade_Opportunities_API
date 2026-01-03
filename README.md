# Trade Opportunities API

## Overview

Trade Opportunities API is a Python-based backend application built using FastAPI that analyzes Indian market sectors and generates AI-powered trade opportunity reports. The system dynamically fetches real-time, sector-specific news using a search API and applies a Large Language Model (LLM) to produce structured, readable market insights in Markdown format.

This project demonstrates backend API development, real-time data collection, AI integration, security implementation, and clean code organization.

---

## Features

- ✅ Accepts a market sector as input (e.g., pharmaceuticals, technology, agriculture)
- ✅ Fetches real-time, updated sector-related news using an external search API
- ✅ Uses an AI model (Google Gemini) to analyze current market information
- ✅ Generates a structured Markdown market analysis report
- ✅ Implements token-based authentication
- ✅ Includes in-memory rate limiting to prevent abuse
- ✅ Handles errors gracefully and follows clean architecture principles

---

## Tech Stack

- **Python** - Core programming language
- **FastAPI** - Modern web framework for building APIs
- **Google Gemini API** - Large Language Model for analysis
- **SerpAPI** - Real-time news search
- **HTTPX** - Async HTTP client
- **Uvicorn** - ASGI server

---

## API Endpoint

### `GET /analyze/{sector}`

#### Example Request
```http
GET /analyze/pharmaceuticals
Authorization: Bearer demo-token
```

#### Example Response

The API returns a structured Markdown report containing:

- Overview
- Current Market Trends
- Trade Opportunities
- Risks
- Conclusion

---

## How It Works

1. The user sends a request with a sector name
2. The system fetches the latest market news related to that sector using a search API
3. The collected news data is passed to a Large Language Model for analysis
4. The AI generates a structured Markdown report based strictly on the fetched news
5. The report is returned as a plain text response

---

## Security

- 🔒 Token-based authentication using HTTP Bearer tokens
- 🔒 Input validation for API parameters
- 🔒 In-memory rate limiting per user/session
- 🔒 No sensitive credentials are committed to the repository

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/trade-opportunities-api.git
cd trade-opportunities-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file using `.env.example` as reference and add your API keys:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SERP_API_KEY=your_serp_api_key_here
AUTH_TOKEN=demo-token
```

### 5. Run the application
```bash
uvicorn main:app --reload
```

### 6. Access the API documentation

Open your browser and navigate to:
```
http://127.0.0.1:8000/docs
```

---

## Notes

- The application uses in-memory storage only (no database)
- Real-time data is fetched dynamically for every request
- AI analysis is based strictly on fetched news to avoid generic output
- A fallback mechanism is implemented in case the AI service is unavailable

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Contact

For questions or feedback, please open an issue on GitHub.