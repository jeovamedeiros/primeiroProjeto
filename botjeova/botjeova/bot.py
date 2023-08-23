"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""
import botcity
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("http://www.discord.com")
        self.execute(r'C:\Users\jeeov\OneDrive\Área de Trabalho\Discord.lnk')
        if not self.find( "pesquisar_amigos", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar_amigos")
        self.click()

        if not self.find( "encontrar_amigos", matching=0.97, waiting_time=10000):
            self.not_found("encontrar_amigos")
        self.click()
        self.click()
        self.click()
        self.paste("dg")
        if not self.find( "dg", matching=0.97, waiting_time=10000):
            self.not_found("dg")
        self.click()
        if not self.find( "digitarMensagem", matching=0.97, waiting_time=10000):
            self.not_found("digitarMensagem")
        self.click()
        self.paste("Eai mano, só estou testando mesmo o programa que estou conhecendo rs AUTOMATIZANDOOOOOOO")


        self.enter()



        # FAZENDO O SEGUNDO BOT TESTE
        self.browse("https://www.hashtagtreinamentos.com")

        
        if not self.find( "Curso_Python", matching=0.97, waiting_time=10000):
            self.not_found("Curso_Python")
        self.click()
        if not self.find( "carregar_Pagina", matching=0.97, waiting_time=10000):
            self.not_found("carregar_Pagina")
            
        
        self.scroll_down(500)
        
        if not self.find( "nome", matching=0.97, waiting_time=10000):
            self.not_found("nome")
        self.click()
        self.paste("Jeová")
        
        if not self.find( "email", matching=0.97, waiting_time=10000):
            self.not_found("email")
        self.click()

        self.paste("jeeova@hotmail.com")

        
        if not self.find( "numero_whatsapp", matching=0.97, waiting_time=10000):
            self.not_found("numero_whatsapp")
        self.click()
        #Número para teste
        self.paste("11999999999")
        
        
        if not self.find( "cadastrar", matching=0.97, waiting_time=10000):
            self.not_found("cadastrar")
        self.click()



        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
