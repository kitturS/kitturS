#Design a ‘book’ class with title, author, publisher, price and author’s royalty as instance variables. Provide getter and
#setter properties for all variables. Also define a method royalty() to calculate royalty amount author can expect to receive
#the following royalties:10% of the retail price on the first 500 copies; 12.5% for the next 1,000 copies sold, then 15% for all
#further copies sold.
#Then design a new ‘ebook’ class inherited from ‘book’ class. Add ebook format (EPUB, PDF, MOBI etc) as additional instance variable
#in inherited class. Override royalty() method to deduct GST @12% on ebooks

class book:
    def __init__(self,a,b,c,d,e):
        self.title = a
        self.author = b
        self.publisher = c
        self.price = d
        self.sold= e

    @property   
    def getdetails(self):
        return self.title, self.author, self.publisher, self.price, self.sold

    
    def setdetails(self,a,b,c,d,e):
        self.title = a
        self.author = b
        self.publisher = c
        self.price = d
        self.sold= e
        
    royalty=0
    def royalty(self):
        
        if self.sold<=500:
            royalty = 0.1*self.price*500
            
        elif self.sold>500 and self.sold<1000:
            royalty = 0.1*self.price*500 + 0.125*self.price*(self.sold-500)
            
        else:
            royalty = 0.1*self.price*500+0.125*self.price*100+0.15*self.price*(self.sold-1500)

        print("Royalty={}".format(royalty))
            
class ebook(book):
    def __init__(self,a,b,c,d,e,f):
        super().__init__(a,b,c,d,e)
        self.format=f

    def getformat(self):
        return self.format
    def setformat(self,x):
        self.format=x
        
    royalty=0
    def royalty(self):
        if self.sold<=500:
            royalty = 0.1*self.price*500
            
        elif self.sold>500 and self.sold<1000:
            royalty = 0.1*self.price*500 + 0.125*self.price*(self.sold-500)
            
        else:
            royalty = 0.1*self.price*500+0.125*self.price*100+0.15*self.price*(self.sold-1500)
        royalty = 0.88*royalty
        print("Royalty={}".format(royalty))
    
    
        
