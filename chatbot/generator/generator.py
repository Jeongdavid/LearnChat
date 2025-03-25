
from llama_cpp import Llama
from typing import Iterator
from typing import Iterable


class Generator:
    def __init__(self) -> None:
        self.llm = Llama.from_pretrained(
            repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
            filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",  )

    def generate(self, prompt: str) -> Iterator[str]:
        self.llm = Llama.from_pretrained(
            repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
            filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",  )
        stream = self.llm(prompt, max_tokens=None, stream=True)

        for chunk in stream:
            yield chunk['choices'][0]['text']
