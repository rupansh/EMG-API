# EMG Classification API

## Setup

Run from cmd:

```bash
python3 -m venv .venv
# For windows
.venv\Scripts\activate.bat
# For Linux
source .venv/bin/activate
```

## Start Server

```bash
uvicorn main:app --reload
```

## Request Example

```
POST /glove HTTP/1.1
Content-Type: application/json
accept: application/json

{"emg": [-1, 23, -31, 1, 2]}
```

```http
HTTP/1.1 200 Ok

{"fingers": [1, 1, 1, 1, 1]}
```

Curl example:

```
curl -X 'POST' \
    'http://127.0.0.1:8000/glove' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"emg": [0, 0, 0, 0, 0]}'
```
