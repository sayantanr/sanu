# Importing sendpdf function 
# From pdf_mail Library 
from pdf_mail import sendpdf 


# Create an object of sendpdf function 
k = sendpdf("##sender##email", 
            "###receiveremail###", 
            "##senderemailpassword##", 
            "##subject of message###", 
            "##bodyofmessage###", 
            "###filename###", 
            "###pathoffile###") 

# sending an email 
k.email_send()
