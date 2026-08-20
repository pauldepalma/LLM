import torch
class NeuralNetwork(torch.nn.Module):
	def __init__(self, num_inputs, num_outputs):
		super().__init__()
		
		self.layers = torch.nn.Sequential(
		#1st hidden layer
		torch.nn.Linear(num_inputs, 30),
		torch.nn.ReLU(),
	
        #2nd hiddenlayer
        torch.nn.Linear(30, 20),
        torch.nn.ReLU(),

        #output layer
		torch.nn.Linear(20,num_outputs),
		)
		
	def forward(self,x):
		logits = self.layers(x)
		return logits
		
if __name__ == "__main__":
	torch.manual_seed(123)
	model = NeuralNetwork(50,3)
	#print(model.layers[0].weight)
	X = torch.rand((1,50)) #Gen 50 random numbers in range [0.0, 1.0)
	out = model(X) #computes as if back prop is the next step
	print(out)
	#Computes as if its only feed forward
	with torch.no_grad():
		out = torch.softmax(model(X), dim=1)
	print(out)
	
