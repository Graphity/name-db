from fastapi import FastAPI

import json
import random

app = FastAPI()


@app.get("/generate")
def generate_names(gender: str | None = None, limit: int | None = 5):
    with open("names.json") as f:
        data = json.load(f)

    if limit < 1:
        limit = 1
    else:
        limit = min(limit, 100)

    if gender and gender in "MF":
        selected = True
    else:
        selected = False

    generated_names = []

    for _ in range(limit):
        if not selected:
            gender = random.choice(["M", "F"])
        first_name = random.choice(data["first_names"][gender])
        last_name = random.choice(data["last_names"])
        generated_names.append(
            {"name": f"{first_name} {last_name}", "gender": gender}
        )

    return {"limit": limit, "names": generated_names}
