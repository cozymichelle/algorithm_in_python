'''
Implement Logistic Regression that performs similar to the sklearn implementation of Logistic Regression
'''

from sklearn.metrics import accuracy_score

class LogisticRegression():
    # Initialize parameters given input shape
    def initialize(self, X):
        self.d, self.n = X.shape
        self.coef_ = np.zeros((1, self.n))
        self.intercept_ = np.zeros(1)
    
    def sigmoid(self, X):
        return 1/(1 + np.exp(-(np.dot(X, self.coef_.T) + self.intercept_)))
    
    def compute_gradient(self, y, yhat, X):
        # gradient in m for all the data
        dl_dW = np.dot((yhat - 1), np.multiply(X, y.reshape(self.d, 1))) \
                + np.dot((1 - y), np.multiply(X, y.reshape(self.d, 1)))
        dl_dW *= (1 / self.d)
        
        # gradient in b for all the data
        dl_db = np.multiply(y, (yhat - 1)) + np.multiply((1 - y), yhat)
        dl_db = (1 / self.d) * np.sum(dl_db)
        
        return dl_dW, dl_db
    
    # Predict class labels for samples in X
    def predict(self, X):
        yhat = np.ravel(self.sigmoid(X))
        return np.asarray(yhat > 0.5).astype(int)
    
    # Probability estimates
    def predict_proba(self, X):
        one_proba = self.sigmoid(X)
        zero_proba = np.ones(one_proba.shape) - one_proba
        return np.column_stack((zero_proba, one_proba))
    
    # Return the mean accuracy
    def score(self, X, y):
        return accuracy_score(y, self.predict(X))
    
    # Fit the model according to the given training data
    def fit(self, X, y, learning_rate = 0.005, epochs = 3000, verbose = False):
        if verbose:
            print("Initialize parameters")
        self.initialize(X)
        
        if verbose:
            print("Training...")
        for epoch in range(epochs):
            if verbose:
                if epoch % 500 == 0:
                    print("\tepoch ", epoch + 1)
            
            # Generate predictions
            yhat = np.ravel(self.predict_proba(X)[:, 1])
            
            # Compute the gradients:
            dl_dW, dl_db = self.compute_gradient(np.asarray(y), yhat, X)
            
            # Perform gradient descent
            self.coef_ -= learning_rate * dl_dW
            self.intercept_ -= learning_rate * dl_db

        return self