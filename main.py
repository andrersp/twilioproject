from twilio.rest import Client 
from pandas import read_excel
from time import sleep



df = read_excel('Listnumber.xlsx')

mynumber = df['Telefone']
account_sid = "AC016e01f4aea79352eb1a0ae87713697f"
auth_token = "03bf5e67c13234eb33827d6ddb5b47f0"
twilioNumber = '+13374545273'
called = '+55'


# Create your models here.
class Send():
    def __init__(self):
        self.auth_token = auth_token
        self.account_sid = account_sid
        self.twilioNumber = twilioNumber
        self.mynumber = mynumber       
        self.callCounter = 0
        self.limit = 0
        self.called = called

             

    def makeCall(self):
        client = Client(self.account_sid, self.auth_token)
        
        for i in mynumber:
            call = client.calls.create(
                to=i,
                from_=self.twilioNumber,
                twiml= """  
                            <Response>
                            <Say language='pt-BR'>
                                Escreva aqui o texto que deseja enviar                                                          
                            </Say> 
                            </Response>

                        """
                        )                

        
            self.callCounter = self.callCounter + 1
            print("Chamado # " + str(self.callCounter) + " Chamando número " + str(i))
            sleep(0.5)




    """ def set_target(self):
        self.called = str(input('Digite o número de telefone desejado: Use "+55" antes do número: '))
 """
        

def main():
    robo = Send()
    #robo.set_target()
    robo.makeCall()

if __name__ == '__main__':
    main()

