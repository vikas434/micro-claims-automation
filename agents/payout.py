from toolbox import Tool, AgentContext
payments = Tool.use("payments_rest")

def run(ctx: AgentContext):
    # In a real-world scenario, this would interact with a payment gateway
    # to issue an e-gift card or other form of credit.
    # For demonstration purposes, we'll simulate a successful payout.
    print(f"Issuing credit for order_id: {ctx.input["order_id"]}")
    ctx.output = ctx.input | {"payout_status": "success", "credit_amount": 9000}



