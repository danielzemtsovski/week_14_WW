from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io
import models1
from db import push_to_db

app = FastAPI()
db_conn = push_to_db()
###

# @app.post("/upload")
# def file(file: UploadFile = File(...)):
#     df = pd.read_csv(io.BytesIO(file.file.read()))
#     df = models1.add_colums(df)
#     df = models1.replacing_None_to_Unknown(df)
#     df = df.where(pd.notnull(df), None)

#     cursor = db_conn.cursor()
#     insert = """
#         INSERT INTO my_table (
#             weapon_id, weapon_name, weapon_type,
#             range_km, weight_kg, manufacturer,
#             origin_country, storage_location,
#             year_estimated, level_risk
#         ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#     """
#     records = [
#         (row.weapon_id,
#          row.weapon_name,
#          row.weapon_type,
#          row.range_km,
#          row.weight_kg,
#          row.manufacturer,
#          row.origin_country,
#          row.storage_location,
#          row.year_estimated,
#          row.risk_level)
#         for row in df.itertuples(index=False)
#     ]
#     cursor.executemany(insert, records)
#     db_conn.commit()
#     return {"status": "success","inserted_records": len(records)}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8010)

@app.post("/upload")
def file(file: UploadFile = File(...)):
    df = pd.read_csv(io.BytesIO(file.file.read()))
    df = models1.add_colums(df)
    df = models1.replacing_None_to_Unknown(df)
    df = df.where(pd.notnull(df), None)

    cursor = db_conn.cursor()
    insert = """
        INSERT INTO my_table (
            weapon_id, weapon_name, weapon_type,
            range_km, weight_kg, manufacturer,
            origin_country, storage_location,
            year_estimated, level_risk
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""  
    records = [
        (row.weapon_id,
         row.weapon_name,
         row.weapon_type,
         row.range_km,
         row.weight_kg,
         row.manufacturer,
         row.origin_country,
         row.storage_location,
         row.year_estimated,
         row.risk_level)
        for row in df.itertuples(index=False)]
    cursor.executemany(insert, records)
    db_conn.commit()
    return {"status": "success","inserted_records": len(records)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8010)




