from fastapi import FastAPI, HTTPException
from utils import run_query

app = FastAPI()

@app.get("/sales_by_city")
def sales_by_city():
    query = """
    SELECT city, SUM(Sales) AS sales
    FROM workspace.default.supermarket_sales
    GROUP BY city
    ORDER BY sales DESC
    """
    try:
        rows = run_query(query)
        # Convert to list of dicts
        result = [{"city": r[0], "sales": r[1]} for r in rows]
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Azure auto-start
if __name__ == "__main__":
    import uvicorn
    # Listen on all interfaces, port 8000
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")