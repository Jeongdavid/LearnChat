import json


class Retrieval:
    def __init__(self, data_path: str = "./data/newjeans.json"):
        with open(data_path, "r") as file:
            data: dict[str, str] = json.load(file)
            self.data = data

    def retrieve(self, query: str) -> str | None:
        '''
        query가 JSON 데이터의 key를 포함하면 "{key}: {value}"를 반환.
        포함하지 않으면 None을 반환.....
        '''
        for key, value in self.data.items():
            if key.lower() in query.lower():
                return f"{key}: {value}"
        return None


    def print_data(self) -> None:
        print(self.data)