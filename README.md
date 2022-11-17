
# Investment Strategy Analysis

## Инструкция по запуску

1. Установите Docker (установка на [Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru), [Windows](https://docs.docker.com/desktop/install/windows-install/)) и Node.js ([Linux](https://help.reg.ru/support/servery-vps/oblachnyye-servery/ustanovka-programmnogo-obespecheniya/kak-ustanovit-node-js-na-ubuntu), [Windows](https://nodejs.org/en/download/)).
2. Скачайте проект на локальный компьютер.  
3. Перейдите в ту директорию, куда скачали проект. На Linux зайдите в папку "scripts" и запустите в терминале `sudo ./start.sh`. На Windows запустите в терминале `docker-compose up --build --force-recreate`.
4. Когда сервер поднимется, к нему можно будет сделать пинг через браузер: http://localhost:8000/ping:     
   
   <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/ping.png">
   </p>
5. Титульная страница доступна в браузере по адресу: http://localhost:5001/hisa/:
   ![title_page](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/title_page.png) 
   
6. Страница с регистрацией доступна в браузере по адресу http://localhost:5001/auth/signup/:    
   
   ![port5001_signup](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/sign_up.png) 
7. Страница авторизации доступна в браузере по адресу http://localhost:5001/auth/login/:  
    
   ![port5001_login](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/log_in.png)   
8. Если страницы регистрации и авторизации, а также титульная страница, не отображаются, можно поднять контейнер для ui_service отдельно. Убедитесь, что Node.js уже    установлен.  
9. Не отключая уже запущенный сервер, вернитесь в корневую папку и перейдите в директорию "services/ui_service":

    <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/ui_service.png">
   </p>

 10. Выполните последовательно в данной директории команды `npm install`, затем `npm run dev`.
 11. После этого страницы должны стать доступны в браузере по адресам, указанным в пунктах 5-7 соответственно. Также эти страницы могут быть доступны по альтернативным адресам, перечисленным в консоли (для примера ниже это адреса  http://172.22.224.1:5001/auth/signup,  http://172.22.224.1:5001/auth/login и т.д.):
     
     <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/my_local_addresses.png">
   </p>
11. Чтобы остановить работу любого сервера, нажмите Ctrl + C.

### Запуск на Windows
1. Установите и запустите [Docker Desktop](https://docs.docker.com/desktop/install/windows-install/). Если при запуске возникает ошибка, пробуйте перезапустить еще раз, периодически перезагружая компьютер. Обычно он запускается только с 3-5 раза.  
2. Если при запуске докера выдается сообщение о проблемах с WSL, проделайте шаги 1-6 по вот [этой инструкции](https://learn.microsoft.com/ru-ru/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package). В частности, это нужно для того, чтобы у под Windows запускались скрипты `.sh`.
3. Установите [Node.js](https://nodejs.org/en/download/).  
4. Скачайте проект из репозитория и запустите файл `docker-compose.yaml`.Это можно сделать, например, через IDE, нажав на 2 зеленые стрелочки:  

   <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/docker-compose.png">
   </p>
   
5. Перейдите в ту директорию, куда скачали проект, зайди в папку "scripts" и запустите в терминале `./start.sh`.
6. Если при запуске докера никаких сообщений о проблемах с WSL не было, но на шагах 4-5 все равно возникает ошибка, попробуйте все же проделать действия из пункта 2. 
7. После этого начнет подниматься сервер, это может занять продолжительное время. Как только все запустится, основной сервер будет работать по адресу                 http://localhost:8000:     
   
   <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/main_server.png">
   </p>
8. Титульная страница доступна в браузере по адресу: http://localhost:5001/hisa/:
   
   ![title_page](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/title_page.png) 
9. Страница с регистрацией доступна в браузере по адресу http://localhost:5001/auth/signup/:    
   
   ![port5001_signup](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/sign_up.png) 
10. Страница автоизации доступна в браузере по адресу http://localhost:5001/auth/login/:  
    
   ![port5001_login](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/log_in.png)   
11. Если страницы регистрации и авторизации, а также титульная страница, не отображаются, можно поднять контейнер для ui_service отдельно. Убедитесь, что Node.js уже установлен.  
12. Не отключая уже запущенный сервер, вернитесь в корневую папку и перейдите в директорию "services/ui_service":

   <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/ui_service.png">
   </p>

 13. Выполните последовательно в данной директории команды `npm install`, затем `npm run dev`.
 14. После этого страницы должны стать доступны в браузере по адресам, указанным в пунктах 8-10 соответственно. Также эти страницы могут быть доступны по альтернативным адресам, перечисленным в консоли (для примера ниже это адреса  http://172.22.224.1:5001/auth/signup,  http://172.22.224.1:5001/auth/login и т.д.):
     
     <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/my_local_addresses.png">
   </p>
15. Чтобы остановить работу любого сервера, нажмите Ctrl + C. 

