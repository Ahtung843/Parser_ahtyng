import pandas as pd

def save_to_file(data: list, format_type: str, file_name: str):
    df = pd.DataFrame(data, columns=["Название", "Значение"])

    if format_type == "xlsx":
        df.to_excel(f"{file_name}.xlsx", index=False, engine="openpyxl")
        print(f"[SAVER] Успешно сохранен Excel: {file_name}.xlsx")

    elif format_type == "csv":
        df.to_csv(f"{file_name}.csv", sep=";", index=False, encoding="utf-8-sig")
        print(f"[SAVER] Успешно сохранен CSV: {file_name}.csv")

    elif format_type == "json":
        df.to_json(f"{file_name}.json", orient="records", force_ascii=False, indent=4)
        print(f"[SAVER] Успешно сохранен JSON: {file_name}.json")
