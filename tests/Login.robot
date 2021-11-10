*Settings*
Documentation       Login test suite

Resource    ${EXECDIR}/resources/Base.robot

Test Setup      Start Session
Test Teardown   Finish Session

*Test Cases*
User Login

    ${user}                     Factory User Login
    
    Go To Login Page
    Fill Credentials            ${user}
    Submit Credentials
    User Should Be Logged In        ${user}

Incorrect Pass
    [Tags]          inv_pass
    ${user}         Create Dictionary       email=marcio.peneluca@hotmail.com       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Modal Content Should Be     Usuário e/ou senha inválidos.

User Not Found
    [Tags]          user_404
    ${user}         Create Dictionary       email=marcio.peneluca@404.com       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Modal Content Should Be     Usuário e/ou senha inválidos.

Incorrect Email
    [Tags]          inv_email
    ${user}         Create Dictionary       email=marcio.peneluca.com.br       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Should Be Type Email 

Required Email
    [Tags]          req_email
    ${user}         Create Dictionary       email=       password=abc123

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Empty Field       E-mail obrigatório

Required Password
    [Tags]          req_pass
    ${user}         Create Dictionary       email=marcio.peneluca@hotmail.com       password=

    Go To Login Page
    Fill Credentials        ${user}
    Submit Credentials
    Empty Field       Senha obrigatória

Required Fields
    [Tags]          req_fields
    ${user}                 Create Dictionary       email=      password=       msg1=E-mail obrigatório       msg2=Senha obrigatória
      
    Go To Login Page
    Fill Credentials            ${user}
    Submit Credentials
    Empty Required Fields       ${user}