## Setup

1) Copy env template and set your key:
~~~bash
cp .env.example .env
# open .env and set GEMINI_API_KEY
~~~

2) Run:
~~~bash
uv run main.py "Your prompt here"
~~~

Notes:
- .env is gitignored; .env.example is committed.
- Requires uv and Python as configured in this repo.

Then commit:
~~~bash
git add README.md
git commit -m "Docs: add setup instructions and env guidance"
git push
~~~