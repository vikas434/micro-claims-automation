from toolbox import Tool, AgentContext
sql = Tool.use("mcp_sql")

def run(ctx: AgentContext):
    row = sql.query_one(
        "SELECT warranty_end FROM purchases "
        "WHERE order_id = %s", (ctx.input["order_id"],)
    )
    if row and row["warranty_end"] >= ctx.input["ts"]:
        ctx.output = ctx.input | {"eligible": True}
    else:
        ctx.abort("Warranty expired.")



