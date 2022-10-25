
# Investment Strategy Analysis

## Инструкция по запуску
### Запуск на Linux  

1. Установите Docker Compose (можно через терминал, как, например [здесь](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru)). Также, скорее всего, потребуется установить [Node.js](https://help.reg.ru/support/servery-vps/oblachnyye-servery/ustanovka-programmnogo-obespecheniya/kak-ustanovit-node-js-na-ubuntu)  
2. Скачайте проект на локальный компьютер.  
3. Перейдите в ту директорию, куда скачали проект, зайди в папку "scripts" и запустите в терминале sudo ./start.sh  
4. После этого начнет подниматься сервер, это может занять продолжительное время. Как только все запустится, основной сервер будет работать по адресу                http://localhost:8000:     
   
   <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/main_server.png">
   </p>
   
5. Страница с регистрацией доступна в браузере по адресу http://localhost:5001/auth/signup/:    
   
   ![port5001_signup](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/sign_up.png) 
6. Страница автоизации доступна в браузере по адресу http://localhost:5001/auth/login/:  
    
   ![port5001_login](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/log_in.png)   
7. Если страницы регистрации и авторизации не отображаются, можно поднять контейнер для ui_service отдельно. Убедитесь, что Node.js уже установлен.  
8. Не отключая уже запущенный сервер, вернитесь в корневую папку и перейдите в директорию services/ui_service:

    <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/ui_service.png">
   </p>

 9. Выполните последовательно в данной директории команды `npm install`, затем `npm run dev`.
 10. После этого страницы должны стать доступны в браузере по адресам, указанным в пунктах 5 и 6 соответственно. Также эти страницы могут быть доступны по альтернативным адресам, перечисленным в консоли (для примера ниже это адреса  http://172.22.224.1:5001/auth/signup,  http://172.22.224.1:5001/auth/login и т.д.):
     
     <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/my_local_addresses.png">
   </p>
11. Чтобы остановить работу любого сервера, нажмите `Ctrl+C`.




