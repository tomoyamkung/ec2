from dataclasses import dataclass


@dataclass
class Instance:
    id: str
    name: str
    state: str
    instance_type: str

    def __init__(self, source) -> None:
        self.id = source.get("InstanceId")
        self.name = list(
            filter(lambda tag: "Name" in tag.values(), source.get("Tags"))
        )[0].get("Value")
        self.state = source.get("State").get("Name")
        self.instance_type = source.get("InstanceType")

    def __str__(self) -> str:
        state_string: str = "起動" if "running" == self.state else "停止"
        return f"- インスタンス {self.name} ({self.id}, {self.instance_type}) は {state_string} しています。"
