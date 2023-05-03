import time
from contextlib import contextmanager


class BaseProvider:
    """Base class for all providers.
    Methods will raise NotImplementedError if they are not overwritten.
    """

    def __repr__(self) -> str:
        return f"{self.__name__} ({self.model})"

    def __str__(self):
        return f"{self.__name__} ({self.model})"

    @contextmanager
    def track_latency() -> float:
        start = time.perf_counter()
        yield time.perf_counter() - start

    def compute_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        cost_per_token = self.MODEL_INFO[self.model]
        cost = (
            (prompt_tokens * cost_per_token["prompt"]) +
            (completion_tokens * cost_per_token["completion"])
        ) / 1_000_000
        return cost

    def count_tokens(self):
        raise NotImplementedError(
            f"Count tokens is currently not supported with {self.__name__}"
        )

    def complete(self):
        raise NotImplementedError

    async def acomplete(self):
        raise NotImplementedError(
            f"Async complete is not yet supported with {self.__name__}"
        )

    def complete_stream(self):
        raise NotImplementedError(
            f"Streaming is not yet supported with {self.__name__}"
        )

    async def acomplete_stream(self):
        raise NotImplementedError(
            f"Async streaming is not yet supported with {self.__name__}"
        )