from reasoning import ReasoningSystem

reasoning_system = ReasoningSystem()
caption = 'one full transparent rectangular plastic jar with a twist finish and a twist closure'

affordances = reasoning_system.infer_affordances(caption=caption)
print(affordances)