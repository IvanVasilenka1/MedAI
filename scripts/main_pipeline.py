from myapp.services.agent_service import MedicalAgent
agent = MedicalAgent()

result = agent.run("I have fever and sore throat for 2 days")

print(result)