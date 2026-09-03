"""每 token 请求频率限制（内存，演示/测试用）。"""


class RateLimiter:
    def __init__(self, max_calls=5):
        self.max_calls = max_calls
        self._counts = {}

    def check(self, key):
        n = self._counts.get(key, 0)
        if n >= self.max_calls:
            return False
        self._counts[key] = n + 1
        return True

    def reset(self, key=None):
        if key is None:
            self._counts.clear()
        else:
            self._counts.pop(key, None)
