from typing import Iterator
from llama_cpp import Llama  # Assuming llama_cpp is the library being used

class Generator:
    def __init__(self) -> None:
        # Llama 모델을 초기화합니다.
        self.llm = Llama.from_pretrained(
            repo_id="bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF",
            filename="DeepSeek-R1-Distill-Qwen-1.5B-IQ2_M.gguf",
        )

    def generate(self, prompt: str) -> Iterator[str]:
        # Llama 모델을 사용하여 프롬프트에 기반한 텍스트를 생성합니다.
        response = self.llm.generate(prompt, max_tokens=50)  # max_tokens는 필요에 따라 조정
        text = response["text"]  # 모델의 응답에서 텍스트를 추출

        # 텍스트를 단어 단위로 나누어 하나씩 반환
        from time import sleep
        for chunk in text.split():
            sleep(0.1)  # 토큰 간의 지연 시간 추가
            yield chunk
            yield ' '

