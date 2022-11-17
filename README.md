
# Investment Strategy Analysis

## Инструкция по запуску

1. Установите Docker (установка на [Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru), [Windows](https://docs.docker.com/desktop/install/windows-install/)) и Node.js ([Linux](https://help.reg.ru/support/servery-vps/oblachnyye-servery/ustanovka-programmnogo-obespecheniya/kak-ustanovit-node-js-na-ubuntu), [Windows](https://nodejs.org/en/download/)).
2. Скачайте проект на локальный компьютер.  
3. Перейдите в ту директорию, куда скачали папку с проектом. На Linux зайдите в папку "scripts" и запустите в терминале `sudo ./start.sh`. На Windows запустите в терминале `docker-compose up --build --force-recreate`.
4. Когда сервер поднимется, к нему можно будет сделать пинг через браузер: http://localhost:8000/ping:     
   
   <p align="center">
      <img src="https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/ping.png">
   </p>
5. Титульная страница будет доступна в браузере по адресу: http://localhost:5001:
   ![title_page](https://github.com/Investment-Strategy-Analysis/investment-strategy-analysis/blob/main/instruction_imgs/title_page.png) 
   
6. Чтобы остановить работу сервера, нажмите в терминале `Ctrl + C`.


