from prefect import flow, task
from datetime import date

@task
def create_message(msg: str) -> str:
    return msg + "!"


@flow
def time_message() -> str:

    today = date.today()

    full_msg = "Current date is " + str(today)

    return full_msg
@flow
def hello_world(msg: str) -> str:
    new_msg = create_message(msg)
    time_msg = time_message()
    full_msg = "This is my message: " + new_msg + " I'm sending it from Prefect!"
    print(full_msg)
    print(time_msg)

    return full_msg


if __name__ == "__main__":
    hello_world("Hace mazo calor aquí")


