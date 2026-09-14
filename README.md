# History of Y Combinator

CS122 project. What factors are indicators of a successful Y Combinator startup?

Team: Tiffany Tran, Abhiram Segu

## Dataset

Y Combinator Startups Full Directory 2005-2026, from Kaggle:
https://www.kaggle.com/datasets/alibekmamyrbay/y-combinator-startups-full-directory-20052026

5,884 companies, 31 columns, one CSV. The CSV is not committed. Download it with the steps below.

## Setup

Create the virtual environment:

```
python3 -m venv .venv
```

Install the dependencies:

```
.venv/bin/pip install -r requirements.txt
```

Log in to Kaggle once. Copy `.env.example` to `.env` and fill in your Kaggle username and API key from https://www.kaggle.com/settings.

```
cp .env.example .env
```

Download the data into `data/`:

```
.venv/bin/python download_data.py
```

## Layout

- `data/` downloaded CSV, ignored by git
- `notebooks/` exploratory analysis
- `src/` source code
- `download_data.py` pulls the Kaggle dataset into `data/`
