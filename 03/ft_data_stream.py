import random
import typing


def gen_event(names: list[str], actions: list[str]) -> typing.Generator:
    while True:
        rand_name: str = random.choice(names)
        rand_action: str = random.choice(actions)
        yield (rand_name, rand_action)


def create_event_list(names: list[str], actions: list[str]) -> list[tuple[str, str]]:
    events_list: list[tuple[str, str]] = []
    event = gen_event(names, actions)
    for _ in range(10):
        events_list.append(next(event))
    return (events_list)


def consume_event(events_list: list[tuple[str, str]]) -> None:
    to_remove: tuple[str, str] = random.choice(events_list)
    print(f"Got event from list: {to_remove}")


def main() -> None:
    print("=== Game Data Stream Processor ===")
    actions: list[str] = ["run",
                          "eat",
                          "sleep",
                          "grab",
                          "move",
                          "climb",
                          "swim",
                          "release",
                          "use"]
    names: list[str] = ["bob",
                        "alice",
                        "dylan",
                        "charlie"]

    event = gen_event(names, actions)
    for i in range(1000):
        print(f"Event {i}: Player {next(event)[0]} did action {next(event)[1]}")
    events_list = create_event_list(names, actions)
    print(f"Built list of 10 events: {events_list}")


if __name__ == "__main__":
    main()
