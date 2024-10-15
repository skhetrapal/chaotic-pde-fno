import numpy as np
import torch
      
class npzloader(object):
    def __init__(self, path, device='cpu'):
        super(npzloader,self).__init__()
        self.path = path
        self.device = device
        
#    def unpack(self):
#        data= self.load()
#        # Check if 'x' and 'y' are valid keys and have correct data type
#        if 'x' in data and 'y' in data and isinstance(data['x'], np.ndarray) and isinstance(data['y'], np.ndarray):
#            x,y = data['x'].astype(np.float32), data['y'].astype(np.float32)
#        else:
#            # Handle the case where keys are not found or have invalid type
#            # For example, you could raise an exception or return default values
#            raise ValueError("Invalid data format: 'x' and 'y' keys not found or have incorrect data type")
#        return [x,y]
    
    def unpack(self):
        data = self.load()
        if isinstance(data, np.ndarray):
            # Assuming the data is already in the desired format (e.g., [N, T, H, W])
            x = data[:, :-1, :, :]
            y = data[:, 1:, :, :]
            return x, y
        else:
            # Handle cases where the data is a dictionary or other format
            x = data['x'].astype(np.float32) if 'x' in data else None
            y = data['y'].astype(np.float32) if 'y' in data else None
            if x is None or y is None:
                print("Error: 'x' or 'y' not found in the loaded data.")
            return x, y

        
    def load(self):
        return np.load(self.path)
    
    def toTensor(self):
        datasetList = self.unpack()
        dataset = [torch.from_numpy(item).to(self.device) for item in datasetList]
        return dataset
    
    def split(self, ntrain, nval, ntest):
        dataset = self.toTensor()

        # dataset = self.data()  #[x,y]
        samples = len(dataset[0]) #total samples in dataset
        # print(dataset[0].shape)
        # print(dataset[1].shape)

        x  = dataset[0]
        y =  dataset[1]

        xtest = x[-ntest:]
        ytest = y[-ntest:]
        ## if ntrain and ntest split 
        if ntrain + ntest + nval > samples:
            raise Exception ("Invalid ntrain, nval and ntest")
        shuffle = torch.randperm(samples-ntest)  ##  get indices to shuffle dataset
        ntrain = shuffle[:ntrain] 
        nval = shuffle[-nval:]

        xtrain, xval = x[ntrain] , x[nval] 
        ytrain, yval = y[ntrain] , y[nval]

        ## delete dataset from memory
        del x
        del y

        return [xtrain, ytrain, xval, yval, xtest, ytest]
    
    def split(self, ntrain, nval, ntest):
        dataset = self.toTensor()

        # dataset = self.data()  #[x,y]
        samples = len(dataset[0])

        x  = dataset[0]
        y =  dataset[1]

        xtest = x[-ntest:]
        ytest = y[-ntest:]
        ## if ntrain and ntest split 
        if ntrain + ntest + nval > samples:
            raise Exception ("Invalid ntrain, nval and ntest")
        shuffle = torch.randperm(samples-ntest)  ##  get indices to shuffle dataset
        ntrain = shuffle[:ntrain] 
        nval = shuffle[-nval:]

        xtrain, xval = x[ntrain] , x[nval] 
        ytrain, yval = y[ntrain] , y[nval]

        ## delete dataset from memory
        del x
        del y

        return [xtrain, ytrain, xval, yval, xtest, ytest]
    
    def cpu(self, tensor):
        return tensor.cpu()
    
    def cuda(self, tensor):
        return tensor.to(self.device)
