from toolbox import Tool, AgentContext
vision = Tool.use("gemini_vision")

PROMPT = ("Classify damage type and severity (0-10) "
          "for this consumer-electronics photo; "
          "return JSON with keys damage_type, severity.")

def run(ctx: AgentContext):
    res = vision.generate(prompt=PROMPT, images=[ctx.input["photo"]])
    ctx.output = ctx.input | res.json()



