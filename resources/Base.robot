*Settings*
Documentation       Arquivo Base do Projeto de Testes

Library         Browser
Library         Collections

Library         factories/Users.py

Resource        actions/_SharedActions.robot
Resource        actions/AuthActions.robot
Resource        actions/SignupActions.robot
Resource        actions/GeekActions.robot

Resource        Database.robot
Resource        Helpers.robot

*Variables*
${BASE_URL}         https://getgeeks-peneluca.herokuapp.com 

*Keywords*
Start Session
    New Browser     chromium        headless=False      slowMo=00:00:00
    New Page        ${BASE_URL}

Finish Session
    Take Screenshot     fullPage=True