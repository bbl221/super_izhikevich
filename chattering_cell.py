import izhikevich_cells as izh



class cCell(izh.izhCell):
    def __init__(self,stimVal):
        # Define Neuron Parameters
        super().__init__(stimVal)
        self.celltype= 'Chattering' 
        self.C=150
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=50
        self.vpeak=25
        self.stimVal = stimVal
    
myCell = cCell(4000)
myCell.simulate()
izh.plotMyData(myCell)