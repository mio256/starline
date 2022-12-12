以下は最新バージョンにて修正されている

Clientをreturn_type=Responseをすると、Paginatorが動作しない。
そのため、`venv/lib/python3.10/site-packages/tweepy/pagination.py`の100行目を書き換える。
```python
        try:
            self.previous_token = response.json()["meta"]["previous_token"]
        except KeyError:
            self.previous_token = None
        self.next_token = response.json()["meta"]["next_token"]
```